# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user=models.OneToOneField(User)
	first_name=models.CharField(max_length=100,default='')
	last_name=models.CharField(max_length=100,default='')
	desciption=models.CharField(max_length=500,default='')
	profile_image=models.FileField(null=True,blank=True) 	

	def __str__(self):
		return self.user.username
	def get_absolute_url(self):
		return reverse('user-detail',args=[str(self.id)])

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)




class Item(models.Model):
	product=models.CharField(max_length=200)
	image=models.FileField(null=True,blank=True)
	quantity=models.IntegerField(null=True,default=100)
	price=models.IntegerField(null=True)
	
	def __str__(self):
		return self.product




class Cart(models.Model):
	user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	product=models.ForeignKey(Item,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username




class Blog(models.Model):
	title=models.CharField(max_length=200)

	author=models.ForeignKey("UserProfile", on_delete=models.SET_NULL, null=True)
	image=models.FileField(null=True,blank=True)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	
	draft=models.BooleanField(default=False)
	publish=models.DateField(auto_now=False,auto_now_add=False)
	
	content=models.TextField(null=True)
	
	

	class Meta:
		ordering = ["-timestamp"]
	def get_absolute_url(self):	
		return reverse('blog-detail',args=[str(self.id)])

	def __str__(self):
		return (self.title)




class BlogComment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return(self.blog.title)



