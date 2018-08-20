from django.contrib import admin

from callapi.models import CallStart, CallEnd, CallRecord, PhoneBill



@admin.register(CallStart)
class CallStartAdmin(admin.ModelAdmin):
    pass

@admin.register(CallEnd)
class CallEndAdmin(admin.ModelAdmin):
    pass


@admin.register(CallRecord)
class CallRecordAdmin(admin.ModelAdmin):
    pass

@admin.register(PhoneBill)
class PhoneBillAdmin(admin.ModelAdmin):
    pass