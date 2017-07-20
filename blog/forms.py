from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Blog, UserProfile
from pagedown.widgets import PagedownWidget

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
   # desciption=forms.CharField(required=True)
   # profile_image=models.FileField(null=True,blank=True)

    class Meta:
        model = User
        fields=(
                'username', 
                'email',
                'password1',
                'password2',    
                #'desciption'
                #'profile_image'
                )
        def save(self,commit=True):
            user = super(RegistrationForm,self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name=self.cleaned_data['last_name']  
            user.email=self.cleaned_data['email']
          #  user.desciption=self.cleaned_data['desciption']

            if commit:
              user.save()

            return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields=( 'email',
                'first_name',
                #'desciption',
                'last_name',
                'password'

            )

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('first_name','last_name',"desciption",)

class BlogForm(forms.ModelForm):
    publish=forms.DateField(widget=forms.SelectDateWidget)
    content = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = Blog
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]
