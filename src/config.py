class Config:
    SECRET_KEY = 'ww^tCK%8n3%X2aK8PwO'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'optirute_db'

config = {
    'development' : DevelopmentConfig
}