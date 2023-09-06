from django.db import models

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    todo = models.ForeignKey(
        Todo, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
