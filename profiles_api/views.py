from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''TEST API VIEW'''

    def get(self,request,format=None):
        '''return a list of APIView Features'''
        an_apiview=[
        'Uses HTTP methods as fucntion(get,post,patch,put,delete)',
        'is similar to a traditional django view',
        'gives most control on logic',
        'is Mapped mannually to URLs',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})
