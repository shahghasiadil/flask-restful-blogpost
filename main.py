from flask import Flask
from flask_restful import Api
from config import Config
from routes.index import config_routes

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

config_routes(api)

if __name__ == '__main__':
    app.run()
