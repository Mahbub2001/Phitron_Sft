from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.category_name
