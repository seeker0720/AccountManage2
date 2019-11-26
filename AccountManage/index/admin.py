from django.contrib import admin
from .models import AccountInfo
from django.utils.html import format_html 
from django.urls import reverse
# Register your models here.

admin.site.site_title = 'AccountManage管理'
admin.site.site_header = 'AccountManage'

@admin.register(AccountInfo)
class AccountInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'link_to_edit','user_type', 'remarks' ]
    # 设置搜索字段
    search_fields = ['id', 'user_name', 'user_type']
    # 设置过滤器
    list_filter = ['id', 'user_name', 'user_type']
    # 设置id字段排序
    ordering = ['id']
    def link_to_edit(self, obj): 
        # 主要代码 
        info = (obj._meta.app_label, obj._meta.model_name) 
        link = reverse('admin:%s_%s_change' % info, args=(obj.id,)) 
        return format_html(u'<a href="%s" title="查看">%s</a>' % (link, '●●●●●●●●'))   
    # 设置 link_to_edit 显示的名称 
    link_to_edit.short_description = '用户密码'
