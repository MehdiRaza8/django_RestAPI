from django.urls import path, include
from django.conf.urls import url
from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
]
