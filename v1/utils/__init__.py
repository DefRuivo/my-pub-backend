from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets


class BaseViewSet(
    viewsets.ModelViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class BaseSingleSet(
    viewsets.ModelViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
