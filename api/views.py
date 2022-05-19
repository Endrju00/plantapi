from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .models import Plant, Conditions, UserSettings
from .serializers import (
    UserSerializer,
    GroupSerializer,
    PlantSerializer,
    ConditionsSerializer,
    UserSettingsSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows plants to be viewed or edited.
    """
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ConditionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conditions to be viewed or edited.
    """
    queryset = Conditions.objects.all()
    serializer_class = ConditionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(plant__user=self.request.user)


class UserSettingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user settings to be viewed or edited.
    """
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
