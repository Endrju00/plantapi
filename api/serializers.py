from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Plant, Conditions, UserSettings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user


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
