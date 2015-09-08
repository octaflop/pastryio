from django.shortcuts import render
from django.views.decorators.http import require_safe


@require_safe
def index(request):
    ctx = {}
    template_name = "profiles/front/index.html"
    return render(request, template_name, ctx)
