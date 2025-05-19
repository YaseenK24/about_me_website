from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField(blank=True)

    def __str__(self):
        return self.question_text



# Create your models here.
