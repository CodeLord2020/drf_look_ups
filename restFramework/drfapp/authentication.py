from rest_framework.authentication import TokenAuthentication as Base
from rest_framework.authentication import SessionAuthentication as base1
from rest_framework.authtoken.models import Token

class TokenAuthentication(Base):
    keyword= 'Bearer'

class SessionAuthentication(base1):
    keyword= 'Bearer'

# class SecretAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         app_key = request.META.get('APP_KEY')
#         app_secret = request.META.get('APP_SECRET')
#         username = request.META.get('X_USERNAME')
#         try:
#             app = ClientApp.objects.match_secret(app_key, app_secret)
#         except ClientApp.DoesNotExist:
#             raise AuthenticationFailed('App secret and key does not match')
#         try:
#             user = app.users.get(username=username)
#         except User.DoesNotExist:
#             raise AuthenticationFailed('Username not found, for the specified app')
#         return (user, None)
