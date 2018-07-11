from django.db import models

# Create your models here.
class Airlines(models.Model):
	flight_number=models.CharField(max_length=8,unique=True)
	airlines_id=models.CharField(max_length=10)
	source=models.CharField(max_length=20)
	destination=models.CharField(max_length=20)
	departure=models.TimeField()
	arrival=models.TimeField()
	base_price=models.DecimalField(decimal_places=2,max_digits=10)

	def __str__(self):
		return self.flight_number

class Users(models.Model):
	user_id=models.CharField(max_length=16)
	email=models.EmailField(max_length=50,unique=True)
	password=models.CharField(max_length=20)
	phone_number=models.IntegerField()
	gender=models.CharField(max_length=10)
	def __str__(self):
		return self.email

class Bookings(models.Model):
	booking_id=models.AutoField(primary_key=True)
	email=models.ForeignKey(Users,on_delete=models.CASCADE)
	flight_num=models.ForeignKey(Airlines,on_delete=models.CASCADE,default='00000',editable=True)

