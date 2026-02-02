from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from app1.models import *
from .serializers import *


class ProductListAPI(APIView):
    def get(self, request):
        products = MedicineProduct.objects.all().order_by("-id")
        serializer = MedicineProductSerializer(products, many=True)
        return Response(serializer.data)

    
#Product details view
class ProductDetailAPI(APIView):
    def get(self, request, slug):
        product = MedicineProduct.objects.get(slug=slug)
        serializer = MedicineProductSerializer(product)
        return Response(serializer.data)

#medicen catagory view
class MedicineCategoryAPI(APIView):
    def get(self, request):
        categories = MedicineCategory.objects.all()
        serializer = MedicineCategorySerializer(categories, many=True)
        return Response(serializer.data)

#searching view
class MedicineSearchAPI(APIView):
    def get(self, request):
        keyword = request.GET.get("q")
        products = MedicineProduct.objects.filter(
            Q(title__icontains=keyword) |
            Q(composition__icontains=keyword) |
            Q(description__icontains=keyword)
        )
        serializer = MedicineProductSerializer(products, many=True)
        return Response(serializer.data)

    
#add to cart view
class AddToCartAPI(APIView):
    def post(self, request):
        product_id = request.data.get("product_id")
        product = MedicineProduct.objects.get(id=product_id)

        cart_id = request.session.get("cart_id")
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = Cart.objects.create(total=0)
            request.session["cart_id"] = cart.id

        cart_product, created = CartProduct.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={
                "rate": product.selling_price,
                "quantity": 1,
                "subtotal": product.selling_price
            }
        )

        if not created:
            cart_product.quantity += 1
            cart_product.subtotal += product.selling_price
            cart_product.save()

        cart.total += product.selling_price
        cart.save()

        return Response({"message": "Added to cart"})

# view cart 
class MyCartAPI(APIView):
    def get(self, request):
        cart_id = request.session.get("cart_id")
        if not cart_id:
            return Response({"cart": None})

        cart = Cart.objects.get(id=cart_id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
#checkout /order view
class CheckoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart_id = request.session.get("cart_id")
        if not cart_id:
            return Response({"error": "Cart empty"}, status=400)

        cart = Cart.objects.get(id=cart_id)

        order = Order.objects.create(
            cart=cart,
            ordered_by=request.user.username,
            shipping_address=request.data.get("address"),
            mobile=request.data.get("mobile"),
            email=request.data.get("email"),
            subtotal=cart.total,
            discount=0,
            total=cart.total,
            order_status="Order Received"
        )

        del request.session["cart_id"]
        return Response({"message": "Order placed", "order_id": order.id})
