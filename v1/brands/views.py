from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from .serializers import BrandSerializer
from core.models import Brand


class BrandViewSet(
    viewsets.ModelViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    serializer_class = BrandSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Brand.objects.all()


class BrandSingleSet(
    viewsets.ModelViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin
):
    serializer_class = BrandSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Brand.objects.all()
