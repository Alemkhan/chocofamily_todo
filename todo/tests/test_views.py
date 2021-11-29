from django.urls import reverse
from django.contrib.auth import get_user_model
from authentication.tests.conftest import create_test_user, user_data

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_todo_task_create(client, create_test_user, user_data, task_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1

    url = reverse('login')
    response = client.post(url, user_data)
    assert response.status_code == 200
    assert response.data['access'] is not None

    url = reverse('task_create')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])
    response = client.post(url, task_data, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_todo_task_get(client, create_test_user, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1

    url = reverse('login')
    response = client.post(url, user_data)
    assert response.status_code == 200
    assert response.data['access'] is not None

    token = response.data['access']

    url = reverse('task_list')
    client = APIClient()
    response = client.get(url, format='json')
    assert response.status_code == 401

    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    response = client.get(url, format='json')
    assert response.status_code == 200


