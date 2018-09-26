# Ubuntu 18.04.1 LTS

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

```

1.修改git权限  

     sudo chown -R shihongguang:shihongguang .git
