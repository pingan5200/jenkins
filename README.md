# jenkins持续集成
## 一、测试环境部署LNMP  
### 1. 服务器ip及域名  
jenkins-server: 192.168.92.10  server10.example.com  
gitlab-server: 192.168.92.134  gitlab.example.com  
stage-server: 192.168.92.11  server11.example.com   
production-server: 192.168.92.12  server12.example.com   
production-server: 192.168.92.13  server13.example.com  
production-server: 192.168.92.14  server14.example.com   
### 2. 所有服务器/etc/hosts环境  
vim /etc/hosts  
192.168.92.10  server10.example.com  server10  
192.168.92.11  server11.example.com  server11  
192.168.92.12  server12.example.com  server12  
192.168.92.13  server13.example.com  server13  
192.168.92.14  server14.example.com  server14  
192.168.92.134 gitlab.example.com  
### 3. 在gitlab仓库，构建4个仓库
3.1 lnmp仓库：nginx安装包，php-fpm安装包及安装lnmp的脚本  
![image](https://github.com/pingan5200/jenkins/blob/master/lnmp.png)  
3.2 puppet仓库: puppet客户端配置文件  
![image](https://github.com/pingan5200/jenkins/blob/master/puppet.png)  
3.3 pupppet-server仓库: puppet服务端配置文件及传给客户端的nginx配置文件 
![image](https://github.com/pingan5200/jenkins/blob/master/puppet-server.png)  
3.4 php仓库： php开源站点包  
![image](https://github.com/pingan5200/jenkins/blob/master/php.png)  
### 4. 在jenkins上构建第一个任务start_lnmp部署lnmp  
4.1 动态参数构建需编辑文件，添加host和role  
[root@server10 ~]# vim /var/lib/jenkins/workspace/start_lnmp/host.list   
host=server10,server11,server12,server13  
role=LNMP,MYSQL  
4.2 开始构建  
4.2.1 动态参数化构建  
![image](https://github.com/pingan5200/jenkins/blob/master/one-job.png)  
4.2.2 用执行shell脚本  
详情见one_job  
![image](https://github.com/pingan5200/jenkins/blob/master/one-job2.png)  
4.3 start_lnmp任务执行完开始阻塞，执行下游Python_QA_TEST任务,下游任务执行成功，上游才释放结果成功  
传递环境变量给下游
![image](https://github.com/pingan5200/jenkins/blob/master/build_check.png)  
### 5. 构建第二个任务Python_QA_TEST白盒测试lnmp环境是否搭建成功
5.1 python脚本检查lnmp环境  
接收上游变量  
![image](https://github.com/pingan5200/jenkins/blob/master/env_get.png)  
代码详情见python_qa.py  
![image](https://github.com/pingan5200/jenkins/blob/master/python_qa.png)  






