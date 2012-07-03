from django.db import models

class News(models.Model):
    creator = models.ForeignKey('users.User', verbose_name = "person who created the news", related_name = "news_created")
    modifier = models.ForeignKey('users.User', verbose_name = "person who last modified the news", related_name = "news_modified")

    published_date = models.DateTimeField('date published')
    heading = models.CharField('heading for the news', max_length = 100)
    summary = models.TextField('summary of the news')
    body = models.TextField('body of the news')

    views = models.IntegerField('number of views of the news')