from django.contrib import admin
from django.db.models import Count

from apps.visitors.models import Visitor, Event, Click


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_count']

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            event_count=Count('click')
        )

    def event_count(self, obj):
        return obj.event_count

    def regroup_by(self):
        return 'event'

    event_count.short_description = 'Event Clicked'


admin.site.register(Visitor)
admin.site.register(Event, EventAdmin)
admin.site.register(Click)
