from django.db import models

# Create your models here.
class Registration(models.Model):
    user_id=models.IntegerField()
    item_id=models.IntegerField()
    rating=models.IntegerField()
    timestamp=models.IntegerField()
    title=models.CharField(max_length=50)
