from django.core.urlresolvers import reverse
from django.views.generic import (CreateView, UpdateView, DeleteView,
								  FormView, DetailView, ListView)

from .forms import PostForm
from .models import Group, Board, Topic, Post
from .mixins import LoginRequiredMixin


class ListGroupView(ListView):
	"""
	List all groups with their boards
	"""
	model = Group
	template_name = 'list_group.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ListGroupView, self).get_context_data(*args, **kwargs)
		context['boards'] = Board.objects
		return context


class DetailBoardView(DetailView):
	"""
	List all Topic objects available to Board
	"""
	model = Board
	template_name = 'detail_board.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DetailBoardView, self).get_context_data(*args, **kwargs)
		context['topics'] = Topic.objects.filter(board=self.get_object().id)
		context['counts'] = Topic.objects.annotate(post=Count('post'))
		return context


class DetailTopicView(DetailView):
	"""
	Detail Topic object and list Post objects
	"""
	model = Topic
	template_name = 'detail_topic.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DetailTopicView, self).get_context_data(*args, **kwargs)
		context['posts'] = Post.objects.filter(topic=self.get_object().id)
		return context


class CreateTopicView(CreateView):
	model = Topic
	template_name = 'manage_topic.html'

	def get_success_url(self):
		return reverse('detail-topic', kwargs={'pk', self.get_object().id})


class UpdateTopicView(UpdateView):
	model = Topic
	template_name = 'manage_topic.html'

	def get_success_url(self):
		return reverse('detail-topic', kwargs={'pk', self.get_object().id})


class DeleteTopicView(DeleteView):
	model = Topic
	template_name = 'manage_topic.html'

	def get_success_url(self):
		return reverse('list-topic')


class PostView(FormView):
	template_name = 'manage_post.html'
	form_class = PostForm

	def get_form_kwargs(self):
		kwargs = super(PostView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		kwargs['topic'] = self.request.id
		return kwargs
