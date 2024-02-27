
app_name = "submitemployment"

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("", views.SubmitEmploymentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
