# create a manifest that kills a process named killmenow
exec {'kill killmenow process':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin'
}
