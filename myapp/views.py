from django.shortcuts import render

def custom_page_not_found(request, exception=None):
    return render(request, '404.html', status=404)

def custom_error_view(request, exception=None):
    return render(request, '500.html', status=500)

def custom_bad_request_view(request, exception=None):
    return render(request, '400.html', status=400)