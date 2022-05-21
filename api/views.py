from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .models import Plant, Conditions, UserSettings
from api import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CreateUserSerializer
        return serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class PlantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows plants to be viewed or edited.
    """
    queryset = Plant.objects.all()
    serializer_class = serializers.PlantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ConditionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conditions to be viewed or edited.
    """
    queryset = Conditions.objects.all()
    serializer_class = serializers.ConditionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(plant__user=self.request.user)


class UserSettingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user settings to be viewed or edited.
    """
    queryset = UserSettings.objects.all()
    serializer_class = serializers.UserSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
