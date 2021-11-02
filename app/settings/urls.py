from currency.views import (
    contact_us, rate_create,
    rate_list, source_create,
    source_delete, source_details,
    source_list, source_update
)

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/list', rate_list),
    path('contactus/', contact_us),
    path('source/list/', source_list),
    path('rate/create/', rate_create),
    path('source/create/', source_create),
    path('source/update/<int:pk>/', source_update),
    path('source/delete/<int:pk>/', source_delete),
    path('source/details/<int:pk>/', source_details),
]
