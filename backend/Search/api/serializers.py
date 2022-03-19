from rest_framework import serializers


class UserPublicData(serializers.Serializer):
    username = serializers.CharField(read_only=True)

