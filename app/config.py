class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/pdf-db?charset=utf8'
