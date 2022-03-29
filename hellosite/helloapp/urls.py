from django.urls import path
from sayhello.views import HelloWorldView

urlpatterns = [
    # helloapp/
    path('', HelloWorldView.as_view(), name='hello_world'),
]