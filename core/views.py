from cgitb import reset
from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.models import *
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import datetime 
from django.urls import reverse

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

class Contact(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

class About(TemplateView):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

class Blog(TemplateView):
    template_name = "blog.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

class Pricing(TemplateView):
    template_name = "pricing.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

class BlogDetails(TemplateView):
    template_name = "blog-details.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

class Login(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

class Error404(TemplateView):
    template_name = "404.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

class SignUp(TemplateView):
    template_name = "sign-up.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

