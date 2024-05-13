from django.urls import path
from . import views

app_name="posts"
urlpatterns = [ 
    path('',views.post_list,name='list'),
    path('new_post/',views.new_post,name='new_post'),
    path('user_post/',views.user_post,name='user_post'),
    path('<slug:slug>',views.post_page,name='post_page'),
    path('new_comment/',views.new_comment,name='new_comment'),
]