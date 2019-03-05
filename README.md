# jenkins持续集成
## 一、部署LNMP  
1. 服务器ip及域名  
jenkins-server: 192.168.92.10  server10.example.com  
gitlab-server: 192.168.92.134  gitlab.example.com  
server: 192.168.92.11  server11.example.com   
server: 192.168.92.12  server12.example.com   
server: 192.168.92.13  server13.example.com  
server: 192.168.92.14  server14.example.com   
2. 准备/etc/hosts环境  
vim /etc/hosts  
192.168.92.10  server10.example.com  server10  
192.168.92.11  server11.example.com  server11  
192.168.92.12  server12.example.com  server12  
192.168.92.13  server13.example.com  server13  
192.168.92.14  server14.example.com  server14  
192.168.92.134 gitlab.example.com  

