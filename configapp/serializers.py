from rest_framework import serializers
from .models.user_auth import User
from .models.teacher import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "name", "surname"]

class UserTeacherSerializer(serializers.ModelSerializer):
    teacher_profile = TeacherSerializer(required=False)

    class Meta:
        model = User
        fields = ["id", "phone", "email", "is_teacher", "teacher_profile"]
        extra_kwargs = {
            "is_teacher": {"default": True}
        }

    def create(self, validated_data):
        teacher_data = validated_data.pop("teacher_profile", None)
        user = User.objects.create(**validated_data)

        if teacher_data:
            Teacher.objects.create(user=user, **teacher_data)

        return user

    def update(self, instance, validated_data):
        teacher_data = validated_data.pop("teacher_profile", None)

        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.is_teacher = validated_data.get("is_teacher", instance.is_teacher)
        instance.save()

        if teacher_data:
            teacher, created = Teacher.objects.get_or_create(user=instance)
            teacher.name = teacher_data.get("name", teacher.name)
            teacher.surname = teacher_data.get("surname", teacher.surname)
            teacher.save()

        return instance
