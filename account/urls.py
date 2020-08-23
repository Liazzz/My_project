from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegisterView, SignView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='sign-up'),
    path('login/', SignView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]