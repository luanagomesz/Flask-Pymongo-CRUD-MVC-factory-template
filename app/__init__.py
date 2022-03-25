from .Routes import init_app
from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = False
    
    init_app(app)
    
    return app
