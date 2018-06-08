Supervisor
==========

安装
--

```sh
# ubuntu
sudo apt-get install supervisor

# centos 7
yum install supervisor.noarch
```

使用
--

```sh
# 默认配置文件
# 进入默认的配置目录
cd /etc/supervisor
# 查看配置文件
cat /etc/supervisor/supervisord.conf


# 手动生成配置文件 /etc/supervisor
# 创建文件夹
mkdir /etc/supervisor -p
# 创建配置文件
echo_supervisord_conf > /etc/supervisor/supervisord.conf

# 为了不将所有新增配置信息全写在一个配置文件里，这里新建一个文件夹，每个程序设置一个配置文件，相互隔离
mkdir /etc/supervisor/conf.d/ -p

# 加入以下配置信息
[include]
files = /etc/supervisor/conf.d/*.conf

# 在supervisord.conf中设置通过web可以查看管理的进程，加入以下代码（默认即有，取消注释即可
[inet_http_server]
port=9001
username=user
password=123

# 修改配置, 创建配置需要的文件
sudo touch /var/run/supervisor.sock
sudo chmod 777 /var/run/supervisor.sock

sudo touch /var/run/supervisor.pid
sudo chmod 777 /var/run/supervisor.pid


sudo touch /var/log/supervisor.log
sudo chmod 777 /var/log/supervisor.log
```

命令
--

```sh
# 启动
# 1.谁系统的启动自动启动
supervisord -c /etc/supervisor/supervisord.conf
# 2.子程序的管理系统
supervisorctl -c /etc/supervisor/supervisord.conf


sudo unlink /var/run/supervisor.sock
```

其他
--

```sh
# 查看是否使用 9001  *:9001(第4列)
ss -anpt | grep 9001
```

例子
--

```conf
# 配置文件 tornado 例子

[program:app] ; 程序名称，在 supervisorctl 中通过这个值来对程序进行一系列的操作
autorestart=True      ; 程序异常退出后自动重启
autostart=True        ; 在 supervisord 启动的时候也自动启动
redirect_stderr=True  ; 把 stderr 重定向到 stdout，默认 false
environment=PATH="/home/shihongguang/.virtualenvs/python3_django/bin"  ; 可以通过 environment 来添加需要的环境变量，一种常见的用法是使用指定的 virtualenv 环境
command=python3 async_server.py  ; 启动命令，与手动在命令行启动的命令是一样的
user=root           ; 用哪个用户启动
directory=/home/shihongguang/Templates/net_server/net_server/  ; 程序的启动目录
stdout_logfile_maxbytes = 20MB  ; stdout 日志文件大小，默认 50MB
stdout_logfile_backups = 20     ; stdout 日志文件备份数
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile = /data/logs/usercenter_stdout.log

```