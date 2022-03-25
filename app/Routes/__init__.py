from .get_routes import get_routes
from .post_routes import post_routes
from .delete_routes import delete_routes
from .patch_routes import patch_routes

def init_app(app):
    get_routes(app)
    post_routes(app)
    patch_routes(app)
    delete_routes(app)