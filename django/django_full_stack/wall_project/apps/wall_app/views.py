from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from apps.wall_app.models import *

# Create your views here.
def index(request):
	if request.session.get('user_id'):
		user = User.objects.get(id=request.session['user_id'])

		context = {
			"user": user,
			"wall_messages": Message.objects.all().order_by('-created_at')
		}

		return render(request, "wall_app/feed.html", context)
	else:
		return render(request, "wall_app/index.html")

def create_user(request):
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)

		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)

			return redirect("/")
		else:
			user = User.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], email=request.POST['email'], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
			messages.success(request, "Successfully registered!")

			request.session['user_id'] = user.id

			context = {
				"user": user,
				"wall_messages": Message.objects.all().order_by('-created_at')
			}

			return render(request, "wall_app/feed.html", context)

def create_session(request):
	if request.method  == "POST":
		user = User.objects.get(email=request.POST['email'])
		if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
			request.session['user_id'] = user.id

			messages.success(request, "Successfully logged in!")

			context = {
				"user": user,
				"wall_messages": Message.objects.all().order_by('-created_at')
			}

			return render(request, "wall_app/feed.html", context)
		else:
			return redirect("/")
	else:
		return redirect("/")

def destroy_session(request):
	request.session.clear()

	return redirect("/")

def create_message(request):
	user = User.objects.get(id=request.session['user_id'])
	Message.objects.create(message=request.POST['wall_message_text'], user=user)

	context = {
		"user": user,
		"wall_messages": Message.objects.all().order_by('-created_at')
	}

	return redirect("/")

def destroy_message(request, message_id):
	user = User.objects.get(id=request.session['user_id'])
	print(message_id)
	message = Message.objects.get(id=message_id)
	message.delete()

	context = {
		"user": user,
		"wall_messages": Message.objects.all().order_by('-created_at')
	}

	return redirect("/")

def create_comment(request, message_id):
	user = User.objects.get(id=request.session['user_id'])
	Comment.objects.create(comment=request.POST['wall_message_comment_text'], message=Message.objects.get(id=message_id), user=user)

	context = {
		"user": user,
		"wall_messages": Message.objects.all().order_by('-created_at')
	}

	return redirect("/")
