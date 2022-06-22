from django.urls import path
from django.urls.conf import include

from price_app import user_views
from price_app.user_views import Add_comment,View_comment, Add_Wish_List, View_Wish_List, Remove,statistics,laptop_statistics

urlpatterns = [
    path('', user_views.IndexView, name="IndexView"),
    path('result', user_views.result, name="result"),
    path('add_comments',Add_comment.as_view()),
    path('view_comment',View_comment.as_view()),
    path('add_wish',Add_Wish_List.as_view()),
    path('view_wish',View_Wish_List.as_view()),
    path('remove',Remove.as_view()),
    path('statistics',statistics.as_view()),
    path('laptop_statistics',laptop_statistics.as_view())
    # path('wish_list',user_views.wish_list, name= "wish_list"),
    # path('add_wish_list',user_views.Add_Wish_list, name="Add_Wish_list"),
]

def urls():
    return urlpatterns, 'user', 'user'
