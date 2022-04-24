from django.urls import path

from store.views import store, cart, checkout, updateItem, processOrder

urlpatterns = [
    path('', store, name="store"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('update_item/', updateItem, name="update_item"),
    path('process_order/', processOrder, name="process_order"),
]