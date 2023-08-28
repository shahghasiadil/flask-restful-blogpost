from flask import request
from flask_restful import Resource

class BlogPostController(Resource):
    def __init__(self, use_cases, presenter):
        self.use_cases = use_cases
        self.presenter = presenter
    def get(self, post_id=None):
        if post_id:
            post = self.use_cases.get_post(post_id)
            if post:
                return self.presenter.present(post), 201
            else:
                return {'message': 'Post not found'}, 404
        else:
            posts = self.use_cases.getAll()
            if posts:
                return self.presenter.getPosts(posts), 200
            else:
                return {'message': 'Post not found'}, 404
    def post(self):
        data = request.get_json()
        post = self.use_cases.create_post(data.get('title'), data.get('content'))
        return self.presenter.present(post), 201
    def put(self, post_id):
        data = request.get_json()
        post = self.use_cases.update_post(post_id, data)
        return self.presenter.present(post), 200

    def delete(self, post_id):
        return self.use_cases.delete_post(post_id)


