from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework import status
from .models import Product


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request):
        return Response({"status":"true"}, status=status.HTTP_202_ACCEPTED)
