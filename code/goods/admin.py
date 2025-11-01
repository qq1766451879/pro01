from django.contrib import admin
from .models import UserInformation
from django.utils.html import format_html

@admin.register(UserInformation)#流量商IP
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('id','StockCode','PhoneNumber','create_time')
    list_per_page = 50
    ordering = ('-create_time',)
    search_fields = ['StockCode','PhoneNumber']  # 搜索