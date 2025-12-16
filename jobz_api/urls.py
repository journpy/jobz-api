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


urlpatterns = [
    path('admin/', admin.site.urls),
    #  add REST framework's login and logout views for the browsable api. 
    path('api-auth/', include('rest_framework.urls')),
    # allauth urls
    path('users/', include('allauth.urls')),
    # expose dj-rest-auth endpoints
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/', include('api.users.urls')),
    # drf spectacular endpoints
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # home page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
