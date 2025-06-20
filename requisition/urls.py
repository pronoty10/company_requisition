from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_requisition, name='create_requisition'),
    path('my/', views.my_requisitions, name='my_requisitions'),
    path('admin/all/', views.all_requisitions, name='all_requisitions'),
    path('admin/update/<int:req_id>/<str:status>/', views.update_status, name='update_status'),
]
