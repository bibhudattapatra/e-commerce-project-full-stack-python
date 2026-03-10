from django.urls import path
from .views import *

app_name="app1"
urlpatterns=[
    path('',HomeView.as_view(), name="home"),
    path("about/",AboutView.as_view(), name='about'),
    path("contactus/",ContactView.as_view(),  name="contact_us"), 
    path("all-products/",AllproductView.as_view(), name="allproducts"),
    path("allcompanies/", AllcompanyView.as_view(), name="allcompanies"),
    path("Product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),
    path("add-to-cart-<int:prod_id>/",AddToCartView.as_view(),name="addtocart"),
    path("mycart/",MyCartView.as_view(),name="mycart"),
    path("managa-cart/<int:cp_id>/",ManageCartView.as_view(),name="managecart"),
    path("empty-cart/",EmptyCartView.as_view(),name="emptycart"),
    path("checkout/",CheckoutView.as_view(),name="checkout"),
    path("register/",CustomerRegistrationView.as_view(),name="customerregistration"),
    path("logout/",CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/",CustomerLoginView.as_view(), name="customerlogin"),
    path("profile/",CustomerProfileView.as_view(),name="customerprofile"),
    path("profile/order.<int:pk>/",CustomerOrderDetailView.as_view(),name="customerorderdetail"),
    #serach pannel urls
    path("serach/",SearchView.as_view(), name = "search"),


    #admin pannerl urls 
    path("admin-login/",AdminLoginView.as_view(),name="adminlogin"),
    path("admin-home/",AdminHomeView.as_view(),name="adminhome"),
    path("admin-order/<int:pk>/",AdminOrderDetailView.as_view(),name="adminorderdetail"),
    path("admin-all-orders/",AdminOrderListView.as_view(),name="adminorderlist"),
    path("admin-order-<int:pk>-change",AdminOrderStatusChangeView.as_view(),name="adminorderstatuschange"),

    # # api url
    # # PRODUCTS
    # path("api_products/", ProductListAPI.as_view()),
    # path("products/<slug:slug>/", ProductDetailAPI.as_view()),

    # # CATEGORIES
    # path("categories/", MedicineCategoryAPI.as_view()),

    # # SEARCH
    # path("search/", MedicineSearchAPI.as_view()),

    # # CART
    # path("cart/", MyCartAPI.as_view()),
    # path("cart/add/", AddToCartAPI.as_view()),

    # # ORDER / CHECKOUT
    # path("checkout/", CheckoutAPI.as_view()),



    # Company Category
    path('api_company-category/', CompanyCategoryListView.as_view()),
    path('api_id_company-category/<int:pk>/', CompanyCategoryDetailView.as_view()),

    # Medicine Category
    path('api_medicine-category/', MedicineCategoryListView.as_view()),
    path('api_id_medicine-category/<int:pk>/', MedicineCategoryDetailView.as_view()),

    # Product
    path('api_products/', MedicineProductListView.as_view()),
    path('api_id_products/<int:pk>/', MedicineProductDetailView.as_view()),

    # Cart
    path('api_cart/', CartListView.as_view()),
    path('api_id_cart/<int:pk>/', CartDetailView.as_view()),

    # Order
    path('api_orders/', OrderListView.as_view()),
    path('api_orders/<int:pk>/', OrderDetailView.as_view()),
]