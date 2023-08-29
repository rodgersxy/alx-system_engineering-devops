# Configuring your server with Puppet
# Ensure nginx service is running and enabled
# Configure nginx to listen on port 80

package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}
file { 'first content':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Hello World!',

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://github.com/rodgersxy permanent;',
}
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
