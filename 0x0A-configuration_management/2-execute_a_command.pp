# kill process using puppet
exec { 'pkill killmenow':
    path => '/usr/bin'
}