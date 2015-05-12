from django.shortcuts import render,redirect
from job.models import Author

def save(request):
	s=Author()	
	s.first_name=request.POST['first_name ']
	s.last_name =request.POST['last_name ' ]
	s.email     =request.POST['email']
	s.save()
	return redirect("")
