from django.urls import path
from likeapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('read/', views.read, name = 'read'),
    path('detail/<str:id>/', views.detail, name = 'detail'),  
    path('update/<str:id>/', views.update, name='update'),
    path('delete/<str:id>/', views.delete, name = 'delete'),
    path('like/<int:id>', views.like, name='like'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('mybookmark/', views.mybookmark, name='mybookmark'),
    path('bookmark/<int:id>/', views.bookmark, name='bookmark'),
]