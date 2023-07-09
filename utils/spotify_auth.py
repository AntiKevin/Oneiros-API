import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path=env_path)


def create_spotify_oauth():
    return SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_SECRET'),
            redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
            scope=os.getenv('SPOTIFY_SCOPE'))