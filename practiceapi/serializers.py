from rest_framework import serializers


class Detailserializers(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    fname = serializers.CharField(max_length=40)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=40)
    city = serializers.CharField(max_length=40)