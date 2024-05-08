from django.contrib import admin
from .models import Questions, Quizz
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(Questions)
admin.site.register(Quizz)