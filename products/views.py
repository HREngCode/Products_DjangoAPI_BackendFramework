from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Products

@api_view(['GET'])
def products_list(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)











@api_view(['GET'])
def product_detail(request, pk):


    return Response('ok')