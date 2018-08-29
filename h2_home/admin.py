from django.contrib import admin
from .models import UserInfo, LabelInfo, ObjInfo

# Register your models here.

admin.site.site_header = "郑工15市2后台管理"
admin.site.site_title = "市2后台管理"


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    empty_value_display = "none"
    list_display = ("id", "name", "age", "gender", "height", "email", "phone", "qq_howl", "single", "is_delete")
    exclude = ("value1", "value2", "value3")


@admin.register(LabelInfo)
class LabelInfoAdmin(admin.ModelAdmin):
    empty_value_display = "none"
    list_display = ("title", "count")


@admin.register(ObjInfo)
class ObjInfoAdmin(admin.ModelAdmin):
    empty_value_display = "none"
    list_display = ("user_id", "age", "name", "gender", "height", "weight", "email", "phone", "qq_howl")
