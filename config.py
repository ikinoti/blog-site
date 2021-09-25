import os

class Config:
  SECRET_KEY = os.environ.get("SECRET_KEY")
  SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kinoti:1234@localhost/myblog"
  UPLOADED_PHOTOS_DEST = "app/static/photos"


class ProdConfig(Config):
    
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kinoti:1234@localhost/myblog_test"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kinoti:1234@localhost/myblog"
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}