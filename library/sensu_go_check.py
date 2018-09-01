#!/usr/bin/env python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: sensu_go_check

short_description: Configure Sensu Go checks

version_added: "2.6"

description:
    - "Configure and manage Sensu Go checks leveraging sensuctl"

options:
    name:
        description:
            - The name of the Sensu check to add/delete
        required: false
    state:
        description:
            - Whether you want to list/add/delete Sensu Go checks
        required: true

author:
    - Jared Ledvina (@jaredledvina)
'''

EXAMPLES = '''
- name: Create a check
  sensu_go_check:
    name: hello
    command: /bin/true
    state: present

- name: Delete a check
  sensu_go_check:
    name: hello
    command: /bin/true
    state: absent

- name: List all checks
  sensu_go_check:
    state: list
  register: sensu_go_checks
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
message:
    description: The output message that the sample module generates
'''

from ansible.module_utils.basic import AnsibleModule
import json

class Sensuctl(object):
    def __init__(self, module):
        self.state = module.params['state']
        self.sensuctl_bin = module.get_bin_path('sensuctl', required=True)


    def command(self, module, positive_filter, action, extra_flags=[]):
        '''Runs sensuctl and returns jsonified stdout if possible'''
        command = [
            self.sensuctl_bin,
            positive_filter,
            action
        ]
        if action == 'list':
            command.append('--format=json')
        if extra_flags:
            for flag in extra_flags:
                command.append(flag)
        rc, stdout, stderr= module.run_command(command, check_rc=True)
        try:
            output = json.loads(stdout)
        except ValueError:
            output = stdout.strip()
        return output


    def checks_list(self, module):
        '''Gets checks'''
        return self.command(module, 'check', 'list')


    def check_create(self, module, name, command, interval, subscriptions, extra_flags):
        '''Creates a check'''
        extra_flags.append(name)
        extra_flags.append('--subscriptions')
        extra_flags.append(','.join(subscriptions))
        extra_flags.append('--command')
        extra_flags.append(command)
        extra_flags.append('--interval')
        extra_flags.append(interval)
        return self.command(module, 'check', 'create', extra_flags=extra_flags)


    def check_delete(self, module, name, extra_flags):
        '''Deletes a check'''
        extra_flags.append(name)
        extra_flags.append('--skip-confirm')
        return self.command(module, 'check', 'delete', extra_flags=extra_flags)



def run_module():
    module_args = dict(
        name=dict(type='str', required=False),
        state=dict(type='str', required=False, default='list'),
        flags=dict(type='list', required=False, default=[]),
        command=dict(type='str', required=False),
        interval=dict(type='str', required=False, default='60'),
        subscriptions=dict(type='list', required=False, default=[])
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        return result

    sensuctl = Sensuctl(module)
    # Fetch the existing checks so we know what we're working with
    checks = sensuctl.checks_list(module)
    check_names = [check['name'] for check in checks]

    if module.params['state'] == 'list':
        result['checks'] = checks
    elif module.params['state'] == 'present':
        if module.params['name'] not in check_names:
            check = sensuctl.check_create(
                        module,
                        module.params['name'],
                        module.params['command'],
                        module.params['interval'],
                        module.params['subscriptions'],
                        module.params['flags']
                    )
            # Refresh the checks after adding
            checks = sensuctl.checks_list(module)
            result['checks'] = checks
            result['changed'] = True
            result['message'] = check
        else:
            result['message'] = 'Check already defined in Sensu'.format(
                                    module.params['name']
                                )
    elif module.params['state'] == 'absent':
        if module.params['name'] in check_names:
            check = sensuctl.check_delete(
                        module,
                        module.params['name'],
                        module.params['flags']
                    )
            # Refresh the checks after deleting
            checks = sensuctl.checks_list(module)
            result['checks'] = checks
            result['changed'] = True
            result['message'] = check
        else:
            result['message'] = 'Check not found in Sensu: {}'.format(
                                    module.params['name']
                                )
    else:
        module.fail_json(
                msg='Unknown module state: {}'.format(module.params['state']),
            **result
        )
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
