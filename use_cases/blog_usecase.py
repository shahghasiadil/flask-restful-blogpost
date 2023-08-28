from entities import BlogPost

class BlogUseCases:
    def __init__(self, repository):
        self.repo = repository

    def create_post(self, title, content):
        post = BlogPost(title, content)
        return self.repo.add_post(post)

    def get_post(self, post_id):
        return self.repo.get_post(post_id)

    def getAll(self):
        return self.repo.getAll()

    def update_post(self, post_id, data):
        return self.repo.update_post(post_id, data)

    def delete_post(self, post_id):
        return self.repo.delete_post(post_id)
