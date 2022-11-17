from django.contrib import admin
from .models import TrackingId
from .models import Summary
from .models import PackageProgress
from .models import SendersInfo
from .models import ReceiversInfo
from .models import ContactInfo


admin.site.register(TrackingId)
admin.site.register(ContactInfo)
admin.site.register(ReceiversInfo)
admin.site.register(SendersInfo)
admin.site.register(PackageProgress)
admin.site.register(Summary)