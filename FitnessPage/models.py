from django.db import models


# Create your models here.

class Goals(models.Model):
    goal = models.CharField(max_length=200, default="Add Goal")
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.goal