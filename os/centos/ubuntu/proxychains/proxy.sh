#!/bin/sh
### BEGIN INIT INFO
# Provides:          land.sh
# Required-start:    $local_fs $remote_fs $network $syslog
# Required-Stop:     $local_fs $remote_fs $network $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the svnd.sh daemon
# Description:       starts svnd.sh using start-stop-daemon
### END INIT INFO

#任务脚本
#进入要执行脚本目录
cd /home/shihongguang/proxy
#取得root权限，'123456'为密码，不用加引号，'ls'无实际作用
echo hong1013
#执行脚本./bin/mywork，sudo -S需要加上
ss-local -c proxy.json
