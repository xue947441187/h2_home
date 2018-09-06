import re

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
import uuid
from h2_home.models import UserInfo
import random


# Create your views here.
from untitled.settings import redis_db


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
    response = render(request, 'h2_home/login.html', context)
    name = "薛新岗".encode("utf-8").decode("latin-1")
    response.set_cookie("name", name)
    response.set_cookie("user", "201553080210")
    return response


def home(request):
    user_info = request.COOKIES

    user_name = user_info.get("uid", None)
    user_id = user_info.get("user", None)
    if not all([user_id, user_name]):
        pass
        # # return HttpResponse("请求失败，<a href='http://127.0.0.1:8000'>点击这里返回首页</a>")
        # return redirect('/landing')
    user = UserInfo.objects.get(id=user_id)
    context = {
        "title": '%s的小世界' % user.name,
        "back": "back%d.jpg" % random.randint(1, 20),
        "users": {
                  "name": user.name,
                  "id": user.id,
                  "age": user.age,
                  "gender": user.gender,
                  "height": user.height,
                  "email": user.email,
                  "phone": user.phone,
                  "qq": user.qq_howl, },

    }
    return render(request, 'h2_home/home.html', context)


def landing(request):
    user = request.POST
    name = user.get("username")
    password = user.get("userpassword")
    context = {
        "title": "登陆"
    }
    if not all([name, password]):
        return render(request, 'h2_home/landing.html', context)
    re_au = re.match(r"^.*?@(163|qq)\.com$", name)
    if re_au:
        try:
            ret = UserInfo.objects.get(email=name)
        except Exception as e:
            print(e)
    else:
        if len(name) == 12:
            try:
                ret = UserInfo.objects.get(id=int(name))
            except Exception as e:
                print(e)
    if not (ret.passwrod == password):
        context["error"] = "密码错误"
        return render(request, "h2_home/landing.html", context)
    uid = uuid.uuid5(uuid.NAMESPACE_DNS, name)
    context["err"] = 0
    context["next"] = request.session["user_next"] if request.session["user_next"] is not None else "/"
    response = JsonResponse(context)
    redis_db.set(name, uid,ex=1*24*60*60)
    response.set_cookie("uid", uid)
    response.set_cookie('user', ret.id)
    return response


def register(request):
    context = {
        "title": "注册页面"
    }

    return render(request, 'h2_home/register.html', context)


class SqlDB(View):
    def get(self, request):
        return HttpResponse("get结果")

    def post(self, request):
        info = request.POST
        tag = info.get("tag")
        context = {}
        if tag == 0:
            """查询注册信息看用户名是否被注册"""
            try:
                user = UserInfo.objects.get(name=info.get("username"), email=info.get("email"))
            except Exception as e:
                user = 0
            if user == 0:
                context["err"] = 0
                return JsonResponse(context)
            else:
                context["err"] = 1
                return JsonResponse(context)

    def delete(self, request):
        return HttpResponse("delete结果")

    def put(self, request):
        return HttpResponse("put结果")
