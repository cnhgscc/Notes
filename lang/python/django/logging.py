LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
       'standard': {
            'format': '[%(asctime)s] [%(threadName)s:%(thread)d] '
                      '[%(name)s:%(filename)s-%(lineno)d] '
                      '[%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'
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
            'filename': 'all.log',     # 日志输出文件
            'maxBytes': 1024*1024*5,   # 文件大小
            'backupCount': 5,          # 备份份数
            'formatter': 'standard',   # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'error.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'script.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'script.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}