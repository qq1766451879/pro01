from django.db import models

class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    class Meta:
        abstract=True


class UserInformation(BaseModel):
    PhoneNumber = models.CharField(max_length=100,verbose_name="电话")
    StockCode = models.CharField(max_length=100,verbose_name="股票代码")
    Remark = models.CharField(max_length=255,verbose_name="备注",null=True, blank=True)
    class Meta:
        db_table='UserInformation'
        verbose_name = "提交数据"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.pk)