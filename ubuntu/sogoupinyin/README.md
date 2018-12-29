## ubuntu 18.04 install sogoupinyin
### 2018-12-29

```sh
# ubuntu 18.04
# download sougoupinyin
# https://pinyin.sogou.com/linux/?r=pinyin

# install Fcitx
sudo apt install fcitx

# <setting: system> [Region&Language: Manage Installed Languages]
# [Keyboard input method system] -> fcitx

# dpkg install sogoupinyun deb
sudo dpkg -i sogoupinyin_2.2.0.0108_amd64.deb
# ps: when dpkg error
sudo apt  --fix-broken install
sudo dpkg -i sogoupinyin_2.2.0.0108_amd64.deb


# system layout
# <Keboard: img> [configure Current Input Method] -> [+] [Sogou Pinyin]
```

