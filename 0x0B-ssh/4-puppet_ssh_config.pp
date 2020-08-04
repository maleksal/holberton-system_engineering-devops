# configure ssh connection with puppet
exec { 'echo -e "\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/holberton"" >> /etc/ssh/ssh_config':
    path => '/bin'
}
