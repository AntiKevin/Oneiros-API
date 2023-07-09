import os
from utils.spotify_auth import create_spotify_oauth
from django.http import JsonResponse
from ninja import NinjaAPI, Schema

api = NinjaAPI(
   title="Difussion API",
   urls_namespace='difussion',
   description="Essa api é dedicada para todos os endpoints de criação de imagens com dados",
)