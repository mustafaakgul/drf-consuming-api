"""consume_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from core import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.users, name='users'),
    path('todos/', views.todos, name='todos'),
    path('embed', views.save_embed, name='embed'),
    path('api/cart-items/', views.CartItemViews.as_view()),
    path('apicart-items/<int:id>', views.CartItemViews.as_view()),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #re_path(r'api/(?P<version>[v1|v2]+)/', include('django_blog.apps.blog.rest_api.urls')),
    #re_path(r'api/(?P<version>[v1|v2]+)/', ),

    path('decimal-test/<int:id>', views.decimal_test, name='decimal_test'),
    path('weather/', weather.views.weather, name='weather'),
]
