from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Item

# Create your views here.
def item_list(request):
    context = {
        'items': Item.objects.all()

    }
    return render(request,'home-page.html',context)

def products(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request,'product-page.html')

def checkout(request):
    return render(request,"checkout-page.html")

class HomeView(ListView):
    model = Item
    template_name = "home-page.html"


# def homePage(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request,"home-page.html",context)

class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"
