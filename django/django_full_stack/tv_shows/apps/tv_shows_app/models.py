from django.db import models
import dateutil.parser
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
	def basic_validator(self, post_data):
		errors = {}

		if len(post_data['show_title']) < 2:
			errors['show_title'] = "Show title should be at least 2 characters"
		if Show.objects.get(title=post_data['show_title']):
			errors['show_title'] = "Show title already exists"
		if len(post_data['show_network']) < 3:
			errors['show_network'] = "Show network should be at least 3 characters"
		if post_data['show_description'] and len(post_data['show_description']) < 10:
			errors['show_description'] = "Show description should be at least 10 characters"
		if dateutil.parser.parse(post_data['show_release_date']) > datetime.now():
			errors['show_release_date'] = "Show release date should be in the past"

		return errors

class Show(models.Model):
	title = models.CharField(max_length=255)
	network = models.CharField(max_length=255)
	release_date = models.DateTimeField()
	description = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ShowManager()
