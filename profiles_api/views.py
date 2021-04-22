from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

'''
APIviews vs Viewsets:

APIViews:
--API views are used when we need complex logic like (calling   other APIs or working with other files)
-- define fucntion for HTTPS
-- full control over logic
'''
class HelloApiView(APIView):
    '''TEST API VIEW'''
    
    #added seirializer class
    serializer_class = serializers.HelloSerializer
    
    
    
    def get(self,request,format=None):
        '''return a list of APIView Features'''
        an_apiview=[
        'Uses HTTP methods as fucntion(get,post,patch,put,delete)',
        'is similar to a traditional django view',
        'gives most control on logic',
        'is Mapped mannually to URLs',
        ]

        # can return list or dict in JSON
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        """create hello messsge wih our name"""
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"Hello {name}"
            return Response({"messsage":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
                )
            
    def put(self,request,pk=None):
        """Handle update an object,it replaces the object"""
        
        return Response({"method":"PUT"})
    
    def patch(self,request,pk=None):
        """Handle partial update of object,it updates object"""
        
        return Response({"method":"PATCH"})
        
    def delete(self,request,pk=None):
        """Deletes the obejct"""
        return Response({"method":"DELETE"})
        
        
        