django中时间的处理

```py
from django.utils.timezone import datatime, timedelta

# 2016-01-02
st = datetime.strptime("2016-01-02", "%Y-%m-%d")
# next day
nt = st + timedelta(1)

```
