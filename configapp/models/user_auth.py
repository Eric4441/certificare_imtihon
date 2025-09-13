# from django.db import models
# from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
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
# class User(AbstractBaseUser,PermissionsMixin):
#     phone=models.CharField(max_length=13)
#     email=models.EmailField(unique=True,null=True,blank=True)
#     is_active=models.BooleanField(default=True)
#     is_admin=models.BooleanField(default=False)
#     is_teacher=models.BooleanField(default=False)
#     is_student=models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.phone
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#
#     @property
#     def is_superuser(self):
#         return self.is_admin
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("Telefon raqam kiritilishi shart")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser is_admin=True bo‘lishi kerak!")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser is_staff=True bo‘lishi kerak!")

        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    @property
    def is_superuser(self):
        return self.is_admin
