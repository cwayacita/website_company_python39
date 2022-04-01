from django.core.exceptions import PermissionDenied

def user_is_webscraping(function):
    def wrap(request, *args, **kwargs):
        if request.user.first_name == 'webscraping' or request.user.first_name == '' :
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_is_QC_Spain(function):
    def wrap(request, *args, **kwargs):
        if request.user.first_name == 'QC_spain' or request.user.first_name == '' :
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap