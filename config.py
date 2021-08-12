import os
class Config:
    NEWS_API_BASE_URL='http://newsapi.org/v1/sources?&apiKey={}'
    NEWS_API_TOP_ARTICLES_BASE_URL = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('d7e79514448524990878310691f78603d')
    SECRET_KEY='damn=secret'

    @staticmethod
    def init_app(app):
        pass
        
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}