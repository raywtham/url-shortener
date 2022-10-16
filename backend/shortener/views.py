from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from shortener.models import ShortenedUrl
from shortener.serializers import ShortenedUrlSerializer
from hashids import Hashids
from rest_framework.response import Response
from django.shortcuts import redirect

hashids = Hashids(salt="alpharius", min_length=6)


class ShortenedUrlRetrieveView(GenericAPIView):
    queryset = ShortenedUrl.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ShortenedUrlSerializer
    lookup_field = 'code'

    def get(self, request, code, format=None):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return redirect(serializer.data['long_url'])


class ShortenedUrlCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ShortenedUrlSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        code = hashids.encode(obj.id)
        obj.code = code
        obj.save()
