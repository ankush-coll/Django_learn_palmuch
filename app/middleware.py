import time
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect

class AutoLogoutMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:
            current_time = time.time()
            last_activity = request.session.get('last_activity')

            if last_activity:
                if current_time - last_activity > 300:   # 300 seconds = 5 minutes
                    logout(request)
                    return redirect('login')  # redirect to login page

            request.session['last_activity'] = current_time

        response = self.get_response(request)
        return response