# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "first_django/index.html", context)

def new(request):
	return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
	return redirect("/")

def show(request, number):
	return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
	return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
	return redirect("/")

def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'first_django/time_display.html', context)
