from django.urls import path
from profiles_api import views


urlpatterns=[
path('hello-view/',views.HelloApiView.as_view()), #as_view() is used to convert APIView to a standard view that can be rendered
]
