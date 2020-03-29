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
            url_username=dict(
                type='str',
                default='admin',
                aliases=['username'],
                fallback=(env_fallback, ['ANSIBLE_SENSU_GO_USERNAME'])
            ),
            url_password=dict(
                type='str',
                default='P@ssw0rd!',
                no_log=True,
                aliases=['password'],
                fallback=(env_fallback, ['ANSIBLE_SENSU_GO_PASSWORD'])
            ),
            namespace=dict(type='str', default='default'),
            validate_certs=dict(type='bool', default=True),
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
            self.fail_json(
                msg='Failed request to {0}'.format(url),
                exception=to_native(e)
            )
        # TODO: What error codes should we handle here?
        if info['status'] == -1:
            self.fail_json(msg='Request to {0} failed with: {1} {2}'.format(
                url,
                info['status'],
                info['msg']
            ))
        if info['status'] >= 500 or info['status'] in [400, 401, 409]:
            self.fail_json(msg='Request to {0} failed with: {1} {2}'.format(
                url,
                info['status'],
                info['body'].strip()),
                status=info['status'],
                url=url,
                method=method,
                data=data
            )
        # 404 leave resp as None
        # 204 has a resp but it's ''
        if resp and info['status'] not in [201, 204]:
            response = resp.read()
            try:
                return json.loads(response.decode('utf-8')), info
            except Exception as e:
                self.fail_json(
                    msg='Failed to parse response as JSON: {0}'.format(info),
                    response=response,
                    exception=to_native(e)
                )
        else:
            return resp, info

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
        metadata = self.params.get('metadata', {}) or {}
        annotations = metadata.get('annotations', None)
        labels = metadata.get('labels', None)

        if annotations:
            check['metadata']['annotations'] = annotations

        if labels:
            check['metadata']['labels'] = labels

        return check
