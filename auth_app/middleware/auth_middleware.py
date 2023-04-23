from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect
from django.urls import reverse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        unlogin_views = (reverse('login'), reverse('registration'))
        if not request.user.is_authenticated and request.path not in unlogin_views:
            path = request.get_raw_uri()
            login_url = reverse('login')
            return redirect(login_url + '?next=' + path)

        return self.get_response(request)