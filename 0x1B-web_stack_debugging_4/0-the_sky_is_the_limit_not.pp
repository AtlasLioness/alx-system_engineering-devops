# Puppet script to increase limit of nginx traffic
exec { 'fix-for-nginx':
  command => "sed -i 's/-n 15/-n 4096/g' /etc/default/nginx && service nginx restart",
  onlyif    => 'test -e /etc/default/nginx',
  provider  => 'shell',
}

# Nginx restart
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  subscribe   => Exec['fix-for-nginx'],
  refreshonly => true,
}
