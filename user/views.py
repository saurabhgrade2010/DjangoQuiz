from django.shortcuts import render,get_object_or_404, redirect
from .forms import UserForm
from .models import User,Score
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.
def home_view(request,*args,**kwargs) :
	return render(request,"header.html",{})


def logout_view(request,*args,**kwargs) :
	del request.session['user_id']
	request.session.modified = True
	return redirect('../')



def main_page_view(request,*args,**kwargs) :
	uid=request.session['user_id']
	obj=User.objects.get(user_id=uid)
	context={
	 'object' :obj
	}
	return render(request,"main_page.html",context)


def register_view(request,*args,**kwargs) :
	return render(request,"user_register.html",{})


def forget_password(request,*args,**kwargs):
	if request.method == 'GET' :
		Email = request.GET['Email']
		obj=''
		try :
			obj = User.objects.get(email = Email)
		except User.DoesNotExist:
			obj=''
		if obj == '':
			return HttpResponse("no")
		else:
			print(obj.email)
			context = {
			 'object' : obj
			}
			return HttpResponse("yes")


def forget1_view(request,*args,**kwargs) :
	if request.method == 'GET' :
		Email = request.GET['Email']
		P = request.GET['P']
		obj = ''
		try :
			obj = User.objects.get(email = Email)
		except User.DoesNotExist :
			obj = ''
		if obj == '' :
			return HttpResponse("no")
		else :
			obj.password = P
			obj.save()
			return HttpResponse("yes") 


def forget_view(request,*args,**kwargs) :
	return render(request,"forget_page.html",{})

def register_user(request,*args,**kwargs) :
	if request.method == 'GET':
		Fname = request.GET['Fname']
		Lname = request.GET['Lname']
		Mobile = request.GET['Mobile']
		Email = request.GET['Email']
		Password=request.GET['Password']
		x='0';
		User.objects.create(fname = Fname,lname=Lname,mobile =Mobile,email =Email,password =Password,acc_type=x)
		return HttpResponse("yes")



def user_login_fun(request,*args,**kwargs):
	if request.method == 'POST' :
		Email= request.POST.get('email')
		password=request.POST.get('password')
		obj = User.objects.filter(email =Email)
		for x in obj :
			print(x.email)
			print(x.password)
			if x.email ==Email and x.password == password :
				request.session['user_id'] = x.user_id
				return redirect('../main_page')
			else:
				return HttpResponse("no")
	else:
		return render(request,'/header.html',{})    	    	
	

def login_view(request,*args,**kwargs)	:
	return render(request,"user_login.html",{})	