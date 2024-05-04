# Puppet script to make changes to SSH config file

file_line { 'disable password auth':
	ensure => 'present',
	path => '/etc/ssh/ssh_config',
	line => 'PasswordAuthentication no',
}
file_line { 'specify identity file':
	ensure => 'present',
	path => '/etc/ssh/ssh_config',
	line => 'IdentityFile ~/.ssh/school',
}
