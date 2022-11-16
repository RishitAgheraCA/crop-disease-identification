from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from inference import views

urlpatterns = [
    path('', views.home_page, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)