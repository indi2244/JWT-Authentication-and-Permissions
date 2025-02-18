from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django .contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, SAFE_METHODS, BasePermission,IsAuthenticatedOrReadOnly
from .permissions import ReadOnly
from rest_framework import status
from .permissions import IsExampleDomainUser, IsAdminRole



class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(generics.CreateAPIView): 
    serializer_class= LoginSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args , **kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user= authenticate(username=username, password= password)

        if user is not None:
            refresh=RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data
            })
        else:
            return Response({'detail':"Invalid credential"}, status= 401)


class DashboardView(APIView):
    permission_classes=(IsAdminUser,)
    def get(self ,request):
        user=request.user
        user_serializer=UserSerializer(user)
        return Response({
            "message":"Welcome to dashboard",
            'user':user_serializer.data
        })
    
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        
        try:
            refresh_token = request.data.get["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class SpecialView(APIView):
    permission_classes = [IsAuthenticated, IsExampleDomainUser]

    def get(self, request):
        return Response({"message": "You have special access!"})

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get(self, request):
        return Response({"message": "Only admin users can see this!"})
    

class ExampleView(APIView):
    permission_classes = [IsAuthenticated , ReadOnly]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
    
    #def get_address():
        
