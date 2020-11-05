# Install Ruby
exec { 'apt-get install -y ruby':
    path => '/usr/bin'
}
# Install puppet-lints
exec { 'gem install puppet-lint -v 2.1.1':
    path => '/usr/bin'
}