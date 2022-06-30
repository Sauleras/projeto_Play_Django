from django.urls import path
from .views import Index, Contact, About, Blog, Pricing, BlogDetails, Login, Error404, SignUp

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('about/', About.as_view(), name='about'),
    path('blog/', Blog.as_view(), name='blog'),
    path('pricing/', Pricing.as_view(), name='pricing'),
    path('blog-details/', BlogDetails.as_view(), name='blog-details'),
    path('login/', Login.as_view(), name='login'),
    path('404/', Error404.as_view(), name='404'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
]