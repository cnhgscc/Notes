djcelery
=====

1. settings.py  
```python

import djcelery


#
# ----- django-celery(3.2.2) settings -----
#
djcelery.setup_loader()
BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']

```
