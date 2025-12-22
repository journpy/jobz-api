"""
URL configuration for jobz_api project.
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView
)
from django.views.generic import TemplateView
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    #  add REST framework's login and logout views for the browsable api. 
    path('api-auth/', include('rest_framework.urls')),
    # allauth urls
    path('users/', include('allauth.urls')),
    # expose dj-rest-auth endpoints
    path('rest-auth/', include('dj_rest_auth.urls')),
    path(
        'rest-auth/registration/account-confirm-email/<str:key>/', 
        ConfirmEmailView.as_view(), 
        name='account-confirm-email'
        ), # Needs to be defined before the registration path
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path(
        'api/v1/dj-rest-auth/account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    path('api/v1/', include('api.users.urls')),
    path('api/v1/', include('api.jobs.urls')),
    # drf spectacular endpoints
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # home page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # simple jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
