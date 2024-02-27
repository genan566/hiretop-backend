
app_name = "employments"


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("", views.EmploymentsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
