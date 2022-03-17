from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    url = serializers.SerializerMethodField(read_only=True) # One way to do it is to use the get_url function

    edit_url = serializers.HyperlinkedIdentityField(view_name='product:product_update_view',lookup_field='pk') # Another way to do it

    class Meta:
        model = Product
        fields = ['url','edit_url','pk','title','description','price','sale_price','my_discount']

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