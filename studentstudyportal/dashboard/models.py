from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Заголовок урока')
    description = models.TextField(verbose_name='Описание урока')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Записи'
        verbose_name_plural = 'Записи'


class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, verbose_name='Предмет')
    title = models.CharField(max_length=80, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание урока')
    time_lesson = models.DateTimeField(verbose_name='Время на выполнение')
    is_finished = models.BooleanField(default=False, verbose_name='Выполнено')

    def __str__(self):
        return self.title
