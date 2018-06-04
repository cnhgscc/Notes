ssh
===
生成ssh-key
```sh

ssh-keygen -t rsa -C "18511828634@163.com"

cd　~/.ssh; ls -alh

# id_rsa
# id_rsa.pub
# known_host
# authorized_keys

# 实现免密码登录
ssh-copy-id  user@ip_addr
```