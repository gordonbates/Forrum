from django.urls import path, include
from .views import signup, signin
# from threads.views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
]
