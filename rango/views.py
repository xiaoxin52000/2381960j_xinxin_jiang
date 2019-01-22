from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page

def show_category(request,category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug= category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)

def add_page(request,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug= category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)

def index(request):
   # context_dict = {'boldmessage': "Crunchy, creamy, cookoe, candy, cupcake"}
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says hey there partners")
