from django.db import models

class Tasking(models.Model):
    taskName = models.CharField(max_length=30, verbose_name='Task')
    done = models.BooleanField(default=False, verbose_name='Hecho?')
    owner = models.ForeignKey('auth.User', related_name='tasks')