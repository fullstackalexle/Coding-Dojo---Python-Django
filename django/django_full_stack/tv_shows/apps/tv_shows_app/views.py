from django.shortcuts import render, redirect
from apps.tv_shows_app.models import Show

# Create your views here.
def index(request):
	content = {
		"shows": Show.objects.all()
	}
	return render(request, "tv_shows_app/index.html", content)

def add_show(request):
	return render(request, "tv_shows_app/new.html")

def create_show(request):
	if request.method == "POST":
		Show.objects.create(title=request.POST['show_title'],network=request.POST['show_network'],release_date=request.POST['show_release_date'],description=request.POST['show_description'])
		return redirect("/")

def show_show(request, id):
	content = {
		"show": Show.objects.get(id=id)
	}
	return render(request, "tv_shows_app/show.html", content)

def edit_show(request, id):
	content = {
		"show": Show.objects.get(id=id)
	}	
	return render(request, "tv_shows_app/edit.html", content)

def update_show(request, id):
	show = Show.objects.get(id=id)

	if request.POST['show_title'] != show.title:
		show.title = request.POST['show_title']
	if request.POST['show_network'] != show.network:
		show.network = request.POST['show_network']
	if request.POST['show_release_date'] != show.release_date:
		show.release_date = request.POST['show_release_date']
	if request.POST['show_description'] != show.description:
		show.description = request.POST['show_description']

	show.save()

	content = {
		"show": show
	}	
	return render(request, "tv_shows_app/show.html", content)

def delete_show(request, id):
	show = Show.objects.get(id=id)

	show.delete()

	return redirect("/")


