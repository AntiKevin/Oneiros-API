from django.urls import path
from .api import api

urlpatterns = [
    path('difussion/', api.urls),
]
