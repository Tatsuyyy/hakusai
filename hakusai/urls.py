from django.urls import path

from hakusai.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]