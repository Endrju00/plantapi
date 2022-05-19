from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conditions = models.OneToOneField('Conditions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # image = models.ImageField()

    def __str__(self):
        return f"{self.user}'s {self.name}"

    class Meta:
        ordering = ["name", "id"]


class Conditions(models.Model):
    INSOLATION_CHOICES = [
        ("Sunny places", "Sunny places"),
        ("Shady places", "Shady places")
    ]

    HUMIDITY_CHOICES = [
        ("Dry places", "Dry places"),
        ("Wet places", "Wet places")
    ]

    WORLD_DIRECTIONS = [
        ("North", "North"),
        ("East", "East"),
        ("West", "West"),
        ("South", "South")
    ]

    water_amount = models.PositiveIntegerField(default=100)
    insolation = models.CharField(max_length=100, choices=INSOLATION_CHOICES)
    humidity = models.CharField(max_length=100, choices=HUMIDITY_CHOICES)
    world_direction = models.CharField(max_length=100, choices=WORLD_DIRECTIONS)
    watering_period = models.PositiveIntegerField(default=1)
    watering_amount = models.PositiveIntegerField(default=1)
    additional_remarks = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Conditions"
        ordering = ["id"]


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    send_notifications = models.BooleanField(default=True)
    send_emails = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "User settings"
        ordering = ["id"]
