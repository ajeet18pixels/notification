from django.shortcuts import render


def error_404_view(request, exception):
    return render(request, 'authentication/404.html', status=404)