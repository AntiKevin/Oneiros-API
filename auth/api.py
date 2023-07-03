import os
from ninja import NinjaAPI
from django.http import HttpResponseRedirect
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path=env_path)

api = NinjaAPI(
   title="Auth API",
   description="Essa api é dedicada para todos os endpoints de autorização e autenticação"
)


@api.get("/login")
def spotify_login(request):
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return HttpResponseRedirect(auth_url)

@api.get("/redirect")
def redirect(request, code: str = None):
    sp_oauth = create_spotify_oauth()
    request.session.clear()
    token_info = sp_oauth.get_access_token(code)
    request.session['token'] = token_info
    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_SECRET'),
            redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
            scope=os.getenv('SPOTIFY_SCOPE'))