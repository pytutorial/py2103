from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField, ImageField
from .models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        
        if self.instance is not None:
            fields['image'].required = False        # Make image optional when update product

        return fields

    category_name = CharField(source='category.name', read_only=True)
