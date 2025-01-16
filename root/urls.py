# """
# URL configuration for PyTestFull project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.conf.urls.i18n import i18n_patterns
# from django.contrib import admin
# from django.urls import path, include
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
# from graphene_django.views import GraphQLView
#
# urlpatterns = i18n_patterns(
#     path('admin/', admin.site.urls),
#     # path('api/v1/apps/', include('apps.urls')),
#     # path('api/v1/apps/schema/', SpectacularAPIView.as_view(), name='apps-schema'),
#     # path('api/v1/apps/swagger/', SpectacularSwaggerView.as_view(url_name='apps-schema'), name='apps-swagger-ui'),
#     path("graphql", GraphQLView.as_view(graphiql=True)),
# )

from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

from apps.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.urls")),
]
