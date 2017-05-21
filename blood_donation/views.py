from django.http import HttpResponse
from django.shortcuts import render
from .forms import PersonForm
from django.utils import timezone
from django.shortcuts import redirect
from .models import Person
from django.contrib import messages

def home(request):
	person = Person.objects.raw('Select * from Person')
	if request.GET:
		group= request.GET.get("group")
		person = Person.objects.raw('Select * from Person where blood_group = %s',[group] )

	return render(request,'blood_donation/home.html',{'person':person})	

def donate(request):
	if request.POST:
		#Get the posted form
		form = PersonForm(request.POST)
		if form.is_valid():
			person = form.save(commit=False)
			person.post_date=  timezone.now()
			person.save()
			messages.info(request, 'Thanks for your nice work . Your Blood is very precious')
			return redirect('donate')
	else:
		form = PersonForm()
	return render(request,'blood_donation/donate.html',{'form':form})

def why_donate(request):
	return render(request,"blood_donation/why_donate.html")

def result(request):
	return HttpResponse("hello")