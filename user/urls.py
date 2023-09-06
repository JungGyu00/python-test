from django.urls import path
from .views import signup, signin, signout


urlpatterns = [
    path('sign-up/', signup),
    path('sign-in/', signin),
    path('sign-out/', signout),
]
