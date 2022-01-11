from api import views

from rest_framework.routers import DefaultRouter

app_name = 'api'


router = DefaultRouter()
router.register('rates', views.RateViewSet,  basename='rate')
router.register('contactus', views.ContactUsViewSet,  basename='contactus')
router.register('sources', views.SourceViewSet, basename='source')

urlpatterns = []

urlpatterns += router.urls
