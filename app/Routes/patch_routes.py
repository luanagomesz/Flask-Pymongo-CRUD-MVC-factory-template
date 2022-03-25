from app.controllers import posts_controller


def patch_routes(app):

    @app.patch('/posts/<id>')
    def update_post(id):
        return posts_controller.update_post(int(id))