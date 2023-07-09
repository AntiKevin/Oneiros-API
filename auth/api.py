from django.http import JsonResponse
from schemas.request_schemas import *
from schemas.response_schemas import *
from ninja import NinjaAPI
from utils.spotify_auth import create_spotify_oauth

api = NinjaAPI(
   title="Auth API",
   urls_namespace='auth',
   description="Essa api é dedicada para todos os endpoints de autorização e autenticação",
)

@api.get("/get-url-login")
def spotify_login(request):
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return {"url":auth_url}


      
@api.post("/token")
async def getToken(request, requestBody: TokenSchema):
    try:
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.get_access_token(requestBody.code)
        return token_info
    except Exception as e:
        # Erros de validação, retorne um erro 400
        return JsonResponse({"detail": str(e), "code":requestBody.code}, status=400)