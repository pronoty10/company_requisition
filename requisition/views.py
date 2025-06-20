from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RequisitionForm
from .models import Requisition

@login_required
def create_requisition(request):
    form = RequisitionForm(request.POST or None)
    if form.is_valid():
        req = form.save(commit=False)
        req.employee = request.user
        req.save()
        return redirect('my_requisitions')
    return render(request, 'requisition/create.html', {'form': form})

@login_required
def my_requisitions(request):
    requisitions = Requisition.objects.filter(employee=request.user)
    return render(request, 'requisition/my_list.html', {'requisitions': requisitions})

@user_passes_test(lambda u: u.is_superuser)
def all_requisitions(request):
    requisitions = Requisition.objects.all()
    return render(request, 'requisition/all_list.html', {'requisitions': requisitions})

@user_passes_test(lambda u: u.is_superuser)
def update_status(request, req_id, status):
    requisition = Requisition.objects.get(id=req_id)
    requisition.status = status
    requisition.save()
    return redirect('all_requisitions')
