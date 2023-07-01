from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.crud_peliculas, name='crud_peliculas'),
    path('favoritas/', views.favoritas, name='favoritas'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)