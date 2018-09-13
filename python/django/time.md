django中时间的处理

```py
from django.utils.timezone import datetime, timedelta


# datetime 与 datetime 模块中的 datatime 一样ßß
# 2016-01-02
st = datetime.strptime("2016-01-02", "%Y-%m-%d")
st.strftime("%Y%m%d")
# next day
nt = st + timedelta(1)

```
