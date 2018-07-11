from django.shortcuts import render
from django.http import HttpResponse
from first.models import Airlines,Users,Bookings
from first.forms import NewUserForm,LoginForm,SearchingForm
# Create your views here.

def index(request):
	return render(request,'first/airlines.html')

def home(request):
	return render(request,'first/homepage.html')

def flights(request):
	flights_list=Airlines.objects.order_by('flight_number')
	#print(flights_list[0].source)
	flight_dict={'flight_record':flights_list}
	return render(request,'first/flights.html',context=flight_dict)

def signup(request):
	form =NewUserForm()
	if request.method=='POST':
		form=NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)

		else:
			print('Error form invalid')

	return render(request,'first/signup.html',{'form':form})

def login(request):
	form=LoginForm()
	if request.method=='POST':
		form=LoginForm(request.POST)

		if form.is_valid():
			em=form['email'].value()
			pwd=form['password'].value()
			user_list=Users.objects.filter(email=em,password=pwd)
			#print(user_list[0].email)
			if(user_list.count()==0):
				return index(request)
			else:
				return welcome(request,{'user_rec':user_list})

		else:
			print('Error form invalid')

	return render(request,'first/login.html',{'form':form})

def welcome(request,content=None):
	form=SearchingForm()
	request.method=None
	if request.method=='POST':
		form=SearchingForm(request.POST)
		if form.is_valid():
			src=form['mysrc'].value()
			dest=form['mydest'].value()
			user_list=Airlines.objects.filter(source=src,destination=dest)
			print(user_list[0].email)

			if(user_list.count()==0):
				print("Unsuccessful")
			else:
				return search(request)

		else:
			print('Error form invalid')
	context=dict(content,**{'form':form})
	print(context)
	return render(request,'first/welcome.html',context)

def search(request):
	return HttpResponse("hello searching")