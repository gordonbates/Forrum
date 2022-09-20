from django.urls import path, include
from threads.views import signup
# from threads.views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
]
