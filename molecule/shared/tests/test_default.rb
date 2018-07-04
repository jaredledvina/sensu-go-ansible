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
  describe apt('https://packagecloud.io/sensu/nightly/debian/') do
    it { should exist }
    it { should be_enabled }
  end
end

if os.name == 'ubuntu'
  describe apt('https://packagecloud.io/sensu/nightly/ubuntu/') do
    it { should exist }
    it { should be_enabled }
  end
end

if os.redhat?
  describe package('pygpgme') do
    it { should be_installed }
  end

  describe package('yum-utils') do
    it { should be_installed }
  end

  describe yum.repo('sensu_prerelease') do
    it { should exist }
    it { should be_enabled }
  end

  describe yum.repo('sensu_prerelease-source') do
    it { should exist }
    it { should be_enabled }
  end
end

describe package('sensu-backend') do
  it { should be_installed }
end

describe package('sensu-agent') do
  it { should be_installed }
end

describe package('sensu-cli') do
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
  its('state-dir') { should eq '/var/lib/sensu' }
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
