from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title
from apiapp.serializers import UserPablicSerializers

class ProductSerializers(serializers.ModelSerializer):
    user = UserPablicSerializers(read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(view_name='product-edit', lookup_field='pk')
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    #title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
             'user', # user_id
             'url',
			'edit_url',    
			'id',
			'title',
			'content',
			'price',
			'get_descount',
		]
    def validate_title(self, value):
        qs = Product.objects.filter(title__exact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is alredy product name")   
        return value

    # def get_edit_url(self, obj):
    #         request = self.context.get('request') #self.request
    #         if request is None:
    #              return None
    #         return reverse("product-edit", kwargs={'pk':obj.pk}, request=request)