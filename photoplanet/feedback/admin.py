from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']

admin.site.register(Feedback, FeedbackAdmin)