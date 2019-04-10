from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp']
    search_fields = ['title', 'content']

    class Meta:
        model = models.Post


admin.site.register(models.Post, PostAdmin)
