from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Type, Department


@login_required()
def download(request, department_id=None):
    types = Type.objects.all().order_by('id').prefetch_related()
    departments = Department.objects.all().order_by('name')
    context = {
        'types': types,
        'departments': departments,
    }
    if department_id is not None:
        context['department_searching'] = departments.get(id=department_id)

    return render(request, 'download_center/download.html', context)
