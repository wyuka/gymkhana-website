from news.models import News
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'published_date', 'creator', 'modifier')

admin.site.register(News, NewsAdmin)
