from rest_framework import viewsets
from configapp.models.user_auth import User
from configapp.serializers import UserTeacherSerializer

class UserTeacherViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_teacher=True)
    serializer_class = UserTeacherSerializer