from django.shortcuts import render, redirect#new2_redirect
from django.contrib.auth.forms import UserCreationForm#new1
from django.contrib.auth.models	import User#new3
from django.contrib.auth.decorators import login_required#new4
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView


# Create your views here.
def home(request):
	count = User.objects.count()
	return render(request, 'accounts/home.html', {'count': count})


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form': form})

@login_required
def secret_page(request):
	return render(request, 'accounts/secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
	template_name = 'accounts/secret_page.html'