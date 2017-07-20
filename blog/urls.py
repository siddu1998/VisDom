from django.conf.urls import url

from . import views


urlpatterns = [
	
	#home-page
	url(r'^$', views.home, name='home'),
	

	#blog and blog detail
	 url(r'^Blog/$', views.BlogListView.as_view(), name='blog'),
	 url(r'^userlist/$', views.UserProfileListView.as_view(), name='user'),
	 url(r'^Blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
	 url(r'^user/(?P<pk>\d+)$', views.UserProfileDetailView.as_view(), name='user-detail'),
	 url(r'^Blog/create$', views.BlogCreateView.as_view(), name='create'),
	


	 

	 url(r'^Blog/update/(?P<pk>\d+)$', views.BlogUpdate.as_view(), name='update'),
	 url(r'^Blog/delete/(?P<pk>\d+)$', views.BlogDelete.as_view(), name='delete'),
	
	 url(r'^Blog/(?P<pk>\d+)/comment/$', views.BlogCommentCreate.as_view(), name='blog-comment'), 
	 #user-shit
	 url(r'^register/$', views.register, name='register'),
	 url(r'^profile/$', views.profile, name='profile'),
	 url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	 url(r'^profile/edituser/$', views.edit_user_profile, name='edit_user_profile'),
	 
		 
]
