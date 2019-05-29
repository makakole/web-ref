from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, AddIdForm, GenerateReferenceForm, RequestPermissionsForm, BankingDataForm
from .models import IdData, References, RequestPermissions, BankingData
from django.contrib import messages
from .validate_id import valid_id, check_gender, sa_citizen
from .encryptions import encrypt, decrypt
from .generate import generate_ref
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


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


@login_required
def dashboard(request):
    context = {'content': {'': ''}}

    # return HttpResponse("Welcome to dashboard")

    return render(request, 'main_app/dashboard.html', context)

@login_required
def add_id_number(request):
	available = True
	try:
		id_data = IdData.objects.get(user = request.user.id)
	except IdData.DoesNotExist:
		available = False
	
	if request.method == 'POST':
		form = AddIdForm(request.POST, request.FILES) if not available else AddIdForm(request.POST, request.FILES, instance=id_data)

		if form.is_valid():
			form_object = form.save(commit=False)
			id_number = form.cleaned_data.get('id_number')

			correct, error_thrown, date_of_birth = valid_id(id_number)
			if correct:
				form_object.user = request.user
				form_object.first_name = encrypt(form.cleaned_data.get('first_name'))
				form_object.second_name = encrypt(form.cleaned_data.get('second_name'))
				form_object.surname = encrypt(form.cleaned_data.get('surname'))
				form_object.id_number = encrypt(form.cleaned_data.get('id_number'))
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
		if available:
			id_data.first_name = decrypt(id_data.first_name)
			id_data.second_name = decrypt(id_data.second_name)
			id_data.surname = decrypt(id_data.surname)
			id_data.id_number = decrypt(id_data.id_number)
		form = AddIdForm() if not available else AddIdForm(instance=id_data)
	
	context = {'form': form}


	return render(request, 'main_app/add-id-number.html', context)



@login_required
def add_banking_info(request):
	available = True
	try:
		id_data = IdData.objects.get(user = request.user.id)
	except IdData.DoesNotExist:
		available = False
	
	if request.method == 'POST':
		form = AddIdForm(request.POST, request.FILES) if not available else AddIdForm(request.POST, request.FILES, instance=id_data)

		if form.is_valid():
			form_object = form.save(commit=False)
			id_number = form.cleaned_data.get('id_number')

			correct, error_thrown, date_of_birth = valid_id(id_number)
			if correct:
				form_object.user = request.user
				form_object.first_name = encrypt(form.cleaned_data.get('first_name'))
				form_object.second_name = encrypt(form.cleaned_data.get('second_name'))
				form_object.surname = encrypt(form.cleaned_data.get('surname'))
				form_object.id_number = encrypt(form.cleaned_data.get('id_number'))
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
		if available:
			id_data.first_name = decrypt(id_data.first_name)
			id_data.second_name = decrypt(id_data.second_name)
			id_data.surname = decrypt(id_data.surname)
			id_data.id_number = decrypt(id_data.id_number)
		form = AddIdForm() if not available else AddIdForm(instance=id_data)
	
	context = {'form': form}


	return render(request, 'main_app/add-banking-info.html', context)



@login_required
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
			form_object.user = request.user
			form_object.save()

			p_form_object.reference = form_object
			p_form_object.save()

			messages.success(request, f'generated')
			return redirect('history')

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


@login_required
def history(request):

	history = References.objects.filter(user = request.user)

	context = {
	'history': history
	}
	return render(request, 'main_app/history.html', context)



# def check_reference(request):
# 	context = None
# 	if 'check_refence' in request.GET:

# 		reference = request.GET['check_refence']

# 		reference = str(reference)

# 		if len(reference) == 15:
# 			node = reference[0:5]
# 			stamp = reference[5:10]
# 			user_id = reference[10:15]

# 			try:
# 				refs = References.objects.get(reference = reference)
# 			except References.DoesNotExist:
# 				messages.error(request, f'Your refence Number is not valid - not available')
# 			if refs:
# 				names = None
# 				date_of_birth = None
# 				gender = None
# 				nationality = None
# 				check_credit_score = None
# 				check_criminal_record = None

# 				perms = RequestPermissions.objects.get(reference = refs)
# 				data = IdData.objects.get(user = refs.user.id)
# 				if perms.names:
		
# 					first_name = data.first_name
# 					second_name = data.second_name
# 					surname = data.surname

# 				if perms.date_of_birth:
# 					correct, error_thrown, date_of_birth = valid_id(decrypt(data.id_number))
# 				# if perms.race:
# 				# 	pass
# 				if perms.gender:
# 					gender = check_gender(decrypt(data.id_number))
# 				if perms.nationality:
# 					nationality = sa_citizen(decrypt(data.id_number))
# 					if nationality:
# 						nationality = 'South African Citizen'
# 					else:
# 						nationality = 'Not South African Citizen'
# 				if perms.check_credit_score:
# 					pass
# 				if perms.check_criminal_record:
# 					pass

# 				context = {
# 				'first_name': decrypt(first_name),
# 				'second_name': decrypt(second_name),
# 				'surname': decrypt(surname),
# 				'date_of_birth': date_of_birth,
# 				'gender': gender,
# 				'nationality': nationality,
# 				'check_credit_score': check_credit_score,
# 				'check_criminal_record': check_criminal_record,
# 				'reference': reference
# 				}
# 		else:
# 			messages.error(request, f'Your refence Number is not valid - not 15 ' + str(len(reference)))
# 			return redirect('check-reference')
# 	else:
# 		pass
# 		# messages.success(request, f'check_refence')

	# return render(request, 'main_app/check-reference.html', context)




def check_reference(request):
	context = None
	if 'check_refence' in request.POST:

		reference = request.POST['check_refence']

		reference = str(reference)

		if len(reference) == 15:
			node = reference[0:5]
			stamp = reference[5:10]
			user_id = reference[10:15]

			try:
				refs = References.objects.get(reference = reference)
			except References.DoesNotExist:
				messages.error(request, f'Your refence Number is not valid - not available')
			if refs:
				names = None
				date_of_birth = None
				gender = None
				nationality = None
				check_credit_score = None
				check_criminal_record = None

				perms = RequestPermissions.objects.get(reference = refs)
				data = IdData.objects.get(user = refs.user.id)
				if perms.names:
		
					first_name = data.first_name
					second_name = data.second_name
					surname = data.surname

				if perms.date_of_birth:
					correct, error_thrown, date_of_birth = valid_id(decrypt(data.id_number))
				# if perms.race:
				# 	pass
				if perms.gender:
					gender = check_gender(decrypt(data.id_number))
				if perms.nationality:
					nationality = sa_citizen(decrypt(data.id_number))
					if nationality:
						nationality = 'South African Citizen'
					else:
						nationality = 'Not South African Citizen'
				if perms.check_credit_score:
					pass
				if perms.check_criminal_record:
					pass

				context = {
				'first_name': decrypt(first_name),
				'second_name': decrypt(second_name),
				'surname': decrypt(surname),
				'date_of_birth': date_of_birth,
				'gender': gender,
				'nationality': nationality,
				'check_credit_score': check_credit_score,
				'check_criminal_record': check_criminal_record,
				'reference': reference
				}
		else:
			messages.error(request, f'Your refence Number is not valid - not 15 ')
			return redirect('check-reference')
	else:
		pass
		# messages.success(request, f'check_refence')

	return render(request, 'main_app/check-reference.html', context)
