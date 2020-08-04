# configure ssh connection with puppet
exec { "configure_ssh":
	command => 'echo -e "\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/holberton"" >> /etc/ssh/ssh_config',
	path => ['/bin'],
}
