import base64, json
from django.contrib.auth import login
from django.contrib.auth.models import User
def get_azure_ad_user(request):
    encoded = request.headers.get("X-MS-CLIENT-PRINCIPAL")
    if not encoded:
        return None
    decoded = base64.b64decode(encoded).decode("utf-8")
    return json.loads(decoded)
class AzureADAutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        principal = get_azure_ad_user(request)
        if principal and not request.user.is_authenticated:
            email = principal.get("userDetails")
            if email:
                user, _ = User.objects.get_or_create(
                    email=email,
                    defaults={"username": email.split("@")[0], "is_staff": True}
                )
                login(request, user)
        return self.get_response(request)
