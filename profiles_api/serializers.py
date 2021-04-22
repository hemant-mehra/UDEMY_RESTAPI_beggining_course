from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """
    Serializes the name field for testing our APIviews
    workds similers to django formsin rest API (apply validation as well)
    
    """
    
    name=serializers.CharField(max_length=10)
    
    