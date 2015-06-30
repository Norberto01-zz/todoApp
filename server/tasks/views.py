from .models import Tasking
from .serializers import TodoSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Tasking.objects.all()
    serializer_class = TodoSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

