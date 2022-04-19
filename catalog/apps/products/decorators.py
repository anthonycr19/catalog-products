from django.http import Http404
from rest_framework import exceptions
from .models import Product, LogUserReadProduct


def user_read_porduct(view_method):
    def wrapper(*args, **kwargs):
        if not args:
            raise exceptions.ValidationError('Error de request')

        view = args[0]
        request = args[1]
        args = args[2:]

        if request.user.is_anonymous:
            try:
                product = Product.objects.get(pk=kwargs.get('pk'))
                LogUserReadProduct.objects.create(product=product)
            except Product.DoesNotExist:
                raise Http404

        return view_method(view, request, *args, **kwargs)
    return wrapper
