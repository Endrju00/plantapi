from django.contrib import admin
from .models import Plant, Conditions, UserSettings

# Register your models here.
admin.site.register(Plant)
admin.site.register(Conditions)
admin.site.register(UserSettings)
