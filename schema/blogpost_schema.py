from firebase_admin import firestore

class BlogPostSchema:
    @staticmethod
    def get_default_post():
        return {
            'title': '',
            'content': '',
            'timestamp': firestore.SERVER_TIMESTAMP
        }
