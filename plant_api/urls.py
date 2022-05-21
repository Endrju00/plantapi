from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'user-settings', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'plants', api_views.PlantViewSet)
router.register(r'conditions', api_views.ConditionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
]
