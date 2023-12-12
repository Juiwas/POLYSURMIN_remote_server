from django.contrib import admin
from .models import SwanTask, SwanSubTask
# Register your models here.



class SwanTaskAdmin(admin.ModelAdmin):
    list_display = ["pk", "hash", "timestamp"]

class SwanSubTaskAdmin(admin.ModelAdmin):
    list_display = ["pk", "vel", "dir", "swan_task"]

admin.site.register(SwanTask, SwanTaskAdmin)

admin.site.register(SwanSubTask, SwanSubTaskAdmin)
