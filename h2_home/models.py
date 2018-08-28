from django.db import models


# Create your models here.
class UserInfo(models.Model):
    id = models.BigIntegerField(unique=True,primary_key=True)
    passwrod = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=30, default=u"未命名")
    age = models.IntegerField(default=0)
    gender = models.BooleanField(default=True)
    height = models.IntegerField(default=0)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    qq_howl = models.CharField(max_length=30)
    # user_id = models.BigIntegerField(unique=True)
    image = models.ImageField()
    single = models.BooleanField(default=False)
    value1 = models.CharField(max_length=30)
    value2 = models.CharField(max_length=30)
    value3 = models.CharField(max_length=30)
    is_delete = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "同学"
    def __str__(self):
        return "%d %s " % (self.id,self.name)


class LabelInfo(models.Model):
    title = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "个性标签"

    def __str__(self):
        return '%s' % self.title


class ObjInfo(models.Model):
    user_id = models.BigIntegerField(default=0)
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    gender = models.BooleanField(default=True)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    qq_howl = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "对象"
    def __str__(self):
        return '%s  %s' % (self.user_id, self.name)
