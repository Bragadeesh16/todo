from django.db import models

class todo(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    completed  = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title