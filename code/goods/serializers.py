# goods/serializers.py
from rest_framework import serializers
from .models import UserInformation

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation  # 关联模型
        fields = "__all__"  # 序列化所有字段（或指定字段如['id', 'name']）