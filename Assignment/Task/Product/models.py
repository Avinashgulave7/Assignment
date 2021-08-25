from django.db import models

# Create your models here.
class PRODUCT(models.Model):
    p_name=models.CharField(max_length=50)
    p_weight=models.FloatField()
    p_price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
