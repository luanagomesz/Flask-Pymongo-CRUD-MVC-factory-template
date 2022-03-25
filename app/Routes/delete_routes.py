from app.controllers import posts_controller


def delete_routes(app):

    @app.delete("/posts/<id>")
    def delete_post(id):
        return posts_controller.delete_post(int(id))
