from django.db import models


class TaskCategory(models.Model):
    category_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.category_name
