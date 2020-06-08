from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)#post requests instantiate usercreationform with post data
		if form.is_valid():#make sure data is valid
			form.save()#save data
			username= form.cleaned_data.get('username')

			messages.success(request, f'Account created for {username}!')#display message 
			return redirect('blog-home')
	else:
			form = UserRegisterForm()#create new instance of form(no POST data)
	return render(request, 'users/register.html', {'form':form})
