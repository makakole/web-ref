from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.



def index(request):
    context = {'content': {'': ''}}


    return render(request, 'main_app/index.html', context)



def register(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
		else:
			form = UserRegisterForm()
	else:
		form = UserRegisterForm()

	context = {'form': form}
	return render(request, 'main_app/register.html', context)



def dashboard(request):
    context = {'content': {'': ''}}

    # return HttpResponse("Welcome to dashboard")

    return render(request, 'main_app/dashboard-base.html', context)