from django.http import HttpRequest
from django.shortcuts import render
from projects.models import Project


def project_index(request: HttpRequest):
    """
    renders html page containing all projects info
    Arguments:
        request (HttpRequest): request object
    """
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/project_index.html", context)


def project_detail(request: HttpRequest, pk: int):
    """
    renders html page for project
    Arguments:
        request (HttpRequest): request object
        pk (int): the primar key - id
    """
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "projects/project_detail.html", context)
