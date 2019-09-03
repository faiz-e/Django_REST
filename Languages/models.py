from django.db import models

# Create your models here.


class Language(models.Model):
    language_name = models.CharField(max_length=10)
    language_creator = models.CharField(max_length=100)
    language_created_in = models.IntegerField()

    def __str__(self):
        return self.language_name
