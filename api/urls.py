from django.urls import path
from .views import *

urlpatterns = [

    # PRODUCTS
    path("products/", ProductListAPI.as_view()),
    path("products/<slug:slug>/", ProductDetailAPI.as_view()),

    # CATEGORIES
    path("categories/", MedicineCategoryAPI.as_view()),

    # SEARCH
    path("search/", MedicineSearchAPI.as_view()),

    # CART
    path("cart/", MyCartAPI.as_view()),
    path("cart/add/", AddToCartAPI.as_view()),

    # ORDER / CHECKOUT
    path("checkout/", CheckoutAPI.as_view()),
]
