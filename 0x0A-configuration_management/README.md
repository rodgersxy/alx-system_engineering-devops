# 0x0A. Configuration management

## Resources

Intro to Configuration Management  
Puppet resource type: file (check “Resource types” for all manifest types in the left menu)  
Puppet’s Declarative Language: Modeling Instead of Scripting  
Puppet lint  
Puppet emacs mode  

## Install puppet
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

## Install puppet-lint
```
$ gem install puppet-lint

puppet-lint --version
```
