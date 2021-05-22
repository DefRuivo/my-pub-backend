from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Product, Brand, ProductItem, User


class TearDownView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        product_items = ProductItem.objects.all()
        products = Product.objects.all()
        brands = Brand.objects.all()
        users = User.objects.all()

        response = {
            "ProductItem": product_items.count(),
            "Product": products.count(),
            "Brand": brands.count(),
            "User": users.count(),
        }

        product_items.delete()
        products.delete()
        brands.delete()
        users.delete()

        return Response(response, status=status.HTTP_200_OK)


class SetUpView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        user_admin, _ = User.objects.get_or_create(
            **{
                "email": request.data["admin"]["email"],
                "first_name": request.data["admin"]["first_name"],
                "last_name": request.data["admin"]["first_name"],
                "is_superuser": True,
                "is_active": True,
                "is_staff": True,
            }
        )
        user_admin.set_password(request.data["admin"]["password"])
        user_admin.save()

        user_common, _ = User.objects.get_or_create(
            **{
                "email": request.data["common"]["email"],
                "first_name": request.data["common"]["first_name"],
                "last_name": request.data["common"]["first_name"],
                "is_superuser": False,
                "is_active": True,
                "is_staff": False,
            }
        )
        user_common.set_password(request.data["common"]["password"])
        user_common.save()

        response = {"admin": user_admin.serialize, "common": user_common.serialize}
        return Response(response, status=status.HTTP_201_CREATED)
