from django.db import models
# توضیح دارد
class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()

