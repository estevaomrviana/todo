from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='titulo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='criado por')

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='titulo')
    completed = models.BooleanField(default=False, verbose_name='compelto?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='criado por')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='projeto', null=True)

    def __str__(self):
        return self.title
