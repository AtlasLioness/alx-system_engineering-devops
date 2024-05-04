# Puppet script that creates file in /tmp

file { 'ALX':
  path    => ' /tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
