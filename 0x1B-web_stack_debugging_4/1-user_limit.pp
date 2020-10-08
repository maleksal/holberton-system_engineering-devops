# user permission

exec { 'hard && soft nofile limit':
  command => "sed -i -e 's/^holberton hard .*/holberton hard nofile 64000/g'\
   -e 's/^holberton soft .*/holberton soft nofile 64000/g' /etc/security/limits.conf",
  path    => '/bin/',
}
