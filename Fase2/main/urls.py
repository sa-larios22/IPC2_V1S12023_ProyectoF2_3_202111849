from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('administrador/', views.administrador, name='administrador'),
    path('cliente/', views.cliente, name='cliente')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)