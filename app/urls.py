from django.contrib import admin
from django.urls import path
from app.views import home,HospitalDetailView

urlpatterns = [
    path('',home,name='homepage'),
    path('hospital/<int:pk>',HospitalDetailView.as_view(), name='hospital_detail')
]