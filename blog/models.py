from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')  #to link to another model (Users already exist by default)
    title = models.CharField(max_length=200)  #text with limir
    text = models.TextField() #long text without limit
    created_date = models.DateTimeField(  #date and time
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


