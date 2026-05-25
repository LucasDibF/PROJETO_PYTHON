from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField("Título", max_length=200)
    description = models.TextField("Descrição", blank=True)
    done = models.BooleanField("Concluída", default=False)
    deadline = models.DateField("Prazo", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["done", "deadline", "-created_at"]

    def __str__(self):
        return self.title
