import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY= os.environ.get('APP_SECRET_KEY')
	GPT_API_KEY= os.environ.get('GPT_API_KEY')
	


class TestConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql:///hh4test'
	TESTING = True
	SECRET_KEY = 'supersecurepw4testing!'

class DevelopmentConfig(Config):
	APPLICATION_ROOT = '/api'
	SECRET_KEY = 'supersecurepw'

class ProductionConfig(Config):
	APPLICATION_ROOT = '/api'