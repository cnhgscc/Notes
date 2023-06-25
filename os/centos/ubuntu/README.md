# Ubuntu 18.04.1 LTS

1.更新源改为国内的更新源  
---------------------

文件/etc/apt/sources.list 内容替换 
    
```
#deb cdrom:[Ubuntu 18.04.1 LTS _Bionic Beaver_ - Release amd64 (20180725)]/ bionic main restricted  

deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```

```sh
# 更新
sudo apt update
sudo apt upgrade
```

2.常用软件与设置
--------------

```sh
# see system info
cat /etc/os-release

# modfiy hostname
nmtui

# apt
# path: /usr/bin

sudo apt install vim
sudo apt install git

# pycharm
# download pycharm from web
# set pycharm app   /usr/shar/applications
# pycharm applications  ~/.local/share/applications; touch charm.destop
# sh path /usr/local/bin/charm
tar xvf pycharm-professional-2018.2.3.tar.gz
mkdir lib_software
mv pycharm_software lib_software

# db
# mariadb
sudo apt install mariadb-server
# MySQL Workbench - a visual database modeling, administration and queuing tool
sudo apt install mysql-workbench

# sudo mysql
# set password
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('123456');
# cancel sudo
USE mysql;
UPDATE user SET plugin='mysql_native_password' WHERE user='root';

# redis
sudo apt install redis

# web
sudo install nginx
sudo install uwsgi
sudo apt install gunicorn3

# net-tools
sudo apt install net-tools

# openssh-server
sudo apt-get install openssh-server

# wrk
git clone https://github.com/wg/wrk.git
cd wrk
make
ln wrk /usr/local/bin

# openvpn
# doc https://www.cnblogs.com/huangweimin/articles/7638943.html
sudo apt install openvpn
sudo apt install  easy-rsa

dpkg -L easy-rsa


# python pip
sudo apt-get install python3-dev libmysqlclient-dev
pip install mysqlclient

# jdk 1.8
sudo apt install openjdk-8-jdk

# .bashrc
PATH=$PATH:$HOME

# Snap是Ubuntu母公司Canonical于2016年4月发布Ubuntu16.04时候引入的一种安全的、易于管理的、沙盒化的软件包格式，
# 与传统的dpkg/apt有着很大的区别
# Snap可以让开发者将他们的软件更新包随时发布给用户，而不必等待发行版的更新周期；
# 其次Snap应用可以同时安装多个版本的软件，比如安装Python2.7和Python3.3。
# 可以通过edge通道进行安装，也可以通过GTK+3、Qt frameworks、stable等通道进行安装需要的软件 
# 默认情况下，是通过stable的通道进行安装的

# 常用的使用方法
# 查询已经安装了的软件
sudo snap list

# 搜索要安装的Snap软件包
sudo snap find xxxx

# 查看Snap软件的更多信息
sudo snap info xxxx

# 安装Snap软件包
sudo snap install xxxx

# 更换软件安装通道
sudo snap switch –channel=xxxx xxxx

# 更新Snap软件包
sudo snap refresh xxxx

# 还原到之前版本
sudo snap revert xxxx

# 卸载Snap软件
sudo snap remove xxxx


# 软件管道切换
snap switch–channel=candidate vlc
snap refresh


# docker 安装例子
snap find docker
snap info docker
sudo snap install docker -stable

# docker 版本查看
docker --version

```

3.docker
--------

    https://registry.docker-cn.com
    http://hub-mirror.c.163.com
    https://docker.mirrors.ustc.edu.cn
    
    # /etc/docker/daemon.json 

    {
        "registry-mirrors": [" http://hub-mirror.c.163.com"],
        "insecure-registries": []
    }
    
    # 修改启动文件
    # /lib/systemd/system/docker.service
    # 启动增加配置文件引用
    ExecStart=/usr/bin/dockerd -H fd:// --config-file /etc/docker/daemon.json
   
    sudo groupadd docker     #添加docker用户组
    sudo gpasswd -a $USER docker     #将登陆用户加入到docker用户组中
    newgrp docker     #更新用户组
    docker ps    #测试docker命令是否可以使用sudo正常使用
   
}


## .bashrc

```sh

# virtualenvwrapper settings
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh

alias quit='deactivate'

# cmdline
alias xgunicorn='gunicorn -w 4 -k gevent -b '

alias xnetstat='sudo netstat -anpt | grep -w LISTEN | grep -w tcp'
alias xps='ps -ef | grep '

alias xwrk='wrk -c1000 -t8 -d5s --latency '

# curl
alias jpost='curl -X POST -H "Content-Type: application/json"'
alias jput='curl -X PUT -H "Content-Type: application/json"'

```


1.修改git权限  

     sudo chown -R shihongguang:shihongguang .git

2.权限  
	1-执行 2-写 3-读

