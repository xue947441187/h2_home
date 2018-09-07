import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from h2_home.models import UserInfo
from django.conf import settings

from untitled.settings import redis_db


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # print(request.path)
        if request.path in settings.NEED_LOGIN:
            info = request.COOKIES
            uid = info.get("uid",None)
            uname = info.get("user",None)
            if not all([uid,uname]) and redis_db.get(uname) == uid:
                request.session["next"] = request.path
                return HttpResponseRedirect("/landing",request)

