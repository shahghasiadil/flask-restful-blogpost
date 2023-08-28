class BlogPost:
    def __init__(self, title, content, post_id=None):
        self.post_id = post_id
        self.title = title
        self.content = content
    def __eq__(self, other):
        if not isinstance(other, BlogPost):
            return NotImplemented
        return (
            self.title == other.title and
            self.content == other.content and
            self.post_id == other.post_id
        )
