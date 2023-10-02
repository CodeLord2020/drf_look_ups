from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import student, Product, Account, Money
from .validators import validate_name, validate_mail, unique_name, validate_account_name
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        #( 'name', 'age', 'faculty', 'department', 'year_enrolled', 'description')

class productSerializer(serializers.ModelSerializer):
    #discount_price = serializers.SerializerMethodField(read_only = True)
    edit = serializers.HyperlinkedIdentityField(view_name = "update-product", lookup_field = 'pk')
    email = serializers.EmailField(write_only = True, validators = [validate_mail])
    name = serializers.CharField(validators = [validate_name, unique_name])
    title = serializers.CharField(source = "name", read_only = True)
    user = serializers.CharField(read_only =True, max_length = 255)

    class Meta:
        model = Product
        fields = ['url',
                  'edit',
                  'email',
                  'user',
                  'pk',
                  'title',
                  'name',
                  'category',
                  'price',
                  'discount',
                  'discount_price',
                  ]
        
    def create(self, validated_data):
        email = validated_data.pop('email')
        return super().create(validated_data)
    
    def get_url(self, obj):
        # so i used this method cos it can work with other serilizers. 
        # The edit = serializers.HyperlinkedIdentityField........ works for Modelserializers
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={'pk':obj.pk }, request = request)
    
    # def validate_name(self, value):
    #     qs = Product.objects.filter(name__iexact = value)
    #     if qs.exists:
    #         raise serializers.ValidationError(f"Product name {value} already exists")
    #     return value

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    detail = serializers.HyperlinkedIdentityField(view_name = "account-detail", lookup_field = 'pk')
    edit = serializers.HyperlinkedIdentityField(view_name = "account-update", lookup_field = 'pk')
    account_name = serializers.CharField(validators = [validate_account_name], )

    class Meta:
        model = Account
        fields =[
            'user',
            'account_name',
            'detail',
            'edit',
            'age',
            'gender',
            'created'
        ]
    def get_detail(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("account-detail", kwargs={'pk':obj.pk }, request = request)

class AccountListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='account-detail-url')
    class Meta:
        model = Account
        fields = [ 'url', 'account_name', 'created']

class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['id']

class MoneySeializer(serializers.ModelSerializer):
    edit = serializers.HyperlinkedIdentityField(view_name= "accounthyperdetail", lookup_field ='pk' )
    class Meta:
        model = Money
        fields = ['edit', 'real_name', 'account_type', 'debt'] 
    

class AccountHyperLink(serializers.ModelSerializer):
    money = MoneySeializer(read_only = True)
    class Meta:
        model = Account
        fields = [ 'account_name', 'age', 'gender', 'created', 'moneyddd']
    