from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    tip_question = models.BigIntegerField(default=0, null=True, blank=True)
    step = models.BigIntegerField(default=1)

    def __str__(self):
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text


class Answer(models.Model):
    text = models.TextField()
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    tip_response = models.CharField(max_length=100)

    def __str__(self):
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text