from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validations import validate_title
from api.serializers import UserPublicData

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)

    url = serializers.SerializerMethodField(read_only=True) # One way to do it is to use the get_url function

    edit_url = serializers.HyperlinkedIdentityField(view_name='product:product_update_view',lookup_field='pk') # Another way to do it


    title = serializers.CharField(validators=[validate_title])
    # name = serializers.CharField(source='title', read_only=True)

    # user = UserPublicData(read_only=True)
    # email = serializers.EmailField(source='user.email',read_only=True)

    class Meta:
        model = Product
        fields = [
            # 'user',
            'url',
            'edit_url',
            # 'email',
            'pk',
            'title',
            'description',
            'price',
            'sale_price',
            'my_discount',
            # 'my_user_data'
        ]

    # def get_my_user_data(self, obj):
    #     return {
    #         "username": obj.user.username
    #     }

    # def validate_title(self,value):
    #     qs = Product.objects.filter(title__iexact=value)

    #     if qs.exists():
    #         raise serializers.ValidationError(f" {value} This title has already been used")
    #     return value


    # def create(self,validated_data):
    #     validated_data.pop('email')
    #     obj = super().create(validated_data)

    #     return obj

    # def update(self,instance,validated_data):
    #     email = validated_data.pop('email')
    #     instance.title = validated_data.get('title')
    #     instance.description = validated_data.get('description')
    #     instance.price = validated_data.get('price')
    #     return super().update(instance,validated_data)

    # url way to do it
    def get_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product:product_view',kwargs={'pk':obj.pk},request=request)   


    def get_my_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None