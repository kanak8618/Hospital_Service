from django.shortcuts import render
from django.http.response import HttpResponse
from  app.models import Facility,State,City,Hospital,Availability
from django.views import generic
# Create your views here.

class HospitalDetailView(generic.DetailView):
    model=Hospital

def home(request):
    selected_state_id=request.GET.get('state')
    selected_city_id=request.GET.get('city')
    selected_facility_id=request.GET.get('facility')
    facilitys = Facility.objects.all().order_by('pk')
    if selected_state_id:
        citys=City.objects.filter(state=selected_state_id)
    else:
        citys=City.objects.all()
   
    states=State.objects.all()
    hospitals=Hospital.objects.all()

    if selected_city_id:
        hospitals = hospitals.filter(city=City(pk=selected_city_id))

    if selected_facility_id:
        availabilitys=Availability.objects.all()
        if selected_city_id:
            availabilitys = availabilitys.filter(hospital__city=City(pk=selected_city_id))
       
        availabilitys = availabilitys.filter(facility=Facility(pk=selected_facility_id), available__gt=0)
       
        hospitals=[]
        for avl in availabilitys:
            hospitals.append(avl.hospital)

    context={
        'facilitys':facilitys,
        'citys':citys,
        'states':states,
        'hospitals':hospitals,
        'selected_state_id':selected_state_id,
        'selected_city_id':selected_city_id,
        'selected_facility_id':selected_facility_id
    }
    return render(request,template_name='app/index.html',context=context)