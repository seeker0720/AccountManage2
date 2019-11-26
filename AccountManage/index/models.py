from django.db import models

# Create your models here.
class AccountInfo(models.Model):
    user_name = models.CharField('用户名', max_length=50)
    user_password = models.CharField('用户密码', max_length=100)
    user_type = models.CharField('用户类型',max_length=50)
    remarks = models.TextField('备注')

    class Meta:
        verbose_name = '账号信息'
        verbose_name_plural = '账号信息'
