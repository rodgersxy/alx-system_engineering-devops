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

file_line { 'redirect_me page':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;',
}
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
