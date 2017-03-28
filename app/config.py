class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
    NAME = 'kaige'
    PASSWORD = 'kaige'
    IP = '192.168.1.60'
    DB = 'pdf'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + NAME + ':' + PASSWORD + '@' + IP + ':3306/' + DB + '?charset=utf8'
