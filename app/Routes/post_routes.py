from app.controllers import posts_controller


def post_routes(app):
    @app.post("/posts")
    def create_post():
       return posts_controller.create_post()

