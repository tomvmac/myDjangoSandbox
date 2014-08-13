from django.shortcuts import render

# Create your views here.
# models
from django.contrib.auth.models import User, Group
from models import Car

from rest_framework import viewsets

# serializers
from quickstart.serializers import UserSerializer, GroupSerializer, CarSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cars to be viewed or edited.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer   