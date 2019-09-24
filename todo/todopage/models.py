from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.title

class TodoList(models.Model):
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
