from django.db import models

class exp(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    Created=models.DateTimeField(auto_now_add=True)

class NYC_data(models.Model):
    zip_code=models.CharField(max_length=20)
    Address=models.CharField(max_length=250)
    class Meta:
        db_table='NYC_data'