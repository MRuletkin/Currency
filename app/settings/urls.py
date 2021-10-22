from currency.views import contact_us, rate_list

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list', rate_list),
    path('contactus/', contact_us)
]
