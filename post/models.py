from django.db import models

# Create your models here.
# 车间类别
class Workshop(models.Model):
    #车间ID
    #混料车间=1
    #吹膜车间=2
    #印刷车间=3
    #制袋A车间=4
    #知道B车间=5    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "车间"
        verbose_name_plural = "车间"
        

        
# 班次类别 
class Workshift(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "班次"
        verbose_name_plural = "班次"
    #班次ID
    #早班=1，晚班=2，中班=3
    
#数据信息
class Post(models.Model):
    
    #填写日期
    create_time = models.DateTimeField(auto_now_add=True)
    #日期
    date = models.DateField(default=0)
    
    #车间
    workshop = models.ForeignKey(Workshop)
    #班次
    workshift = models.ForeignKey(Workshift)
    #机号
    machine_num = models.CharField(max_length=100, blank=True)
    #订单号
    order_num = models.CharField(max_length=100, blank=True)
    #生产数量
    product_num = models.FloatField(blank=True, default=0)
    #生产单位数
    product_units = models.IntegerField(blank=True, default=0)
    #废料数
    waste_num = models.FloatField(blank=True, default=0)
    #操作员
    operator = models.CharField(max_length=100, blank=True)
    #备注
    remarks = models.CharField(max_length=100, blank=True)
    
    class Meta:
        ordering = ["-create_time"]
        verbose_name = "生产数据"
        verbose_name_plural = "生产数据"