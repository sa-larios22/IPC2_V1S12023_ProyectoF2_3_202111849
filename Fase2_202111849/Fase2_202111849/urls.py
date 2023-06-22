"""
URL configuration for Fase2_202111849 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from Usuarios.views import mostrar_user
from Usuarios.views import cargar_xml
from Usuarios.views import agregar_usuario

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('Usuarios/', mostrar_user, name='mostrar_user'),
    path('Usuarios/cargar_xml', cargar_xml, name='cargar_xml'),
    path('Usuarios/agregar_usuario', agregar_usuario, name='agregar_usuario'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)