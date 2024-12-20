from django.http import HttpRequest
from django.shortcuts import render


def home(request: HttpRequest):
    """
    Renders a html page
    Args:
        request (HttpRequest): a django request object
    Returns:
        html page render
    """
    return render(request, "pages/home.html", {})
