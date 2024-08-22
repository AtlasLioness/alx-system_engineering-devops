# Puppet script to increase limit of nginx traffic
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/1024/" /etc/default/nginx',
  path    => '/etc/default/nginx'
}

# Nginx restart
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  subscribe   => Exec['fix-for-nginx'],
  refreshonly => true,
}
