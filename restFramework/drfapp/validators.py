from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product, Account

def validate_name(value):
    qs = Product.objects.filter(name__exact = value)
    if qs.exists():
        raise serializers.ValidationError(f"Product name {value} already exists")
    return value

def validate_mail(value):
    if "@gmail" not in value.lower():
        raise serializers.ValidationError("Contact mail must be G-mail")
    return value

unique_name = UniqueValidator(queryset= Product.objects.all())


# def validdate_account_name(value):
#     qs = Account.objects.filter(account_name__iexact = value)
#     if qs.exists():
#         raise serializers.ValidationError(f"Account name {value} already exists")
#     return value

def validate_account_name(value, instance=None):
    if instance is None:
        # It's a create operation, so check for uniqueness
        try:
            Account.objects.get(account_name__iexact=value)
            raise serializers.ValidationError(f"Account name {value} already exists.")
        except Account.DoesNotExist:
            return value
    else:
        # It's an update operation, skip the uniqueness check if the value remains the same
        if value == instance.account_name:
            return value
        try:
            Account.objects.exclude(pk=instance.pk).get(account_name__iexact=value)
            raise serializers.ValidationError(f"Account name {value} already exists.")
        except Account.DoesNotExist:
            return value


