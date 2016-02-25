from django.shortcuts import render

# Create your views here.

def login(request):
	name=request.GET['name']
	number=request.GET['passwd']
	return render(request,'web1.html',{'name':name,'number':number})

def signin(request):
	
	return render(request,'login.html',{})

def twosignin(request):
	print('---------------------------')
	name=request.GET['name']
	passwd=request.GET['passwd']
	return render(request,'signintwo.html',{'name':name,'passwd':passwd})

def search(request):

	
	pass
	return render(request,'.html',{ })