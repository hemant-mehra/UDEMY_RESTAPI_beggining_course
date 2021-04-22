from rest_framework import serializers
from profiles_api import models

# serializers for apiviewn and viewsets
class HelloSerializer(serializers.Serializer):
    """
    Serializes the name field for testing our APIviews
    workds similers to django formsin rest API (apply validation as well)
    
    """
    
    name=serializers.CharField(max_length=10)
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer gor usermodel"""
    class Meta:
         model=models.UserProfile
         fields=("id","email","name","password")
         extra_kwargs={
             "password":{
                 "write_only":True, #so that we use it only to create not retirieve
                 "style":{"input_type":"password"} #os that when we type passwod it not shown on display  ***
             }
         }
         
    def create(self,validated_data):
        """overwrite create function of modelserializers with our own function"""
        # this create user fucntion is wht we created in model userprofilemanager
        user=models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"]
            
        )
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)