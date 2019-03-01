from django.urls import path

from . import views
app_name = 'man'
urlpatterns = [
    path('', views.logi, name='logi'),
    path('<int:mservice_id>/', views.man_sender, name='man_sender'),
    path('<int:otpr_id>/detail/', views.detail, name='detail'),
    path('<int:otpr_id>/barr/', views.barr, name='barr'),
    path('<int:otpr_id>/fill/', views.fill, name='fill'),
    path('<int:otpr_id>/htm/', views.htm, name='htm'),
]

