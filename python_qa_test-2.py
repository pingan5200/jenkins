#!/usr/local/bin/python3
# -*- coding:utf-8 -*-


import os
import subprocess


# 检查nginx，php-fpm, mysqld服务
def remote_check(hostname, port):
    cmd_ssh = "sudo ssh" + ' ' + hostname + ' '
    cmd_netstat = "netstat -anlput"
    ssh_netstat = cmd_ssh + cmd_netstat
    server_result = get_shell_cmd(ssh_netstat)
    if "nginx" in server_result:
        print("Nginx is Running")
    else:
        print("Nginx is not Running")
        os._exit(1)
    if "php-fpm" in server_result:
        print("php-fpm is Running")
    else:
        print("php-fpm is not Running")
        os._exit(2)
    if "mysqld" in server_result:
        print("mysql is Running")
    else:
        print("mysql is not Running")
        os._exit(2)
    cmd_curl = "curl -q -s http://127.0.0.1:" + str(port) + "/php/index.php"
    cmd_grep = "|grep -i 'php version'"
    ssh_php = cmd_ssh + cmd_curl + cmd_grep
    php_result = get_shell_cmd(ssh_php)
    if "PHP Version" in php_result:
        print("php is Running")
    else:
        print("php is not Running")
        os._exit(3)


# 检查php刚部署时的源代码
def remote_check_web(hostname):
    cmd_ssh = "sudo ssh" + ' ' + hostname + ' '
    cmd_curl = "curl -q -I -s http://127.0.0.1/php/app/web.php"
    cmd_grep = "| grep 'HTTP/1.1 200 OK'"
    ssh_php_web = cmd_ssh + cmd_curl + cmd_grep
    web_result = get_shell_cmd(ssh_php_web)
    if "HTTP/1.1 200 OK" in web_result:
        print("php_web is Running")
    else:
        os._exit(4)
        print("php_web is not Running")


# 检查测试机修改的stage分支php代码, 合并代码
def remote_check_curl_100(hostname, port, stage):
    cmd_curl = "curl -I -m 10 -o /dev/null -s -w %{http_code}"
    cmd_url = "http://" + hostname + ':' + str(port) + "/php/app/web.php"
    cmd_line = cmd_curl + ' ' + cmd_url
    print(cmd_line)
    http_status = {}
    http_code = ['200', '404', '304', '301']
    for i in range(1, 101):
        curl_code = get_shell_cmd(cmd_line)
        # print(curl_code)
        if curl_code in http_code:
            http_status[curl_code] = http_status.get(curl_code, 0) + 1
    print(http_status)
    if http_status.get('200', 0) < 98:
        print("php_web have some problem")
        os._exit(5)
    else:
        print('http_code_percental:', str(http_status['200']) + "%")
        print(hostname)
        if hostname == "server11":
            cmd_git_commit = """cd /var/lib/jenkins/workspace/GIT_CODING_TRIGGER/php/;
            sudo git checkout master;
            sudo git merge %s;
            sudo git add .;
            sudo git commit -m"haha"
            sudo git -c http.sslVerify=false push origin master;
            """ % (stage, stage)
            get_shell_cmd(cmd_git_commit)
            print(cmd_git_commit)
        else:
            print(hostname)
            print('hostname NOT == server11')


def get_shell_cmd(cmd):
    proc = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            encoding='utf-8')
    try:
        outs, errs = proc.communicate()
        if errs:
            print(errs)
            os._exit(10)
        return outs
    except TimeoutExpired:
        proc.kill()
    except Exception as e:
        print(e)


hostname = os.getenv('RUN_SERVER_TO_QA')
print(hostname)
remote_check(hostname, 80)
remote_check_web(hostname)
remote_check_curl_100(hostname, 80, 're-1.0')
