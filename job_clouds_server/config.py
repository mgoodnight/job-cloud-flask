class Config(object):
    DEBUG = False
    FLASK_PORT = 5001
    PADDING = 20

    TWITTER = {
        'SIZE': (440, 220)
    }

    FACEBOOK = {
        'SIZE': (1200, 628)
    }

    INSTAGRAM = {
        'SIZE': (1080, 1080)
    }

    PINTEREST = {
        'SIZE': (222, 150)
    }

    LINKEDIN = {
        'SIZE': (1104, 736)
    }


class Development(Config):
    ENV = 'development'
    DEBUG = True


class Production(Config):
    ENV = 'production'


env_configs = {
    'development': Development,
    'production': Production
}