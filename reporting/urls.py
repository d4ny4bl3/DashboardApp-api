from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reporting import views


router = DefaultRouter()
router.register("orders", views.OrderViewSet, basename="orders")

urlpatterns = [
    path("reporting/", views.ReportingViewSet.as_view(), name="reporting"),
    path("", include(router.urls)),
]
