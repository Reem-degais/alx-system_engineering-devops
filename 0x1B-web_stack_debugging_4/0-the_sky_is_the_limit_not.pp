#increase the amount of request.

exec { 'fix--for--nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx.dpkg-dist',
  path => '/usr/local/bin/:/bin/',
}

exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path => '/etc/init.d/',
}
