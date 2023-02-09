from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('arts/', views.arts_index, name='index'),
    path('arts/<int:art_id>/', views.arts_detail, name='detail'),
]