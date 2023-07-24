from django.contrib import admin
from app.models import State,City,Hospital,Facility,Availability
from django.db.models.signals import post_save
from django.dispatch import receiver
# Register your models here.

@receiver(post_save, sender=Hospital)
def afterHospitalSave(signal, instance, **kwargs):
    facilities=Facility.objects.all()
    for f in facilities:
        availibilitys = Availability(hospital=instance , facility=f)
        availibilitys.save()

@receiver(post_save, sender=Facility)
def afterFacilitylSave(signal, instance, **kwargs):
    hospitals=Hospital.objects.all()
    for h in hospitals:
        availibilitys = Availability(hospital=h , facility=instance)
        availibilitys.save()

class facilityAdmin(admin.ModelAdmin):
    model=Facility
    list_display=['title']

class hospitalAdmin(admin.ModelAdmin):
    model=Hospital
    list_display=['name','phone','address','city']

class cityAdmin(admin.ModelAdmin):
    model=City
    list_display=['name','state']

class availabilityAdmin(admin.ModelAdmin):
    model=Availability
    list_display=['hospital','facility','total','available','updated_at']
    list_editable=['total','available']

    
admin.site.register(State)
admin.site.register(City,cityAdmin)
admin.site.register(Hospital,hospitalAdmin)
admin.site.register(Facility,facilityAdmin)
admin.site.register(Availability,availabilityAdmin)