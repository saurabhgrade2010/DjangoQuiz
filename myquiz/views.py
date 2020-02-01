from django.shortcuts import render
from myquiz.models import Quiz
from user.models import Score
import json
from sklearn.linear_model import LinearRegression
from django.http import HttpResponse,JsonResponse
import matplotlib
#matplotlib.use('Agg')
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
# Create your views here.
def quiz_view(request,*args,**kwargs) :
	return render(request,"main_quiz.html",{})

def insert_score(request,*args,**kwargs) :
	uid=request.session['user_id']
	score = request.GET['score']
	Score.objects.create(user_id=uid,result=score)

def fetch_result(request,*args,**kwargs) :
	uid=request.session['user_id']
	obj=Score.objects.filter(user_id=uid)
	result_store= {}
	data = []
	#print(df)
	y=1
	for x in obj :
		result_store[y]=x.result
		data.append([y,x.result])
		y=y+1
	df = pd.DataFrame(data,columns = ['Test_no','Result'])
	print(df)
	X = df.iloc[ :, : -1].values
	Y = df.iloc[ :,1:2].values
	regressor = LinearRegression()
	regressor.fit(X,Y)
	y_pred = regressor.predict(X)
	print(y_pred)
	plt.scatter(X,Y,color= 'blue')
	#plt.plot(X,Y,color = 'green')
	plt.plot(X,regressor.predict(X),color= 'red')
	plt.title("Relationship btw Test_no and Result")
	plt.xlabel("Test number")
	plt.ylabel("Result")
	#plt.show()
	return JsonResponse(result_store)	


def fetch_view(request,*args,**kwargs):
	response_data={}
	y=0
	if request.method == 'GET':
		sub_t = request.GET['sub_type']
		obj = Quiz.objects.filter(sub_type=sub_t)
		for x in obj:
			response_data2={}
			response_data2['qsn']=x.qsn
			response_data2['ans1']=x.ans1
			response_data2['ans2']=x.ans2
			response_data2['ans3']=x.ans3
			response_data2['ans4']=x.ans4
			response_data2['ans']=x.ans
			y=y+1
			response_data[y]=response_data2
		print(response_data)	
		return JsonResponse(response_data)
	else:
		return JsonResponse(response_data)		
