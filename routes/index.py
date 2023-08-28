from controllers import BlogPostController
from presenters import BlogPostPresenter
from repositories import BlogPostRepository
from use_cases import BlogUseCases


blog_repository = BlogPostRepository()
blog_use_cases = BlogUseCases(blog_repository)
blog_presenter = BlogPostPresenter()

def config_routes(api):
    api.add_resource(BlogPostController, '/posts', '/posts/<string:post_id>', resource_class_args=[blog_use_cases, blog_presenter])
