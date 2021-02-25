from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=250)
  date_created = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  description = models.TextField()
  task_complete = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'todos'
    managed = True
    verbose_name = 'Todo'
    verbose_name_plural = 'Todos'
