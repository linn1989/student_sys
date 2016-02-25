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
	id=request.GET['id']
	passwd=request.GET['passwd']
	return render(request,'signin_ok.html',{'id':id,'passwd':passwd})

