#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Jared Ledvina <jaredledvina@gmail.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json

from ansible.module_utils.basic import AnsibleModule, env_fallback
from ansible.module_utils.urls import fetch_url, url_argument_spec
from ansible.module_utils._text import to_native

class AnsibleModuleError(Exception):
    def __init__(self, results):
        self.results = results

    def __repr__(self):
        print('AnsibleModuleError(results={0})'.format(self.results))


# TODO: Once 2.8.0 is released, bump min support and switch to:
# from ansible.module_utils.common.dict_transformations import recursive_diff
# https://github.com/ansible/ansible/blob/3b08e75eb2336950e0d1a617fa89ff9afb43bc72/lib/ansible/module_utils/common/dict_transformations.py#L126-L141
def recursive_diff(dict1, dict2):
    left = dict((k, v) for (k, v) in dict1.items() if k not in dict2)
    right = dict((k, v) for (k, v) in dict2.items() if k not in dict1)
    for k in (set(dict1.keys()) & set(dict2.keys())):
        if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
            result = recursive_diff(dict1[k], dict2[k])
            if result:
                left[k] = result[0]
                right[k] = result[1]
        elif dict1[k] != dict2[k]:
            left[k] = dict1[k]
            right[k] = dict2[k]
    if left or right:
        return left, right
    else:
        return None


class SensuGo(AnsibleModule):
    def __init__(self, argument_spec, attributes, resource, **kwargs):
        self.headers = {"Content-Type": "application/json"}
        # List of attributes from the upstream specification
        self.attributes = attributes
        # The type of resource to work with. i.e.: checks, handlers, etc.
        self.resource = resource
        args = dict(
            name=dict(type='str', required=True),
            host=dict(
                type='str',
                required=True,
                fallback=(env_fallback, ['ANSIBLE_SENSU_GO_HOST'])
            ),
            port=dict(
                type='int',
                default=8080,
                fallback=(env_fallback, ['ANSIBLE_SENSU_GO_PORT'])
            ),
            protocol=dict(
                type='str',
                default='http',
                choices=['http', 'https'],
                fallback=(env_fallback, ['ANSIBLE_SENSU_GO_PROTOCOL'])
            ),
            username=dict(
                type='str',
                default='admin',
                aliases=['url_username'],
                fallback=(env_fallback, ['ANSIBLE_SENSU_GO_USERNAME'])
            ),
            password=dict(
                type='str',
                default='P@ssword!',
                no_log=True,
                aliases=['url_password'],
                fallback=(env_fallback, ['ANSIBLE_SENSU_GO_PASSWORD'])
            ),
            namespace=dict(type='str', default='default'),
        )
        argument_spec.update(args)
        super(SensuGo, self).__init__(argument_spec=argument_spec, **kwargs)

    def get_base_url(self):
        return '%s://%s:%s' % (
            self.params.get('protocol'),
            self.params.get('host'),
            self.params.get('port')
        )

    def request(self, url, method="GET", data=None):
        if data:
            data = self.jsonify(data)
        try:
            resp, info = fetch_url(
                module=self,
                url=url,
                method=method,
                data=data,
                headers=self.headers
            )
        except Exception as e:
            raise AnsibleModuleError(results={'msg': 'Failed request to {0}'.format(url), 'exception': to_native(e)})
        # TODO: What error codes should we handle here?
        if info['status'] == -1:
            self.fail_json(msg='Request to {0} failed with: {1} {2}'.format(
                url,
                info['status'],
                info['msg']
            ))
        if info['status'] >= 500 or info['status'] == 401:
            self.fail_json(msg='Request to {0} failed with: {1} {2}'.format(
                url,
                info['status'],
                info['body'].strip()),
                status=info['status'],
                url=url,
                method=method,
                data=json.loads(data)
            )
        response = None
        if resp:
            response = resp.read()
            if response:
                try:
                    response = json.loads(response)
                except Exception as e:
                    raise AnsibleModuleError(results={'msg': 'Failed to parse response as JSON: {0}'.format(response), 'exception': to_native(e)})
        return response, info

    def auth(self):
        # Force basic auth to get access_token
        self.params['force_basic_auth'] = True
        url = '%s/auth' % self.get_base_url()
        response, info = self.request(url)
        self.headers.update({'Authorization': 'Bearer ' + response['access_token']})
        # Remove the following to prevent any basic auth from happening via fetch_url
        self.params.pop('url_username', None)
        self.params.pop('username', None)
        self.params.pop('url_password', None)
        self.params.pop('password', None)
        self.params.pop('force_basic_auth', None)

    def get_resources(self):
        url = '{0}/api/core/v2/namespaces/{1}/{2}'.format(
            self.get_base_url(),
            self.params['namespace'],
            self.resource
        )
        resp, info = self.request(url)
        return resp, info

    def get_resource(self):
        url = '{0}/api/core/v2/namespaces/{1}/{2}/{3}'.format(
            self.get_base_url(),
            self.params['namespace'],
            self.resource,
            self.params['name'])
        resp, info = self.request(url)
        return resp, info

    def put_resource(self, resource):
        url = '{0}/api/core/v2/namespaces/{1}/{2}/{3}'.format(
            self.get_base_url(),
            self.params['namespace'],
            self.resource,
            self.params['name'])
        resp, info = self.request(url, method='PUT', data=resource)
        return resp, info

    def post_resource(self, resource):
        url = '{0}/api/core/v2/namespaces/{1}/{2}'.format(
            self.get_base_url(),
            self.params['namespace'],
            self.resource)
        resp, info = self.request(url, method='POST', data=resource)
        return resp, info

    def delete_resource(self):
        url = '{0}/api/core/v2/namespaces/{1}/{2}/{3}'.format(
            self.get_base_url(),
            self.params['namespace'],
            self.resource,
            self.params['name'])
        resp, info = self.request(url, method='DELETE')
        return resp, info

    def create_check_definition(self):
        check = {}
        for attribute in self.attributes:
            check[attribute] = self.params[attribute]
        # Every check definition must include the following:
        check['metadata'] = {
            'namespace': self.params['namespace'],
            'name': self.params['name']
        }
        if self.params['metadata']:
            if self.params['metadata']['annotations']:
                check['metadata']['annotations'] = self.params['metadata']['annotations']
            if self.params['metadata']['labels']:
                check['metadata']['labels'] = self.params['metadata']['labels']
        return check
