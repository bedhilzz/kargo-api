from django.contrib import admin

from .models import Job, Bid, Shipper, Transporter

admin.site.register(Job)
admin.site.register(Bid)
admin.site.register(Shipper)
admin.site.register(Transporter)