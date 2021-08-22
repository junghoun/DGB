# python 객체, queryset 복잡한 객체 json 형태로 변환해주는 어뎁터 역할
from rest_framework import serializers

from .models import Advertising, User, Account

# ex)
# from .models import User, TableName
# 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'userName', 'accCnt', 'cash', 'phoneNumber')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('aId', 'accNum', 'password', 'balance', 'ownerId', 'ownerName', 'title', 'card')


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = ('aId', 'aName', 'title', 'contents', 'img')