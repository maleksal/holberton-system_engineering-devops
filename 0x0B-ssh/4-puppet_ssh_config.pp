# configure ssh connection with puppet
exec { 'echo -e "\tPasswordAuthentication no" >> /etc/ssh/ssh_config':
    path => '/bin'
}
exec { 'echo -e "\tIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config':
    path => '/bin'
}
