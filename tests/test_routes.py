import pytest
from main import app
import json
from entities import BlogPost
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_all_posts(client):
    response = client.get("/posts")
    
    assert response.status_code == 200
    assert b"Uleana" in response.data

def test_create_post(client):
    post_data = {
        "title": "Test Post",
        "content": "Test Content"
    }
    response = client.post("/posts", data=json.dumps(post_data), content_type='application/json')
    assert response.status_code == 201

    response_data = json.loads(response.data)
    assert response_data["title"] == post_data["title"]
    assert response_data["content"] == post_data["content"]

def test_get_single_post_not_found(client):
    response = client.get("/posts/9999")

    assert response.status_code == 404
    assert b"Post not found" in response.data