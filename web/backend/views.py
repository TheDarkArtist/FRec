from rest_framework.views import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def root_endpoint(request):
    return Response()