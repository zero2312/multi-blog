from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),

    # Посты
    path('post/create', views.create, name='post-create'),
    path('post/detail/<int:id>', views.detail, name='detail'),
    path('post/<int:id>/edit', views.edit, name='post-edit'),
    path('post/<int:id>/delete', views.post_delete, name='post-delete'),

    # Комментарии
    path('comment/<int:id>/edit', views.comment_edit, name='edit-comment'),
    path('comment/<int:id>/delete', views.comment_delete, name='delete-comment'),

]
