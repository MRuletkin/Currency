from api import views

from django.urls import path

from rest_framework.routers import DefaultRouter

app_name = 'api'


router = DefaultRouter()
router.register('rates', views.RateViewSet,  basename='rate')
router.register('contactus', views.ContactUsViewSet,  basename='contactus')

urlpatterns = [
    path('sources/', views.SourceViewSet.as_view(), name='source')
]

urlpatterns += router.urls
