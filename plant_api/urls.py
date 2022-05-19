from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user-settings', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'plants', views.PlantViewSet)
router.register(r'conditions', views.ConditionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
