from django.urls import path, include
from django.http import JsonResponse, HttpResponse
from .views import get_matrixes, get_matrixes_with_auth

from .views import TokenView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('results/', get_matrixes),
    path('auth/results/', get_matrixes_with_auth),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/token/results/', TokenView.as_view()),
]
