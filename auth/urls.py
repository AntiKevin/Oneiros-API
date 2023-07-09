from django.urls import path
from .api import api

urlpatterns = [
    path('auth/', api.urls),
]
