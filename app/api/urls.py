from api import views

from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
from rest_framework.routers import DefaultRouter

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register('rates', views.RateViewSet,  basename='rate')
router.register('contactus', views.ContactUsViewSet,  basename='contactus')
router.register('sources', views.SourceViewSet, basename='source')

urlpatterns = [path('rates/latest/', views.LatestRatesView.as_view(), name='rates-latest')]

urlpatterns += router.urls
