from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	"""Restrict visible form elements to subject and body"""
	class Meta:
		model = Post
		fields = ('subject', 'body')