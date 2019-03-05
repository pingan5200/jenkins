# jenkins持续集成
## 一、部署LNMP  
1. 服务器ip及域名  
jenkins-server: 192.168.92.10  server10.example.com  
gitlab-server: 192.168.92.134  gitlab.example.com  
server: 192.168.92.11  server11.example.com   
server: 192.168.92.12  server12.example.com   
server: 192.168.92.13  server13.example.com  
server: 192.168.92.14  server14.example.com   
2. 所有服务器/etc/hosts环境  
vim /etc/hosts  
192.168.92.10  server10.example.com  server10  
192.168.92.11  server11.example.com  server11  
192.168.92.12  server12.example.com  server12  
192.168.92.13  server13.example.com  server13  
192.168.92.14  server14.example.com  server14  
192.168.92.134 gitlab.example.com  
3. 构建gitlab仓库，构建5个仓库存放的分别为  
lnmp仓库：nginx安装包，php-fpm安装包  
puppet仓库: puppet客户端配置文件
pupppet-server仓库: puppet服务端配置文件及传给客户端的nginx配置文件  
php仓库： php开源站点包  
![image](https://github.com/pingan5200/jenkins/blob/master/repo.png)  


