from django.db import models

# Create your models here.

# class client(models.Model):
#     id = models.IntegerField(primary_key= True)
#     fullname = models.CharField(max_length=250) 
#     business_name = models.CharField(max_length=250)
#     tax_id = models.IntegerField()
#     vat_id = models.IntegerField() 
#     business_id = models.IntegerField()
#     tax_rate = models.DecimalField()
#     phone = models.CharField(max_length=10)
#     website = models.CharField(max_length=1000)
#     logo_url = models.CharField(max_length=250)
#     payment_type = models.CharField(max_length=1) # O is one-time and R is recurring 
#     payment_terms = models.CharField(max_length=10) # 90 days
#     created_at timestamptz, 
#     updated_at timestamptz,
#     created_by varchar,
#     updated_by varchar
