from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from h2_home.models import UserInfo
from django.conf import settings


class AuthMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.path in settings.NEED_LOGIN:
            print(request.path)
            print("aaaaa")

