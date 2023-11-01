from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from basket.petition.views import sign_petition, signatures_json

urlpatterns = (
    path("sign/", csrf_exempt(sign_petition), name="sign-petition"),
    path("signatures.json", signatures_json, name="signatures-json"),
)
