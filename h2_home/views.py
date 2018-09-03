from django.shortcuts import render, redirect, HttpResponse
from h2_home.models import UserInfo
import random


# Create your views here.
def index(request):
    context = {
        "title": '首页',
        "back": "back%d.jpg" % random.randint(1, 20)
    }
    return render(request, "h2_home/index.html", context)


def login(request):
    context = {
        "title": "登陆/注册"
    }
    response = render(request,'h2_home/login.html',context)
    name = "薛新岗".encode("utf-8").decode("latin-1")
    response.set_cookie("name",name)
    response.set_cookie("user","201553080210")
    return response


def home(request):
    user_info = request.COOKIES
    user_name = user_info.get("uid", None)
    user_id = user_info.get("user", None)
    if not all([user_id, user_name]):
        # return HttpResponse("请求失败，<a href='http://127.0.0.1:8000'>点击这里返回首页</a>")
        return redirect('/landing')
    user = UserInfo.objects.get(name=user_name, id=user_id)
    context = {
        "title": '%s的小世界' % user.name,
        "name": user.name,
        "id": user.id,
        "age": user.age,
        "gender": user.gender,
        "height": user.height,
        "email": user.email,
        "phone": user.phone,
        "qq": user.qq_howl,
        "back": "back%d.jpg" % random.randint(1, 20)
    }
    return render(request, 'h2_home/home.html', context)


def landing(request):
    context = {
        "title":"登陆"
    }
    return render(request,'h2_home/landing.html',context)


def register(request):
    return HttpResponse("注册页面")