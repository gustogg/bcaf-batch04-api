from rest_framework import serializers

from documents.models import Doc, Picture


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'
        read_only_fields = ['owner']


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'
        read_only_fields = ['owner']
