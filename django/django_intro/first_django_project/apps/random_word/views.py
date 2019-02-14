from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    return redirect("/random_word")

def generate_random_word(request):
	if request.method == "GET":
		context = {
			"word": request.session['word'],
			"counter": request.session['counter']
		}
		return render(request, "random_word/index.html", context)
	if request.method == "POST":
		random_word = get_random_string(length=14)
		request.session['word'] = random_word
		request.session['counter'] += 1
		context = {
			"word": request.session['word'],
			"counter": request.session['counter']
		}
		return render(request, "random_word/index.html", context)

def reset_counter(request):
	request.session['counter'] = 0
	return redirect("/random_word")

