# Puppet to make changes to our configuration file.
file { 'SSH client configuration':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => "
    Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
    ",
}
