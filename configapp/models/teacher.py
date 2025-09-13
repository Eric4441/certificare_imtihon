# from django.db import models
# from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
#
#
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self,username,password=None, **extra_fields):
#         if not username:
#             raise ValueError('Username kiritilishi shart')
#         user=self.model(username=username,**extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self,username,password,**extrafields):
#         extrafields.setdefault('is_admin',True)
#         extrafields.setdefault('is_staff',True)
#
#         if extrafields.get('is_admin') is not True:
#             raise ValueError('Superuser is_admin=True bolishi kerak!')
#
#         if extrafields.get('is_staff') is not True:
#             raise ValueError('Superuser is_staff=True bolishi kerak!')
#         return self.create_user(username,password,**extrafields)
#
# class Teacher(AbstractBaseUser, PermissionsMixin):
#     name = models.CharField(max_length=20)
#     surname = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#
#     @property
#     def is_superuser(self):
#         return self.is_admin
from django.db import models
from .user_auth import User  # User modelini import qilamiz

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.surname}"
