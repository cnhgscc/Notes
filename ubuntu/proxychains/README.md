# proxychains

```sh
# 安装proxychains
apt search proxychains
apt-get install proxychains

# 配置proxychains
sudo su
cat /etc/proxychains.conf
vim /etc/proxychains.conf

# 添加socks5到proxychains.conf
socks5 127.0.0.1 1080
```