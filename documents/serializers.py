from rest_framework import serializers

from documents.models import Doc, Picture


class DocSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('meta_user')

    def meta_user(self, instance):
        return {
            "username": instance.owner.username,
            "email": instance.owner.email
        }
    class Meta:
        model = Doc
        fields = '__all__'
        read_only_fields = ['owner']


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'
        read_only_fields = ['owner']
