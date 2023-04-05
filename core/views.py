from django.shortcuts import render

# Create your views here.
from item.models import CategoryModel,Item

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    category = CategoryModel.objects.all()
    return render(request, 'core/index.html',{
        'categories':category,
        'items':items,
    })

def contact(request):
    return render(request,'core/contact.html')