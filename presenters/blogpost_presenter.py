class BlogPostPresenter:
    def present(self, post):
        return {
            'id': post.post_id,
            'title': post.title,
            'content': post.content,
        }
    def getPosts(self, posts):
       return [self.present(post) for post in posts]