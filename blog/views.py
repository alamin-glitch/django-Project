from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Post, Product

class HomeView(View):
    def get(self, request):
        return HttpResponse ("Welcome to the Home Page! Hello Everyone")
    
class AboutView(TemplateView):
    template_name = 'blog/about.html'
    Extra_context = {'title': 'About Us'}

class ContactView(TemplateView):
    template_name = 'blog/contact.html'
    Extra_context = {'title': 'Contact Us'}

def Post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    context = {
        'posts': posts
        }
    return render(request, 'blog/post_list.html', context)

def product_list(request):
    products = Product.objects.filter(is_published=True).order_by('-created_at')
    context = {
        'products': products
        }
    return render(request, 'blog/product.html', context)