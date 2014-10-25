from django.conf import settings
from django.db import models

# Create your models here.
class Group(models.Model):
	# Fields
	name = models.CharField(max_length=200)

	# Model Methods
	def __str__(self):
		return "%s" % self.name

class Board(models.Model):
	# Fields
	name = models.CharField(max_length=200)
	desc = models.TextField()

	# Relations
	group = models.ForeignKey(Group)

	# Model Methods
	def __str__(self):
		return "%s" % self.name

class Topic(models.Model):
	# Fields
	subject = models.CharField(max_length=200)
	body = models.TextField()

	# Relations
	board = models.ForeignKey(Board)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	# Model Methods
	def __str__(self):
		return "%s" % self.subject

class Post(models.Model):
	# Fields
	subject = models.CharField(max_length=200)
	body = models.TextField()

	# Relations
	topic = models.ForeignKey(Topic)
	reply = models.ForeignKey(Post, blank=True, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	# Model Methods
	def __str__(self):
		return "%s" % self.subject