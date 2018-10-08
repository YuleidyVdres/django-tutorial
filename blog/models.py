from django.db import models
from django.utils import timezone

class Post(models.Model):
    TECHNOLOGY='TE'
    HUMAN='HU'
    ANIMAL='AN'
    TYPE_OF_POST=(
        (TECHNOLOGY, 'Technology'),
        (HUMAN, 'Human'),
        (ANIMAL, 'Animal'),
    )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    type = models.CharField(max_length=2, choices=TYPE_OF_POST, default=TECHNOLOGY,)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
