from currency.models import Rate, Source

from import_export import resources


class RateResource(resources.ModelResource):
    class Meta:
        model = Rate


class SourceResource(resources.ModelResource):
    class Meta:
        model = Source
