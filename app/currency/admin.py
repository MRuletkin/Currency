from currency.models import ContactUs, Rate, Source
from currency.resources import RateResource, SourceResource

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from rangefilter.filters import DateTimeRangeFilter


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'message',
        'created',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ContactUs, ContactUsAdmin)


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )
    list_filter = (
        'type',
        ('created', DateTimeRangeFilter),
    )
    search_fields = (
        'buy',
        'sale',
        'source',
    )
    readonly_fields = (
        'buy',
        'sale',
    )


admin.site.register(Rate, RateAdmin)


class SourceAdmin(admin.ModelAdmin):
    resource_class = SourceResource
    list_display = (
        'source_url',
        'name',
        'created',
    )
    list_filter = (
        'name',
        ('created', DateTimeRangeFilter),
    )
    search_fields = (
        'source_url',
        'name',
        'created',
    )
    readonly_fields = (
        'name',
        'created',
    )


admin.site.register(Source, SourceAdmin)
