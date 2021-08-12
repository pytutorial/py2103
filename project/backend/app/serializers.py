from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.serializers import CharField, IntegerField, DateTimeField
from .models import *
from rest_framework.validators import UniqueValidator

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            "category": {
                "error_messages": {
                    'null': 'Trường này không được bỏ trống.'
                }
            },
            "code": {
                "validators": [
                    UniqueValidator(queryset=Product.objects.all(), message='Mã sản phẩm đã tồn tại')
                ]
            },
            "price": {
                "error_messages": {
                    'invalid': 'Giá sản phẩm không hợp lệ.'
                }
            },
            "image":{
                "error_messages": {
                    'invalid': 'Ảnh sản phẩm không hợp lệ.'
                }
            }
        }

    def is_valid(self, raise_exception):
        try:
            return super().is_valid(raise_exception=raise_exception)
        except Exception as e:
            print(self.errors)
            raise e
    
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        
        if self.instance is not None:
            fields['image'].required = False        # Make image optional when update product

        return fields

    category_name = CharField(source='category.name', read_only=True)

class OrderInputSerializer(Serializer):
    qty = IntegerField()
    customerName = CharField()
    customerPhone = CharField()
    customerAddress = CharField()