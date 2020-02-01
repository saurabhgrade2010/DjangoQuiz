from django.db import models

# Create your models here.

class Quiz(models.Model) :
	sub_type = models.CharField(max_length=5,null= False)
	qsn      = models.CharField(max_length=200,null = False)
	ans1     = models.CharField(max_length=150,null= False)
	ans2     = models.CharField(max_length=150,null = False)
	ans3     = models.CharField(max_length=150,null = False)
	ans4     = models.CharField(max_length=150,null = False)
	ans      = models.IntegerField(null = False)