# Fix nginx failed requests

exec { 'fix':
  command => 'sed -i \'s/^ULIMIT=.*/ULIMIT="-n 4096"/g\' /etc/default/nginx',
  path    => '/bin/',
}

exec { 'restart nginx server':
  command => 'servide nginx restart',
  path    => '/etc/init.d/',
}