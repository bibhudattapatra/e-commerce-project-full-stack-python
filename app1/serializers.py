# from rest_framework import serializers
# from app1.models import *

# # ---------- CATEGORY ----------
# class CompanyCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CompanyCategory
#         fields = "__all__"


# class MedicineCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicineCategory
#         fields = "__all__"


# # ---------- PRODUCT ----------
# class MedicineProductSerializer(serializers.ModelSerializer):
#     company_category = CompanyCategorySerializer(read_only=True)
#     medicine_category = MedicineCategorySerializer(read_only=True)

#     class Meta:
#         model = MedicineProduct
#         fields = "__all__"


# # ---------- CART ----------
# class CartProductSerializer(serializers.ModelSerializer):
#     product = MedicineProductSerializer(read_only=True)

#     class Meta:
#         model = CartProduct
#         fields = "__all__"


# class CartSerializer(serializers.ModelSerializer):
#     cartproduct_set = CartProductSerializer(many=True, read_only=True)

#     class Meta:
#         model = Cart
#         fields = "__all__"


# # ---------- ORDER ----------
# class OrderSerializer(serializers.ModelSerializer):
#     cart = CartSerializer(read_only=True)

#     class Meta:
#         model = Order
#         fields = "__all__"

from rest_framework import serializers
from django.contrib.auth.models import User
from app1.models import (
    Admin,
    Customer,
    CompanyCategory,
    MedicineCategory,
    MedicineProduct,
    Cart,
    CartProduct,
    Order
)


# =====================================
# USER SERIALIZER
# =====================================
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email"]


# =====================================
# ADMIN SERIALIZER
# =====================================
class AdminSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = "__all__"


# =====================================
# CUSTOMER SERIALIZER
# =====================================
class CustomerSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"


# =====================================
# COMPANY CATEGORY SERIALIZER
# =====================================
class CompanyCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyCategory
        fields = "__all__"


# =====================================
# MEDICINE CATEGORY SERIALIZER
# =====================================
class MedicineCategorySerializer(serializers.ModelSerializer):

    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = MedicineCategory
        fields = "__all__"

    def get_subcategories(self, obj):
        subs = obj.subcategories.all()
        return MedicineCategorySerializer(subs, many=True).data


# =====================================
# MEDICINE PRODUCT SERIALIZER
# =====================================
class MedicineProductSerializer(serializers.ModelSerializer):

    # READ nested
    company_category = CompanyCategorySerializer(read_only=True)
    medicine_category = MedicineCategorySerializer(read_only=True)

    # WRITE using IDs
    company_category_id = serializers.PrimaryKeyRelatedField(
        queryset=CompanyCategory.objects.all(),
        source="company_category",
        write_only=True,
        required=False
    )

    medicine_category_id = serializers.PrimaryKeyRelatedField(
        queryset=MedicineCategory.objects.all(),
        source="medicine_category",
        write_only=True,
        required=False
    )

    class Meta:
        model = MedicineProduct
        fields = "__all__"


# =====================================
# CART PRODUCT SERIALIZER
# =====================================
class CartProductSerializer(serializers.ModelSerializer):

    # READ nested
    product = MedicineProductSerializer(read_only=True)

    # WRITE using ID
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=MedicineProduct.objects.all(),
        source="product",
        write_only=True
    )

    class Meta:
        model = CartProduct
        fields = "__all__"


# =====================================
# CART SERIALIZER
# =====================================
class CartSerializer(serializers.ModelSerializer):

    # Show customer details
    customer = CustomerSerializer(read_only=True)

    # Show cart products
    cart_products = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = "__all__"

    def get_cart_products(self, obj):
        items = CartProduct.objects.filter(cart=obj)
        return CartProductSerializer(items, many=True).data


# =====================================
# ORDER SERIALIZER
# =====================================
class OrderSerializer(serializers.ModelSerializer):

    # READ nested cart
    cart = CartSerializer(read_only=True)

    # WRITE using cart ID
    cart_id = serializers.PrimaryKeyRelatedField(
        queryset=Cart.objects.all(),
        source="cart",
        write_only=True
    )

    class Meta:
        model = Order
        fields = "__all__"