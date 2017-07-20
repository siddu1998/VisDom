
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.models import User
from .forms import RegistrationForm, EditProfileForm, EditUserProfileForm
from .forms import BlogForm
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from pagedown.widgets import PagedownWidget
from django import forms
from django.urls import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.views.generic import FormView
from django.core.urlresolvers import reverse
# Create your views here.
def home(request):
	#num_users=Author.objects.count()
	#front_page=TextModel.objects.all()
	return render(
		request,
		'home.html',
		context={}
		)

class BlogListView(generic.ListView):
	model=Blog
	paginate_by = 10



class BlogDetailView(LoginRequiredMixin,generic.DetailView):
	model=Blog
	


class BlogCommentCreate(LoginRequiredMixin, generic.CreateView):
    model = BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})




class UserProfileListView(generic.ListView):
	model=UserProfile

class UserProfileDetailView(LoginRequiredMixin,generic.DetailView):
	model=UserProfile


def register(request):

	if request.method == 'POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts/login')
	else:
		form=RegistrationForm()
		args = {'form':form}
	return render(request,'reg_form.html', {'form':form})









def profile(request):
	args={"user":request.user}

	return render(request,'profile.html',args)


@login_required
def edit_profile(request):

	if request.method =='POST':
		form=EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/')

	else:
		form=EditProfileForm(instance=request.user)
		args={'forms':form}
		return render(request,'user_change.html', {'form':form})








@login_required
def edit_user_profile(request):
		if request.method =='POST':
			form=EditUserProfileForm(request.POST, instance=request.user.userprofile)
			if form.is_valid():
				form.save()
				return redirect('/')

		else:
			form=EditUserProfileForm(instance=request.user.userprofile)
			args={'forms':form}
			return render(request,'user_profile_change.html', {'form':form})








class BlogCreateView(LoginRequiredMixin,generic.CreateView):
	model=Blog
	form_class=BlogForm
	template_name='blog_create.html'

	def form_valid(self,form):
		blog=form.save(commit=False)
		blog.author=UserProfile.objects.get(user=self.request.user)
		blog.save()
		return redirect('/')






class BlogUpdate(LoginRequiredMixin,generic.UpdateView):
	model=Blog
	fields=['title','content','image']
	template_name_suffix='_update_form'





class BlogDelete(LoginRequiredMixin,generic.DeleteView):
	
	model=Blog
	success_url=reverse_lazy('profile')