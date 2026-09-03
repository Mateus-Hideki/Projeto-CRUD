"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve

from core.admin_site import admin_site
from core.views import react_frontend

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('core.urls')),
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR.parent / 'frontend' / 'dist' / 'assets'}),
    re_path(r'^favicon\.svg$', serve, {'document_root': settings.BASE_DIR.parent / 'frontend' / 'dist'}),
    re_path(r'^icons\.svg$', serve, {'document_root': settings.BASE_DIR.parent / 'frontend' / 'dist'}),
    re_path(r'^(?!admin/|roupas/|modelos/|categorias/).*$', react_frontend),
]