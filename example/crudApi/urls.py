from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crudApi.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'persons', PersonViewSet, basename='persons')
app_name = 'crudApi'
urlpatterns = [
    path('', include(router.urls))
]
