from django.db import models

class Post(models.Model):
    title = models.CharField('タイトル',max_length=50)
    content = models.TextField('内容',max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Create your models here.
