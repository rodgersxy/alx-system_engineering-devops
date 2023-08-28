# 0x0C. Web server

## Resources
### Read or watch:
```
How the web works
Nginx
How to Configure Nginx
Child process concept page
Root and sub domain
HTTP requests
HTTP redirection
Not found HTTP response code
Logs files on Linux
```
* For reference:
```
RFC 7231 (HTTP/1.1)
RFC 7540 (HTTP/2)
```
* man or help:
```
scp
curl
```

## server:
```
# Install and setup nginx into the server
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
/var/www/html$ ls
echo "Hello World!" | sudo tee /var/www/html/index.html
ls
sudo nginx -t
sudo service nginx restart
sudo service nginx reload
```
