xrandr
======
新增加屏幕分辨率

```sh
# 文件: /etc/profile 
# 追加下面内容

cvt 1920 1080
xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode Virtual1 "1920x1080_60.00"
```