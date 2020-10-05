from django.shortcuts import render, redirect
from login.models import data
from itertools import permutations
from numpy import random
from django.core.mail import send_mail

# Create your views here.
def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	if request.method == 'POST':
		global email
		email = request.POST.get('email')
		passwrd = request.POST.get('passwrd')

		if data.objects.filter(email=email):
			l = data.objects.get(email=email)
			if l.password == passwrd:
				if l.twoauth == 'enable':
					return redirect('/twoauth/')
				else:
					return render(request, 'home.html', {'l':l})
			else:
				return redirect('/login/')
		else:
			return redirect('/login/')
		
	return redirect('/register/')

def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('passwrd')
		re_password = request.POST.get('re_passwrd')

		if password == re_password:
			d = data(name=name, email=email, password=password)
			d.save()

			l = data.objects.get(email=email)

	return render(request, 'home.html', {'l':l})

def home(request):
	if request.method == 'POST':
		global twoauth
		twoauth = request.POST.get('twoauth')
		t = data.objects.get(email=email)
		t.twoauth = twoauth
		t.save()
	return render(request, 'home.html')

def twoauth(request):
	if request.method == 'GET':
		return render(request, 'twoauth.html')
	perm = permutations([1, 2, 3, 4], 4)
	s = ''
	p = []
	for i in list(pert):
		for j in i:
			s = s+str(j)
		p.append(int(s))
		s = ''
	x = random.choice(p)
	subject = 'OTP'
	message = 'your otp is '+str(x)
	from_email= 'svigneshkrish007@gmail.com'
	send_mail(subject, message, from_email, ['vigneshvickii701@gmail.com'], fail_silently=False)
	if request.method == 'POST':
	    otp = request.POST.get('otp')
	    if otp == x:
	        return render(request, 'home.html')
	    else:
	    	return render(request, 'home.html')	
	return render(request, 'home.html')	




