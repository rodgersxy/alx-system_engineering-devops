# Ensure nginx package is installed
package { 'nginx':
  ensure  => 'installed',
}

# Configure Nginx to listen on port 80
file { 'first content':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

# Configure redirection
file_line { 'install':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://github.com/rodgersxy permanent;',
  require => Package['nginx'],  # This line ensures that the package is installed before this resource is managed
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
