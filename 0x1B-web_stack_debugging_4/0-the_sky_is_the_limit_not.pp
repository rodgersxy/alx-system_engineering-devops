# To  Fix requests limit in nginx
exec { 'fix requests limit':
  onlyif  => 'test -e /etc/default/nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/15/5555/' /etc/default/nginx && sudo service nginx restart",
}
