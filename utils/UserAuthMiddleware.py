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
            userinfo = request.COOKIES
            uid = userinfo.get("uid", None)
            uname = userinfo.get("user", None)
            if all([uid, uname]):
                if redis_db.get(uname) is not None:
                    print(redis_db.get(uname))
                    print("**********************************************")
                else:
                    return redirect("/landing")
            else:
                request.session["user_next"] = request.path
                return redirect("/landing")
