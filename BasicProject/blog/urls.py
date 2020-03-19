from django.urls import path
from . import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
