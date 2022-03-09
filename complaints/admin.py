from django.contrib import admin
from .models import Complainant,Complaint,Progress

# Register your models here.

admin.site.register(Complaint)
admin.site.register(Complainant)
admin.site.register(Progress)