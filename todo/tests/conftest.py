import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def task_data():
    return {
        "title": "Dog",
        "description": "Go walk with my dog",
        "deadline": "2021-11-27T12:51:30.000"
    }
