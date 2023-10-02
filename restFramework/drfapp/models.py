from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year_enrolled = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length= 1000)
    hostel = models.BooleanField(null=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    user = models.ForeignKey(User, null = True, on_delete= models.CASCADE)
    account_name = models.CharField(max_length = 50)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length = 50, null= True)
    created = models.DateTimeField(auto_now = True, editable=False)

    def __str__(self):
        return self.account_name

account_types =( 

    ('savings','savings'),
   ( 'current', 'current'),
    ('golden','golden'),
)

class Money(models.Model):
    display_name = models.OneToOneField(Account, on_delete = models.CASCADE, null = True)
    real_name = models.CharField(null = True, max_length = 70)
    account_type = models.CharField(max_length=10, default='savings', null = False, choices= account_types)
    debt = models.BooleanField(null = False, default= False)

    def __str__(self):
        return self.real_name

    

class Product(models.Model):
    user = models.ForeignKey(User, default=1, null = True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.BooleanField(default=False)
    discount_price = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.discount:
            self.discount_price = self.price * 0.95  # Apply 5% discount
        else:
            self.discount_price = None  # No discount

        super(Product, self).save(*args, **kwargs)

