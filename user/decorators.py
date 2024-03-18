from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse

def customer_test_function(user):
    if user.is_customer:
        return True
    return False

def adm_test_function(user):
    if user.is_adm:
        return True
    return False 

def adm_access_only(message_to_deliver = "No estas autorizado para acceder a la pagina de admin, logeate como admin"):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not adm_test_function(request.user):
                messages.error(request,message_to_deliver)
                return redirect("login")
            return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator
