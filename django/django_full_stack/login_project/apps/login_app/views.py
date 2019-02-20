from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from apps.login_app.models import User

# Create your views here.
def index(request):
	return render(request, "login_app/index.html")

def create_user(request):
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)

		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)

			return redirect("/")
		else:
			user = User.objects.create(first_name=request.POST['f_name'],last_name=request.POST['l_name'],birthdate=request.POST['birthdate'],email=request.POST['email'],password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
			messages.success(request, "Successfully registered!")

			request.session['user_id'] = user.id

			context = {
				"user": user
			}

			return render(request, "login_app/profile.html", context)

def create_session(request):
	if request.method == "POST":
		user = User.objects.get(email=request.POST['email'])
		print(bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()))
		if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
			request.session['user_id'] = user.id

			messages.success(request, "Successfully logged in!")

			context = {
				"user": user
			}

			return render(request, "login_app/profile.html", context)
		else:
			return redirect("/")

def destroy_session(request):
	request.session.clear()

	return redirect("/")		