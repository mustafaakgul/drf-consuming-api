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
from weather import views as weather_
from infura import views as infura_

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('decimal-test/<int:id>', views.decimal_test, name='decimal-test'),
    path('weather/', weather_.weather, name='weather'),
    path('infura-initial/', infura_.infura_initial, name='infura-initial'),
    path('github/', views.index_github, name='index_github'),
    path('github-library/', views.index_github_library, name='index_github_library'),
]
