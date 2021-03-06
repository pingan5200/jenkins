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
代码详情见python_qa_test1.py  
![image](https://github.com/pingan5200/jenkins/blob/master/python_qa.png)  

## 二.php代码修改持续集成  
### 1.创建三个任务
![image](https://github.com/pingan5200/jenkins/blob/master/task-2.png)    
1.1 第一个任务  
jenkins检查server11，从PHP仓库的 re-1.0分⽀上不断的检查更新 如果发生了更新 那么就继续触发 下游server11的 stage分支更新代码  
图1  
![image](https://github.com/pingan5200/jenkins/blob/master/GIT_TRIGGER.png)   
图2  代码见GIT_TRIGGER.sh  
![image](https://github.com/pingan5200/jenkins/blob/master/TRIGGER-2.png)   
1.2 第二个任务  
DEPLOY_STAGE  这个任务比较简单，部署server11 ，就是把stage机器上的stage分支下的代码更新,然后继续触发下游的测试任务  
图一
![image](https://github.com/pingan5200/jenkins/blob/master/DEPLOY-1.png)   
图二  代码见DEPLOY_STAGE.sh  
![image](https://github.com/pingan5200/jenkins/blob/master/DEPLOY-2.png)   
1.3 第三个任务  
jenkins检查server11测试机stage分支php代码是否满足状态码200 大于98,如果合格，合并master分支  
图一  
![image](https://github.com/pingan5200/jenkins/blob/master/python-qa-1.png)   
图二  
![image](https://github.com/pingan5200/jenkins/blob/master/python-qa-2.png)   
## 三.发布测试
1. server11发布测试前仓库re-1.0分支代码  
![image](https://github.com/pingan5200/jenkins/blob/master/before_re-1.0.png)   
2. 运维人员修改re-1.0分支php代码后，如图：  
![image](https://github.com/pingan5200/jenkins/blob/master/after_re-1.0.png)   
3. 发布测试  
发布成功  
4. master分支代码，已经更新  
[root@server11 php]# cat README.md 
PHP  
update php re-1.0 merge master  





