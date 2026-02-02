from rest_framework import serializers
from app1.models import *

# ---------- CATEGORY ----------
class CompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategory
        fields = "__all__"


class MedicineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineCategory
        fields = "__all__"


# ---------- PRODUCT ----------
class MedicineProductSerializer(serializers.ModelSerializer):
    company_category = CompanyCategorySerializer(read_only=True)
    medicine_category = MedicineCategorySerializer(read_only=True)

    class Meta:
        model = MedicineProduct
        fields = "__all__"


# ---------- CART ----------
class CartProductSerializer(serializers.ModelSerializer):
    product = MedicineProductSerializer(read_only=True)

    class Meta:
        model = CartProduct
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    cartproduct_set = CartProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"


# ---------- ORDER ----------
class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
