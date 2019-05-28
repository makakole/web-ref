from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, AddIdForm, GenerateReferenceForm, RequestPermissionsForm
from .models import IdData
from django.contrib import messages
from .validate_id import valid_id
from .generate import generate_ref
from django.contrib.auth import get_user_model


User = get_user_model()

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


def add_id_number(request):
	available = True
	try:
		id_data = IdData.objects.get(user = request.user.id)
	except IdData.DoesNotExist:
		available = False
	
	if request.method == 'POST':
		form = AddIdForm(request.POST) if not available else AddIdForm(request.POST, instance=id_data)

		if form.is_valid():
			form_object = form.save(commit=False)
			id_number = form.cleaned_data.get('id_number')

			correct, error_thrown, date_of_birth = valid_id(id_number)
			if correct:
				form_object.user = request.user #User.objects.get(id = request.user.id)
				form_object.save()
				messages.success(request, f'ID Number info updated')
				return redirect('add-id-number')
			else:
				form = AddIdForm() if not available else AddIdForm(instance=id_data)
				# form = AddIdForm(instance=id_data)
				messages.error(request, f'' + error_thrown)
				# return redirect('add-id-number')
		else:
				form = AddIdForm() if not available else AddIdForm(instance=id_data)
				messages.error(request, f'invalid form')
				# return redirect('add-id-number')
	else:
		id_data.first_name = 'Owen'
		form = AddIdForm() if not available else AddIdForm(instance=id_data)
	
	context = {'form': form}


	return render(request, 'main_app/add-id-number.html', context)




def reference(request):

	if request.method == 'POST':
		form = GenerateReferenceForm(request.POST)
		p_form = RequestPermissionsForm(request.POST)
		if form.is_valid():
			stamp, ref = generate_ref(request.user.id)
			form_object = form.save(commit=False)
			p_form_object = p_form.save(commit=False)

			form_object.data = IdData.objects.get(user = request.user)
			form_object.reference = ref
			form_object.save()

			p_form_object.reference = form_object
			p_form_object.save()

			messages.success(request, f'generated')
			return redirect('reference')

		else:
			form = GenerateReferenceForm()
			p_form = RequestPermissionsForm()
	else:
		form = GenerateReferenceForm()
		p_form = RequestPermissionsForm()

	context = {
	'form': form,
	'p_form': p_form
	}

	return render(request, 'main_app/reference.html', context)



def history(request):

	history = References.objects.filter(user = request.user)

	messages.success(request, f'generated')
	return render(request, 'main_app/history.html')