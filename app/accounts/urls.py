from accounts import views
from accounts.views import ProfileView

from django.urls import path

app_name = 'accounts'


urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('activate/<uuid:username>/', views.UserActivateView.as_view(), name='activate'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
