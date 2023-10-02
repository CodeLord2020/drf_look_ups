from django.contrib import admin
from .models import student, Product, Account, Money

# Register your models here.

admin.site.register(student)
admin.site.register(Product)
admin.site.register(Account)
admin.site.register(Money)