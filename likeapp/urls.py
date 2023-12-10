from django.urls import path
from likeapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('read/', views.read, name = 'read'),
    path('mybookmark/', views.mybookmark, name='mybookmark'),
    path('detail/<str:id>/', views.detail, name = 'detail'),  
    path('update/<str:id>/', views.update, name='update'),
    path('delete/<str:id>/', views.delete, name = 'delete'),

    path('<int:id>/like/', views.like, name='like'),
    path('<int:id>/bookmark/', views.bookmark, name='bookmark'),
]