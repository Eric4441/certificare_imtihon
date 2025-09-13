from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from configapp.views.user_teacher_views import UserTeacherViewSet

router = DefaultRouter()
router.register("teachers", UserTeacherViewSet, basename="teacher-user")
urlpatterns = [
    path("", include(router.urls)),

]
