from django.urls import path


from . import views


urlpatterns = [
    path('', views.index, name="index" ),
    path('user_register', views.user_register, name="user_register"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logut', views.user_logut, name="user_logut"),
    path('dashboard', views.dashboard, name="dashboard"), 
    path('create_post', views.create_post, name='create_post'),
    path('update_post/<str:pk>/', views.update_post, name='update_post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete_post'),
    path('likes/<int:pk>/', views.likes, name='likes'),
    path('comment_post/<int:pk>/', views.comment_post, name='comment_post'),
]
