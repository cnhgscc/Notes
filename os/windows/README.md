scoop search zig

```
# 安装 scoop
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
iwr -useb get.scoop.sh | iex

# 配置安装地址
scoop config home D:\scoop

# 查询安装的软件
scoop search zig
# 安装软件 
scoop install zig
# zig
scoop bucket add versions
scoop install versions/zig-dev
scoop list zig
scoop reset zig

# 增加桶列表中
scoop bucket add extras

# 列出所有已添加的桶
scoop bucket list

# scoop search extras
scoop search extras

```