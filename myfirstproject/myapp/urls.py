from django.urls import path
from .views import TodoGetCreate,TodoUpdateDellet

urlpatterns = [
    path('',TodoGetCreate.as_view()),
    path('<int:pk>',TodoUpdateDellet._as_view)
]
