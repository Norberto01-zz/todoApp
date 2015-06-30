from django.contrib import admin
from .models import Tasking

class TaskAdmin(admin.ModelAdmin):
    fields = ('taskName', 'done', 'owner')


admin.site.register(Tasking, TaskAdmin)