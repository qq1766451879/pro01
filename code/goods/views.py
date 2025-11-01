from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render
from .serializers import GoodsSerializer
from .models import UserInformation
from rest_framework import status  # 导入状态码常量
def Index_template(request):
    return render(request, 'index.html')

class GoodsViewSet(viewsets.ModelViewSet):
    """商品视图集：自动提供列表、详情、创建、更新、删除接口"""
    queryset = UserInformation.objects.all()  # 数据源
    serializer_class = GoodsSerializer  # 关联序列化器


class GoodsCreateView(APIView):
    """
    使用APIView创建新商品
    接收POST请求，验证数据后保存到数据库
    """

    def post(self, request):
        # 1. 获取前端提交的数据（request.data自动解析JSON/表单数据）
        # 2. 用序列化器验证数据
        serializer = GoodsSerializer(data=request.data)

        # 3. 验证通过：保存数据到数据库
        if serializer.is_valid():
            # save()方法会自动创建Goods实例（内部调用Goods.objects.create()）
            goods = serializer.save()
            # 返回创建成功的商品数据（包含自动生成的id和create_time）
            return Response(
                data={
                    'msg': '正常に作成されました',
                    'data': {
                        'id': goods.id,
                        'create_time': goods.create_time
                    }
                },
                status=status.HTTP_201_CREATED  # 201表示资源创建成功
            )

        # 4. 验证失败：返回错误信息
        return Response(
            data={
                'msg': '作成に失敗しました',
                'errors': serializer.errors  # 错误详情（如"价格不能小于0"）
            },
            status=status.HTTP_400_BAD_REQUEST  # 400表示请求数据错误
        )