from django.contrib import admin
from .models import Feedback, Issues

# Register your models here.
admin.site.register(Issues, admin.ModelAdmin)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('issue', 'email', 'message', 'read',)
    search_fields = ['issue', 'email', 'message']
    list_filter = ('issue', 'email', 'read')
