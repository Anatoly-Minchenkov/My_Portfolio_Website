from django.contrib import admin
from .models import FeedBack
# Register your models here.


@admin.register(FeedBack)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'feedback', 'date']