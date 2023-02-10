from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('arts/', views.arts_index, name='index'),
    path('arts/<int:art_id>/', views.arts_detail, name='detail'),
    path('arts/create/', views.ArtCreate.as_view(), name='art_create'),
    path('arts/<int:pk>/update/', views.ArtUpdate.as_view(), name='arts_update'),
    path('arts/<int:pk>/delete/', views.ArtDelete.as_view(), name='arts_delete'),
    path('arts/<int:art_id>/add_maintaining/', views.add_maintaining, name='add_maintaining'),
    path('frames/', views.FrameList.as_view(), name='frames_index'),
    path('frames/<int:pk>/', views.FrameDetail.as_view(), name='frames_detail'),
    path('frames/create/', views.FrameCreate.as_view(), name='frames_create'),
    path('frames/<int:pk>/update/', views.FrameUpdate.as_view(), name='frames_update'),
    path('frames/<int:pk>/delete/', views.FrameDelete.as_view(), name='frames_delete'),
    path('arts/<int:art_id>/assoc_frame/<int:frame_id>/', views.assoc_frame, name='assoc_frame'),
    path('arts/<int:art_id>/unassoc_frame/<int:frame_id>/', views.unassoc_frame, name='unassoc_frame'),
    ]