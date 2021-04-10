from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

# Create your models here.
#*******
#Categ,Prod,CartProd,Cart,Order,Customer,Specif
#*******
User = get_user_model()

def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(self, *args, **kwargs):
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        return products


class LatestProducts:
    objects = LatestProductsManager


#def get_product_url(obj, viewname):
    #ct_model = obj.__class__._meta.model_name
    #return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class Category(models.Model):

    name = models.CharField(max_length=128, verbose_name='Category')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
        class Meta:
            abstract = True

        category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
        title = models.CharField(max_length=255, verbose_name='Product')
        slug = models.SlugField(unique=True)
        image = models.ImageField(verbose_name='Image')
        description = models.TextField(verbose_name='Description', null=True)
        price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
        quantity = models.PositiveIntegerField(default=0)

        def __str__(self):
            return self.title

class Notebook(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Diagonal')
    display = models.CharField(max_length=255, verbose_name='Display type')
    ram = models.CharField(max_length=255, verbose_name='RAM')
    video = models.CharField(max_length=255, verbose_name='Video cart')
    processor = models.CharField(max_length=255,verbose_name='Processor')
    os = models.CharField(max_length=255, verbose_name='OS')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Diagonal')
    display = models.CharField(max_length=255, verbose_name='Display type')
    resolution = models.CharField(max_length=255, verbose_name='Display option')
    battery = models.CharField(max_length=255,verbose_name='Battery')
    frontal_camera = models.CharField(max_length=255, verbose_name='Front camera')
    main_camera = models.CharField(max_length=255, verbose_name='Camera')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Buyer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total')

    def __str__(self):
        return "Product: {} (in cart)".format(self.product.title)

class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Owner', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, verbose_name='Phone number')
    address = models.CharField(max_length=255, verbose_name='Address')

    def __str__(self):
        return "Customer: {} {}".format(self.user.first_name, self.user.last_name)


