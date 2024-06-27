# apps/middleware.py
from django.http import HttpResponseForbidden

class UgelRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated and user.role != 'admin_sistema':
            if 'ugel' in request.GET and request.GET['ugel'] != str(user.ugel.id):
                return HttpResponseForbidden("No tiene permiso para acceder a esta UGEL.")
        response = self.get_response(request)
        return response
