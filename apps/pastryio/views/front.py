from django.shortcuts import render


def index(request):
    ctx = {}
    template_name = "pastryio/front/index.html"
    return render(request, template_name, ctx)
