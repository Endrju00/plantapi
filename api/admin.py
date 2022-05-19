from django.contrib import admin
from .models import Plant, Conditions, UserSettings


# Register your models here.
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user")


@admin.register(Conditions)
class ConditionsAdmin(admin.ModelAdmin):
    list_display = ("id", "plant")


@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "send_notifications", "send_emails")
