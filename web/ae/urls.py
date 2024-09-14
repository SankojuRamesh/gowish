"""
URL configuration for ae project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter
# from canvasmanager import views
from accountmanager import views as user_views


schema_view = get_schema_view(
   openapi.Info(
      title="AfterEffect Atuomation API",
      default_version='v1',
      description="AFTEREFFECT Canvas ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
# router.register(r'projects', views.ProjectViewSet, basename='projects')
# router.register(r'composits', views.CompositViewSet, basename='composits')
# router.register(r'layers', views.LayerViewSet, basename='LayerViewSet')
# router.register(r'deeplayers', views.DeepLayerViewSet, basename='DeepLayerViewSet')




urlpatterns = [
    # path('',  views.home),
    path('admin/', admin.site.urls),
     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('sign-in/', user_views.SignInView.as_view(), name='sign_in'),
]+router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)