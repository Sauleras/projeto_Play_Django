from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from core.forms import RegisterForms
from django.contrib.auth import authenticate, login, logout

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

    def post(self, request):

        if request.method == 'POST':

            username = request.POST['username']
            pass1 = request.POST['password']          

            user_obj = authenticate(username=username, password=pass1)
            
            if user_obj is not None:
                login(request, user_obj)
                return redirect('index')
            
            else:

                messages.error(request, 'Credenciais invalidas')
            
        return render(request, self.template_name)

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

    def post(self, request):
        form = RegisterForms(request.POST or None, request.FILES or None)

        if form.is_valid():
            print("############################# FORM " + str(form))

            username = form.cleaned_data['username'] #request.POST['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name'] 
            email = form.cleaned_data['email']
            pass1 = form.cleaned_data['password']            

            myuser = User.objects.create_user(username, email, pass1) 
            myuser.first_name = first_name
            myuser.last_name = last_name

            myuser.save()

            messages.success(request, "Usuário cadastrado com sucesso.")
            
            return redirect('login')

        else:
            contexto = {
                "mensagemErro" : "Erro ao validar dados " + str(form.errors),
            }
            
        return render(request, self.template_name, contexto)
        
def sair(request):
    logout(request)
    messages.success(request, "Deslogado com sucesso!")
    return HttpResponseRedirect('/login')