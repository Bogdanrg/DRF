"""Django_rest_site URL Configuration

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
from rest_framework.routers import Route, DynamicRoute
from rest_framework_simplejwt.views import *

from news.views import *
from rest_framework import routers


#class MyCustomRouter(routers.SimpleRouter):
 #   routes = [
#        Route(
 #           url=r'^{prefix}$',
 #           mapping={'get': 'list'},
 #           name='{basename}-list',
 #           detail=False,
 #           initkwargs={'suffix': 'List'}
 #       ),
 #       Route(
 #           url=r'^{prefix}/{lookup}$',
 #           mapping={'get': 'retrieve'},
 #           name='{basename}-detail',
# #           detail=True,
 #           initkwargs={'suffix': 'Detail'}
#        ),
 #       DynamicRoute(
#            url=r'^cats/{url_path}/$',
#            name='{basename}-{url_name}',
#            detail=False,
#            initkwargs={}
#        )
#    ]


#router = MyCustomRouter()
#router.register(r'news', NewsViewSet, basename='news')
#print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/newslist/', NewsAPIList.as_view()),
    path('api/v1/newslist/<int:new_pk>/', NewUpdateApiView.as_view()),
    path('api/v1/deletenew/<int:new_pk>/', NewDeleteAPIView.as_view()),
    path('api/v1/auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

