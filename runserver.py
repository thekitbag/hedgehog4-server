import os
from webapp import create_app, db
from config import Config, TestConfig, DevelopmentConfig, ProductionConfig

if os.environ['FLASK_ENV'] == 'development':
    app = create_app(DevelopmentConfig)
elif os.environ['FLASK_ENV'] == 'prod':
    app = create_app(ProductionConfig)
else:
    print('ENV NOT SET TO dev, staging or prod')


@app.shell_context_processor
def make_shell_context():
    return {'db': 'db'} 

