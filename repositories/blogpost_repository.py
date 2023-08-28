import firebase_admin
from firebase_admin import firestore, credentials, initialize_app
from schema import BlogPostSchema
from entities import BlogPost

import os
from config.setting import Config

class BlogPostRepository:
    def __init__(self):
        # Correct way to check if Firebase has been initialized
        if not firebase_admin._DEFAULT_APP_NAME in firebase_admin._apps:
            cred = credentials.Certificate(Config.FIREBASE_KEY_PATH)
            initialize_app(cred)
        self.db = firestore.client()
        self.collection = self.db.collection('posts')

    def initialize_collection(self):
        """Initialize the collection with default data if empty."""

        # Check if the 'posts' collection is empty
        if not self.collection.document().get().exists:

            # Get the default post structure from our schema
            default_post = BlogPostSchema.get_default_post()

            # Add the default post to the 'posts' collection
            self.collection.add(default_post)

    def add_post(self, post):
        """Add a new post to the 'posts' collection and return it with its ID."""

        # Add the post (as a dictionary) to the 'posts' collection
        new_post_ref = self.collection.add(post.__dict__)

        # Assign the generated Firestore ID to the post object
        post.post_id = new_post_ref[1].id

        # Return the post object with its ID
        return post

    def get_post(self, post_id):
        """Retrieve a post from the 'posts' collection using its ID."""

        # Fetch the document with the given ID from the 'posts' collection
        doc = self.collection.document(post_id).get()
        # If the document exists, convert it to a BlogPost object and return it
        if doc.exists:
            return BlogPost(**doc.to_dict())

        # If the document doesn't exist, return None
        return None

    def getAll(self):
        docs = self.collection.stream()
        posts = []

        for doc in docs:
            post_data = doc.to_dict()
            post = BlogPost(
                title=post_data['title'],
                content=post_data['content'],
                post_id=doc.id
            )
            posts.append(post)
        return posts

    def update_post(self, post_id, updated_data):
        """ Update a post with the given post_id in the 'posts' collection. """
        return self.collection.document(post_id).update(updated_data)

    def delete_post(self, post_id):
        """ Delete a post with the given post_id from the 'posts' collection. """
        return self.collection.document(post_id).delete()

