from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

User._meta.get_field('email')._unique = True


class post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = RichTextField()
    imagen = models.ImageField(null=True,blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    published_date = models.DateTimeField(blank=False, null=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()