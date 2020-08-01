from rest_framework import serializers
from django.contrib.auth.models import User
import django.contrib.auth.password_validation as validators
from .models import Product
from django.core import exceptions
from rest_framework_jwt.settings import api_settings


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id','username','email', 'password','token')
        extra_kwargs = {'password': {'write_only': True}}
    """
    token = serializers.SerializerMethodField()
    esto significa que este campo personalizado va a depender de un metodo el cual tiene que llevar su nombre mmas el get
    de la siguiente manera get_campo y asi se relaciona un campo con un metodo que tendra que retornar un valor

    """

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        print(obj.email)
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
