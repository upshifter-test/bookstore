from cloudinary.models import CloudinaryField
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    publish_date = models.DateField()
    is_available = models.BooleanField(default=True)
    cover = CloudinaryField('cover')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


