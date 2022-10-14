from rest_framework import serializers
from shortener.models import ShortenedUrl
# from rest_framework.reverse import reverse


class ShortenedUrlSerializer(serializers.ModelSerializer):
    # short_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortenedUrl
        fields = ('long_url', 'code')
        lookup_field = 'code'

    # def get_short_url(self, obj):
    #     return reverse('api-shortener:shortened-detail',
    #                    args=[obj.code], request=self.context['request'])
