from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=15)
    reg_no = models.CharField(max_length=30)

    USER_TYPE_CHOICES = (
        (u'u', u'User'),
        (u'm', u'Manager'),
        (u'a', u'Administator'),
    )
    privilege = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)

    DEPARTMENT_CHOICES = (
        (u'BT', u'Biotechnology'),
        (u'CE', u'Civil Engineering'),
        (u'CHE', u'Chemical Engineering'),
        (u'CSE', u'Computer Science and Engineering'),
        (u'ECE', u'Electronics and Communications Engineering'),
        (u'EE', u'Electrical Engineering'),
        (u'IT', u'Information Technology'),
        (u'ME', u'Mechanical Engineering'),
        (u'MME', u'Mettalurical and Materials Engineering'),
    )
    department = models.CharField(max_length=5, choices=DEPARTMENT_CHOICES)

    pinned_news = models.ManyToManyField('news.News', verbose_name = "news that the user has pinned to his profile", related_name = "users_who_pinned", null = True, blank = True)