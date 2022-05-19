from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Plant, Conditions, UserSettings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        fields = [
            "water_amount",
            "insolation",
            "humidity",
            "world_direction",
            "watering_period",
            "watering_amount",
            "additional_remarks",
            "url",
        ]


class PlantSerializer(serializers.ModelSerializer):
    conditions = ConditionsSerializer()

    class Meta:
        model = Plant
        fields = ["user", "name", "conditions", "image_path"]


class UserSettingsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserSettings
        fields = ["user", "send_notifications", "send_emails"]
