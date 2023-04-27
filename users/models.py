from django.db import models

# Create your models here.
class UserData(models.Model):
    email = models.EmailField(max_length=254, unique=True, verbose_name="이메일")
    password = models.CharField(max_length=50, verbose_name="비밀번호")
    name = models.CharField(max_length=50, verbose_name="이름")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="성별")
    age = age = models.PositiveIntegerField(verbose_name="나이")
    introduction = models.TextField(verbose_name="자기소개")

