from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + ' - ' + self.author
