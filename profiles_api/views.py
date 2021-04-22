from rest_framework.views import APIView
from rest_framework.response import Response


'''
APIviews vs Viewsets:

APIViews:
--API views are used when we need complex logic like (calling   other APIs or working with other files)
-- define fucntion for HTTPS
-- full control over logic
'''
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

        # can return list or dict in JSON
        return Response({'message':'hello','an_apiview':an_apiview})
