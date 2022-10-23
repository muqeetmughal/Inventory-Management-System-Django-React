from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# from api.serializers import ListUserSerializer
User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # user_dict = ListUserSerializer(user).data

        # token["user"] = user_dict

        token["permissions"] = list(user.get_all_permissions())

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        my_user = User.objects.filter(pk=self.user.id).first()
        if my_user:
            # use user serelizor or parse required fields
            data['user'] = my_user
            data['permissions'] = list(my_user.get_all_permissions())

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # you need to instantiate the serializer with the request data
        serializer = self.serializer_class(data=request.data)

        # you must call .is_valid() before accessing validated_data
        serializer.is_valid(raise_exception=True)

        # get access and refresh tokens to do what you like with
        access = serializer.validated_data.get("access", None)
        refresh = serializer.validated_data.get("refresh", None)
        user = serializer.validated_data.get("user", None)
        permissions = serializer.validated_data.get("permissions", None)

        # print(serializer.validated_data)

        # build your response and set cookie

        if access is not None:
            response = Response(
                {"access": access, "refresh": refresh, "user": UserSerializer(user).data, "permissions": permissions}, status=200)
            # response.set_cookie('refresh', refresh, httponly=True)
            return response

        return Response({"Error": "Something went wrong"}, status=400)


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)

        user_uid = decoded_payload['user_id']

        # print(user_uid)

        my_user = User.objects.filter(pk=user_uid).first()
        if my_user:
            # use user serelizor or parse required fields
            data['user'] = my_user
            data['permissions'] = list(my_user.get_all_permissions())

        return data


class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom Refresh token View
    """
    serializer_class = CustomTokenRefreshSerializer


    def post(self, request, *args, **kwargs):
        # you need to instantiate the serializer with the request data
        serializer = self.serializer_class(data=request.data)

        # you must call .is_valid() before accessing validated_data
        serializer.is_valid(raise_exception=True)

        # get access and refresh tokens to do what you like with
        access = serializer.validated_data.get("access", None)
        refresh = serializer.validated_data.get("refresh", None)
        user = serializer.validated_data.get("user", None)
        permissions = serializer.validated_data.get("permissions", None)

        # print(serializer.validated_data)

        # build your response and set cookie

        if access is not None:
            response = Response(
                {"access": access, "refresh": refresh, "user": UserSerializer(user).data, "permissions": permissions}, status=200)
            # response.set_cookie('refresh', refresh, httponly=True)
            return response

        return Response({"Error": "Something went wrong"}, status=400)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@ api_view(["GET"])
@ authentication_classes([JWTAuthentication])
@ permission_classes([IsAuthenticated])
def whoami(request):

    serializer = UserSerializer(request.user)
    return Response(serializer.data)
