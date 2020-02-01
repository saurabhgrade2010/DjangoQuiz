from django.db import models

# Create your models here.
class User(models.Model) :
	user_id = models.IntegerField(primary_key=True)
	fname   = models.CharField(max_length=120,null=False)
	lname   = models.CharField(max_length=120,null=True)
	mobile  = models.CharField(max_length=20,null= True)
	email   = models.CharField(max_length=50,null= False)
	password= models.CharField(max_length=20,null= False)
	acc_type= models.TextField(null= False)	
class Score(models.Model) :
	user_id =  models.IntegerField(null = False)
	result  = models.DecimalField(decimal_places=2,max_digits=10000,null=False)

