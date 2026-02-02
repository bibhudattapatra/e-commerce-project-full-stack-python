from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="admins")
    mobile = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address=models.CharField(max_length=200,null=True,blank=True)
    joined_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class CompanyCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/company/', null=True, blank=True)


    def __str__(self):
        return self.title
 

class MedicineCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcategories')

    def __str__(self):
        return self.title

    
    
class MedicineProduct(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    #use both catagories
    company_category = models.ForeignKey(CompanyCategory, on_delete=models.SET_NULL, null=True, blank=True)
    medicine_category = models.ForeignKey(MedicineCategory, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="products/")
    brand = models.CharField(max_length=100, null=True, blank=True)
    composition = models.CharField(max_length=300, null=True, blank=True)
    usage = models.TextField(null=True, blank=True)
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    expiry_date = models.DateField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    requires_prescription = models.BooleanField(default=False)
    serial_number = models.PositiveIntegerField(null=True, blank=True)
    pack = models.CharField(max_length=50, null=True, blank=True)
    packing_type = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    customer=models.ForeignKey(
        Customer, on_delete=models.SET_NULL,null=True,blank=True)
    total=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart:" +str(self.id) 
    
class CartProduct(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey( MedicineProduct,on_delete=models.CASCADE)
    rate=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    subtotal=models.PositiveIntegerField()

    def __str__(self):
        return "Cart:" + str(self.cart.id) + "CartProduct:" + str(self.id)


ORDER_STATUS=(
    ("Order Received","Order Received"),
    ("Order Processing","Order Processing"),
    ("On the way","On the way"),
    ("Order Completed","Order Completed"),
    ("Order Canceled","Order Canceled"),
)
class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    ordered_by=models.CharField(max_length=200)
    shipping_address=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(null=True,blank=True)
    subtotal=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    total=models.PositiveIntegerField()
    order_status=models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order:" + str(self.id)


