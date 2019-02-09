from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class LoginView(auth_views.LoginView):
	"""Aquí se hace el inicio de seión y traigo el modelo de django para hacerlo mas breve"""
	template_name = ('accounts/login.html')
	redirect_authenticated_user = True

class LogoutView(auth_views.LogoutView, LoginRequiredMixin):
	"""aquí hace logout el men es decir el usuario"""