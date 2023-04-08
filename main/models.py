from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=50)
    is_Completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class TodoItem(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    is_Completed = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.name
    
    def getDesc(self): 
        return self.description[:150]+'...'