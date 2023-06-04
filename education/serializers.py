from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(unique=True, null=True)
    address = serializers.CharField(max_length=255)
    birthday = serializers.DateField()