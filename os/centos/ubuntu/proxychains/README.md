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

# 配置开启自动启动代理服务
sudo cp proxy.sh /etc/init.d/
sudo chmod 755 /etc/init.d/proxy.sh
cd /etc/init.d
sudo update-rc.d proxy.sh defaults 100
```