from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model=Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, required=False)
    class Meta:
        model=Order
        fields = [
            'order_id',
            'user',
            'created_at',
            'status',
            'products'
        ]
        read_only_fields = ["user"]
    
    def create(self, validated_data):
        products = validated_data.pop("products")
        order = Order.objects.create(**validated_data)
        order_items = []
        for prod in products:
            product = Product.objects.get(id=prod['id'])
            order_items.append(OrderItem(order=order, product=product, quantity=5))
        
        OrderItem.objects.bulk_create(order_items)

        return order


