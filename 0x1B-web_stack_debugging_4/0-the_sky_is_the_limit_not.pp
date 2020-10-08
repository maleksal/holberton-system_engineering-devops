# Fix nginx failed requests

exec { 'fix':
  command => 'sed -i \'s/^ULI.*=.*/ULIMIT="-n 4096"/g\' /etc/default/nginx',
  path    => '/bin/',
}

-> exec { 'restart nginx server':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}