from django.db import models

# Create your models here.
class UploadImage(models.Model):
 caption = models.CharField(max_length=200)
 image = models.ImageField(upload_to='images')
 def __str__(self):
  return self.caption

class Cars(models.Model):
  cars_model = models.CharField(max_length=200)
  cars_luxury_type = models.CharField(max_length=200)
  cars_company_name = models.CharField(max_length=200)
  cars_route_name = models.CharField(max_length=200)
  cars_plate_no = models.CharField(max_length=200)
  cars_date_of_journey = models.DateField(auto_now=False, auto_now_add=False)
  cars_departure_time  = models.TimeField(auto_now=False, auto_now_add=False)
  cars_destination_time = models.TimeField(auto_now=False, auto_now_add=False)
  cars_created_time  =    models.DateTimeField(auto_now=False, auto_now_add=True)

class Routes(models.Model):
   routes_name = models.CharField(max_length=200)
   routes_created_time  = models.DateTimeField(auto_now=False, auto_now_add=True)

class Companies(models.Model):
   companies_name = models.CharField(max_length=200)
   companies_contact = models.IntegerField()
   companies_office = models.CharField(max_length=200)
   companies_created_time  = models.DateTimeField(auto_now=False, auto_now_add=True)

class Regions(models.Model):
   regions_name = models.CharField(max_length=50)
   regions_created_time  = models.DateTimeField(auto_now=False, auto_now_add=True)