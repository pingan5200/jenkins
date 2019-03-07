##############  STAGE UPDATE VERY SIMPLE ###########
sudo ssh server11 "pkill -9 nginx; systemctl stop php-fpm; systemctl stop mariadb"
sudo ssh server11 "cd /usr/local/nginx/html/php; sudo git -c http.sslVerify=false pull && sudo git -c http.sslVerify=false checkout re-1.0"
sudo ssh server11 "/usr/sbin/nginx; systemctl start php-fpm; systemctl start mariadb"
