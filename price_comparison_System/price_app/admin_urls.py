
from django.urls import path
from django.urls.conf import include

from price_app import admin_views
from price_app.admin_views import View_Comment, User_Approve, ApproveView, RejectView, Approve_User_View

urlpatterns = [
    path('', admin_views.IndexView, name="IndexView"),
    path('cpmment',View_Comment.as_view()),
    path('user_approve',User_Approve.as_view()),
    path('approve',ApproveView.as_view()),
    path('remove',RejectView.as_view()),
    path('user_view',Approve_User_View.as_view())


]
