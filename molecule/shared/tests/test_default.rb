# frozen_string_literal: true

# Debian Specific Things
if os.debian?
  describe package('curl') do
    it { should be_installed }
  end

  describe package('gnupg') do
    it { should be_installed }
  end

  describe package('debian-archive-keyring') do
    it { should be_installed }
  end

  describe package('apt-transport-https') do
    it { should be_installed }
  end
end

if os.name == 'debian'
  describe apt('https://packagecloud.io/sensu/stable/debian/') do
    it { should exist }
    it { should be_enabled }
  end
  describe apt('https://packagecloud.io/sensu/community/debian/') do
    it { should_not exist }
  end
end

if os.name == 'ubuntu'
  describe apt('https://packagecloud.io/sensu/stable/ubuntu/') do
    it { should exist }
    it { should be_enabled }
  end
  describe apt('https://packagecloud.io/sensu/community/ubuntu/') do
    it { should exist }
    it { should be_enabled }
  end
end

if os.redhat?
  # AmazonLinux 1 ships with python27-pygpgme skip testing for it
  unless os.name == 'amazon' && os.release == '2018.03'
    describe package('pygpgme') do
      it { should be_installed }
    end
  end

  describe package('yum-utils') do
    it { should be_installed }
  end

  describe yum.repo('sensu_go') do
    it { should exist }
    it { should be_enabled }
  end

  describe yum.repo('sensu_go-source') do
    it { should exist }
    it { should be_enabled }
  end

  describe yum.repo('sensu_go_community') do
    it { should exist }
    it { should be_enabled }
  end

  describe yum.repo('sensu_go_community-source') do
    it { should exist }
    it { should be_enabled }
  end
end

describe package('sensu-go-backend') do
  it { should be_installed }
end

describe package('sensu-go-agent') do
  it { should be_installed }
end

describe package('sensu-go-cli') do
  it { should be_installed }
end

describe file('/etc/default/sensu-agent') do
  it { should_not exist }
end

describe file('/etc/sysconfig/sensu-agent') do
  it { should_not exist }
end

describe file('/etc/default/sensu-backend') do
  it { should_not exist }
end

describe file('/etc/sysconfig/sensu-backend') do
  it { should_not exist }
end

describe file('/etc/sensu/') do
  it { should be_directory }
  its('owner') { should eq 'sensu' }
  its('owner') { should eq 'sensu' }
  its('mode') { should cmp '0750' }
end

describe file('/etc/sensu/backend.yml.example') do
  it { should_not exist }
end

describe file('/etc/sensu/backend.yml') do
  its('owner') { should eq 'sensu' }
  its('owner') { should eq 'sensu' }
  its('mode') { should cmp '0640' }
end

describe yaml('/etc/sensu/backend.yml') do
  its('state-dir') { should eq '/var/lib/sensu/sensu-backend' }
end

describe file('/etc/sensu/agent.yml.example') do
  it { should_not exist }
end

describe file('/etc/sensu/agent.yml') do
  its('owner') { should eq 'sensu' }
  its('owner') { should eq 'sensu' }
  its('mode') { should cmp '0640' }
end

describe yaml('/etc/sensu/agent.yml') do
  its(['backend-url', 0]) { should eq 'ws://127.0.0.1:8081' }
  its('cache-dir') { should eq '/var/cache/sensu/sensu-agent' }
end

# Debian 10/Buster/Sid is not detected as SystemD correctly
# https://github.com/inspec/inspec/pull/4233
if os.release == 'buster/sid'
  describe systemd_service('sensu-backend') do
    it { should be_enabled }
    it { should be_installed }
    it { should be_running }
  end

  describe systemd_service('sensu-agent') do
    it { should be_enabled }
    it { should be_installed }
    it { should be_running }
  end
else
  describe service('sensu-backend') do
    it { should be_enabled }
    it { should be_installed }
    it { should be_running }
  end

  describe service('sensu-agent') do
    it { should be_enabled }
    it { should be_installed }
    it { should be_running }
  end
end
