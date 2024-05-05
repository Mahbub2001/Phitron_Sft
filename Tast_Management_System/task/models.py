from django.db import models
from category.models import TaskCategory

class Task(models.Model):
    taskTitle = models.CharField(max_length=50, verbose_name='Task Title')
    taskDescription = models.TextField(verbose_name='Task Description')
    is_completed = models.BooleanField(default=False, verbose_name='Is Completed')
    TaskAssignDate = models.DateField(verbose_name='Task Assign Date')
    category = models.ManyToManyField(TaskCategory, related_name="tasks")

    def __str__(self):
        return self.taskTitle
