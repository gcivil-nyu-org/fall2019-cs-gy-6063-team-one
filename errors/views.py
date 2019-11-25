from django.shortcuts import render


def forbidden(request, exception=None):
    context = {"code": 403}
    return render(request, "errors/errors.html", context=context)


def not_found(request, exception=None):
    context = {"code": 404}
    return render(request, "errors/errors.html", context=context)


def bad_request(request, exception=None):
    context = {"code": 400}
    return render(request, "errors/errors.html", context=context)


def internal_error(request, exception=None):
    context = {"code": 500}
    return render(request, "errors/errors.html", context=context)
