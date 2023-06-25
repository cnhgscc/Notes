Logging 
=====

Django1.8  
```python
#
# ----- logging base settings -----
#
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
       'standard': {
            'format': '[%(asctime)s] [%(threadName)s:%(thread)d] '
                      '[%(name)s:%(filename)s-%(lineno)d] '
                      '[%(module)s:%(funcName)s] '
                      '<%(levelname)s>\n'
                      '%(message)s'
       },
    },
    'filters': {},
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'django.log',
            'maxBytes': 1024*1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'django.log',
            'maxBytes': 1024*1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

# ------ logging add app logger -----
for app in INSTALLED_APPS:
    if app.startswith("django"):
        continue
    LOGGING['loggers'].setdefault(app, {
        'handlers': ['console', 'error'],
        'level': 'DEBUG',
        'propagate': False
    })
```