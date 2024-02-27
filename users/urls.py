from django.urls import path

from rest_framework.routers import DefaultRouter
from . import views

app_name = "user"
urlpatterns = [
    path("list/", views.ManageUserListView.as_view(), name="list"),
    path("retrieve/<int:id>", views.RetrieveUserView.as_view(), name="retrieve"),
    path("retrieve/upload-image/", views.ManageUserRetriveUpdateView.as_view(), name="retrieve-upload-image"),
    path("retrieve/upload-image-auth/<int:id>", views.ManageUserRetriveUpdateAuthView.as_view(), name="retrieve-upload-image-auth"),
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("token/", views.CreateTokenView.as_view(), name="token"),
    path("mee/", views.ManageUserView.as_view(), name="mee"),
]
