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

describe apt('https://packagecloud.io/sensu/prerelease/debian/') do
  it { should exist }
  it { should be_enabled }
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

describe file('/etc/sensu/backend.yml') do
  its('owner') { should eq 'sensu' }
  its('owner') { should eq 'sensu' }
  its('mode') { should cmp '0640' }
end

describe file('/etc/sensu/agent.yml') do
  its('owner') { should eq 'sensu' }
  its('owner') { should eq 'sensu' }
  its('mode') { should cmp '0640' }
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
