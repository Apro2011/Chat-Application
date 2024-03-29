from django.shortcuts import render
from users.serializers import UserSerializer
from users.models import MyUser as User
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET"])
def user_list(
    request,
):
    users = User.objects.all().order_by("username")
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data)
