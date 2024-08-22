# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
exec { 'Change ULIMIT':
  command  => 'echo -e "holberton hard nofile 2500\nholberton soft nofile 25000" > /etc/security/limits.conf',
  provider => shell,
}
