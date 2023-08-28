import json
import pytest
from use_cases import BlogUseCases
from entities import BlogPost
from unittest.mock import Mock, call

@pytest.fixture
def mocked_repository():
    return Mock()

@pytest.fixture
def blog_use_case(mocked_repository):
    return BlogUseCases(mocked_repository)

def test_create_post(blog_use_case, mocked_repository):
    # Setup
    expected_post = BlogPost(title="Test", content="Test content")
    mocked_repository.add_post.return_value = expected_post

    # Execute
    created_post = blog_use_case.create_post(title="Test", content="Test content")

    # Assert repository interaction
    called_post = mocked_repository.add_post.call_args[0][0]  # Extract the BlogPost instance
    assert isinstance(called_post, BlogPost)
    assert called_post == expected_post

    # Assert returned result
    assert created_post == expected_post

def test_get_post(blog_use_case, mocked_repository):
    # Given a post ID and a corresponding mocked post in the repository
    post_id = 1
    mock_post = BlogPost(title="Test", content="Test content", post_id=post_id)
    mocked_repository.get_post.return_value = mock_post

    # When the get_post method is called
    result = blog_use_case.get_post(post_id)

    # Then the repository's get_post method should have been called with the correct ID
    mocked_repository.get_post.assert_called_once_with(post_id)

    # And the returned post should match the mock post
    assert result == mock_post

def test_get_all_posts(blog_use_case, mocked_repository):

    # Setup: Create a list of expected posts
    expected_posts = [
        BlogPost(title="Test1", content="Test content1", post_id=1),
        BlogPost(title="Test2", content="Test content2", post_id=2),
    ]
    mocked_repository.getAll.return_value = expected_posts

    # Action: Call the method to get all posts
    result_posts = blog_use_case.getAll()

    # Assertion: The repository's method was called and the returned posts match the expected posts
    mocked_repository.getAll.assert_called_once()
    assert result_posts == expected_posts


def test_update_post(blog_use_case, mocked_repository):
    # Setup
    post_id = 1
    update_data = {'title': 'Updated Title', 'content': 'Updated Content'}

    updated_post = BlogPost(title=update_data['title'], content=update_data['content'], post_id=post_id)
    mocked_repository.update_post.return_value = updated_post

    # Execute
    result = blog_use_case.update_post(post_id, update_data)

    # Assert repository interaction
    mocked_repository.update_post.assert_called_once_with(post_id, update_data)

    # Assert returned result
    assert result == updated_post

def test_delete_post(blog_use_case, mocked_repository):
    # Setup
    post_id = 1

    # Execute
    blog_use_case.delete_post(post_id)

    # Assert repository interaction
    mocked_repository.delete_post.assert_called_once_with(post_id)
