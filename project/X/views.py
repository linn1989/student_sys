from django.shortcuts import render

# Create your views here.


# start here + login , or signin
def start(request):
	return render(request,'start.html')

# to login page, show student sys main page
def login(request):
	id=request.GET['id']
	passwd=request.GET['passwd']
	return render(request,'login_ok.html',{'id':id,'passwd':passwd})

# to signin page
def signin(request):	
	return render(request,'signin.html')
# sign ok page
def signin_ok(request):	
	id=int(request.GET['id'])
	passwd=request.GET['passwd']
	
	import mysql
	res=mysql.mysql('signin1',id)
	if len(res)==1: # id already exists
		return render(request,'signin_fail.html',{'id':id})
	elif len(res)==0:
		mysql.mysql('signin1',id,passwd,'test')
		return render(request,'signin_ok.html',{'id':id,'passwd':passwd})
	

