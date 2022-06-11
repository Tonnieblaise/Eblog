from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=400, default = 'my_title')
    blog_post = models.TextField(max_length=None)

    def __str__(self):
        return f'{self.id} {self.name}'