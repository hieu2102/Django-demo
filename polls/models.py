from django.db import models
from django.utils import timezone
import datetime
import pytz
#convert datetime to specific timezone
zone = pytz.UTC
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    # def was_published_recently(self):
    #     return (self.pub_date.to_python().month == timezone.datetime.now().month) \
    #            and  \
    #            (self.pub_date.to_python().day >= timezone.datetime.now().day-1) \
    #            and \
    #            (self.pub_date.to_python().year == timezone.now().year)

    def was_published_recently(self):
        # return self.pub_date >= zone.localize(timezone.datetime.now() - datetime.timedelta(days=1))
        now = timezone.now()
        return now - datetime.timedelta(days=1)<=self.pub_date<=now

    """modify how was_published_recently row is displayed in admin site"""
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text