from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskDetailView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create', TaskCreateView.as_view(), name='task_create'),
    path('detail/<int:pk>', TaskDetailView.as_view(), name='task_detail')
]
