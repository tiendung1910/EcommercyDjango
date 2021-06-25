from django.urls import path
from .views import item_list
from .views import(
    ItemDetailView,
    checkout,
    HomeView,
    add_to_cart
)

app_name = 'core'

urlpatterns = [
    # path('',item_list,name='item-list'),
    path('',HomeView.as_view(),name='home'),
    path('checkout/',checkout,name='checkout'),
    path('product/<slug>/',ItemDetailView.as_view(),name='product'),
    path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart')
]