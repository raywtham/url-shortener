from django.urls import path
from shortener.views import ShortenedUrlCreateView, ShortenedUrlRetrieveView


urlpatterns = [
    path("shortenedurls/", ShortenedUrlCreateView.as_view(), name="shortened-create"),
    path("<str:code>", ShortenedUrlRetrieveView.as_view(), name="shortened-detail"),
]
