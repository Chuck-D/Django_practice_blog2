from django.shortcuts import render
from .models import Post #.models just means from the model file in current package


# Create your views here.
def home(request):

	context = {
		'posts': Post.objects.all()
	}
	return render(request,'blog/home.html',context)#passes data into template


def about(request):
	return render(request, 'blog/about.html',{'title':'About'})

def contact(request):
	return render(request, 'blog/contact.html',{'title':'Contact'})

