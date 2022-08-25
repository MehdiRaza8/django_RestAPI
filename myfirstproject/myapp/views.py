from rest_framework import serializers
from .models import Todo
from .serializers import Todoserializers
from rest_framework import generics



class TodoGetCreate(generics.ListCreateAPIView):
     queryset = Todo.objects.all()
     serializer_class = Todoserializers

class TodoUpdateDellet(generics.RetrieveUpdateDestroyAPIView):
     queryset = Todo.objects.all()
     serializer_class = Todoserializers





