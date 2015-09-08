from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe

from profiles.models import BaseProfile


@require_safe
def index(request):
    ctx = {}
    bps = BaseProfile.objects.all()
    ctx['bps'] = bps
    template_name = "profiles/front/index.html"
    return render(request, template_name, ctx)


@require_safe
def detail(request, b36id):
    ctx = {}
    bp = get_object_or_404(BaseProfile, b36id=b36id)
    ctx['bp'] = bp
    template_name = "profiles/front/detail.html"
    return render(request, template_name, ctx)
