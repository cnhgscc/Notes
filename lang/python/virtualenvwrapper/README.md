virtualenvwrapper
=================
安装
--
```sh
pip install virtualenvwrapper
pip install virtualenvwrapper-win　　#Windows使用该命令
```
配置
--
```sh
# ~/.bashrc
# virtualenvwrapper存放虚拟环境目录
# export WORKON_HOME=~/Pyenv

# virtrualenvwrapper 在那个目录
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3

# 让系统识别命令 bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper.sh

# 启用配置　
source ~/.bashrc
```
使用
--
```sh
# 查看python3
which python3

# 创建虚拟环境venv 
# 指定解释器 /usr/bin/python3
mkvirtualenv --python=/usr/bin/python3 venv
```
命令
--
```sh
# 查看当前的虚拟环境目录
workon
# 退出虚拟环境
deactivate
# 删除虚拟环境
rmvirtualenv venv
```
