import requests
import random
import io
from PIL import Image
from utils.huggingface_api import get_ai_image
from ninja import NinjaAPI, Schema
from django.http import FileResponse
from django.http.response import HttpResponse

from django.http import StreamingHttpResponse
import spotipy

api = NinjaAPI(
   title="Difussion API",
   urls_namespace='difussion',
   description="Essa api é dedicada para todos os endpoints de criação de imagens com dados",
)

@api.get("/create_spotiphoto")
def create_spotiphoto(request):
    auth_header = request.headers.get("Authorization")
    token = auth_header[7:]
    sp = spotipy.Spotify(auth=token)
    # extracting artists
    top_artist_json = sp.current_user_top_artists(limit=10, offset=5)['items']
    top_artists = [artist['name'] for artist in top_artist_json]
    random_artists = random.sample(top_artists, 3)
    #AI pipeline
    image_bytes = get_ai_image(f'a character who listens to {random_artists[0]}')
    
    image = Image.open(io.BytesIO(image_bytes))
    # Crie um buffer de memória para armazenar a imagem
    buffer = io.BytesIO()
    
    # Salve a imagem no buffer
    image.save(buffer, format="PNG")
    
    # Mova o cursor do buffer para o início
    buffer.seek(0)
    
    # Crie uma resposta de streaming a partir do buffer
    response = StreamingHttpResponse(buffer, content_type="image/png")
    
    # Defina o cabeçalho Content-Disposition para fazer o navegador baixar a imagem em vez de exibi-la
    response["Content-Disposition"] = "attachment; filename=imagem.png"
    
    return response