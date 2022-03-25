from app.controllers import posts_controller

def get_routes(app):
    @app.get('/posts')
    def get_all_posts():
        return posts_controller.get_posts()

    @app.get('/posts/<id>')
    def get_post_byId(id):
        return posts_controller.get_post_by_id(int(id))
    