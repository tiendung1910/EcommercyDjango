from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import ListView,DetailView
from .models import Item, OrderItem,Order
from django.utils import timezone

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
    return render(request,'product-page.html',context)

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


def add_to_cart(request,slug):
    item = get_object_or_404(Item,slug=slug)
    order_item = OrderItem.objects.get_or_create(item = item)
    order_qs = Order.objects.filter(user=request.user,ordered = False)
    if order_qs.exists():
        order = order_qs[0] 

        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1 
            order_item.save()
        else:
            order.items.add(order_item)
    
    else: 
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product",slug = slug)
