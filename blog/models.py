from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
