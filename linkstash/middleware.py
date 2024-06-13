from django.utils import timezone
import pytz



class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_timezone = request.session.get('user_timezone')
        if user_timezone:
            timezone.activate(pytz.timezone(user_timezone))
        else:
            timezone.deactivate()

        return self.get_response(request)
        