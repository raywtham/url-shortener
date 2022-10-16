from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.reverse import reverse
from shortener.models import ShortenedUrl


class ShortenedUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()
    long_url = serializers.CharField()

    class Meta:
        model = ShortenedUrl
        fields = ('long_url', 'short_url')
        lookup_field = 'code'

    def get_short_url(self, obj):
        return reverse('api-shortener:shortened-detail',
                       args=[obj.code], request=self.context['request'])

    def validate_long_url(self, value):
        # Add protocol prefix if not present
        protocols = ['http://', 'https://']
        prefix = [p for p in protocols if (p in value)]
        if not prefix:
            value = protocols[0] + value
        validate = URLValidator()
        try:
            validate(value)
        except ValidationError as e:
            raise serializers.ValidationError(e)
        return value
