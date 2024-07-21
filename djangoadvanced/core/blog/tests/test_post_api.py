import pytest
from rest_framework.test import APIClient
from datetime import datetime
from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="james@gmail.com", password="aaaadsfwerof;e4wig"
    )


@pytest.mark.django_db
class TestPostapi:
    def test_tegpostresponse200(self, api_client):
        response = api_client.get("http://localhost:8000/blog/api/v1/post/")

        assert response.status_code == 200

    # def test_create_post_401(self,api_client,common_user):

    #     data={"title":'test',"content":"aaaaaaaaaaa","status":True,
    #         #   "category":None,
    #           "published_date":datetime.now()}
    #     response=api_client.post('http://localhost:8000/blog/api/v1/post/',data)
    #     assert response.status_code == 401

    # def test_create_post_201(self,api_client,common_user):

    #     data={"title":'test',"content":"aaaaaaaaaaa","status":True,
    #         #   "category":None,
    #           "published_date":datetime.now()}
    #     api_client.force_login(user=common_user)
    #     response=api_client.post('http://localhost:8000/blog/api/v1/post/',data)
    #     assert response.status_code == 201
