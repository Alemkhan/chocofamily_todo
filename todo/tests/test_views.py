from django.urls import reverse
from django.contrib.auth import get_user_model
from authentication.tests.conftest import create_test_user, user_data

import pytest


@pytest.mark.django_db
def test_todo_task_create(client, create_test_user, user_data, task_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    url = reverse('login')
    response = client.post(url, user_data)
    assert response.status_code == 200
    assert response.data['access'] is not None
    url = reverse('task_create')
    headers = {
        f"Authorization': 'JWT {response.data['access']}"
    }
    response = client.post(url, task_data)
    assert response.status_code == 201


