from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
 
    path('', lambda request: redirect('requisition/create/')),

    path('admin/', admin.site.urls),
    path('requisition/', include('requisition.urls')),
]



