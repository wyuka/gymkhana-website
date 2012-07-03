from django.db import models

class Complaint(models.Model):
    creator = models.ForeignKey('users.User', verbose_name = "person who made the complaint", related_name = "complaints_made")

    complaint_date = models.DateTimeField('date of complaint')

    COMPLAINT_TYPE_CHOICES = (
    (u'e', u'Electrical'),
    (u'm', u'Maintenance'),
    (u'a', u'Aquaguard'),
    (u'n', u'Network'),
    (u'f', u'Mess Food'),
    (u'e', u'Academic'),
    (u'o', u'Other'),
    )
    complaint_type = models.CharField(max_length=1, choices=COMPLAINT_TYPE_CHOICES)

    body = models.TextField('body of the complaint')