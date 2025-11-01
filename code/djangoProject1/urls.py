"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include  # 需导入include
from goods import views
from django.views.static import serve  # 导入处理静态文件的serve视图
from django.conf import settings  # 导入settings，获取静态文件路径配置
from rest_framework.routers import DefaultRouter  # 导入DRF路由器
from goods import views
from goods.views import GoodsViewSet  # 导入视图集
from goods.views import GoodsCreateView  # 导入创建商品的视图

# 1. 初始化DRF路由器
router = DefaultRouter()
# 2. 注册视图集：第一个参数是路由前缀，第二个是视图集
router.register(r'goods', GoodsViewSet)  # 生成的路由如 /goods/（列表）、/goods/1/（详情）等

urlpatterns = [
    path('admin123pwd/', admin.site.urls),
    #re_path(r'^.*$', views.Index_template, name='Index_template'),
# 2. 新增：静态文件路由（匹配/static/开头的所有请求）

    path('', views.Index_template, name='Index_template'),
# 3. 引入DRF自动生成的路由（路径前缀为/api/，可自定义）
#     path('api_mydata/', include(router.urls)),
path('api/submit-jaxa/', GoodsCreateView.as_view(), name='goods_create'),
]
