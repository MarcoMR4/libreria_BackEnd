from rest_framework import viewsets
from .serializer import UserSerializer, BookSerializer
from .models import Users, Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


# Registro de usuarios para tabla users, esta es para crear una url personalizada 
class UserRegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def create_users(self, serializer):
        if not self.request.data['password'].startswith(('pbkdf2_sha256$', 'bcrypt')):
            user = serializer.save()
            user.set_password(self.request.data['password'])
            user.save()
        else:
            serializer.save()



# Vista con los metodos necesarios para crud en tabla libros con ayuda de serializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Login de users 
class TokenObtainView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Users.objects.get(email=email)
            pass1 = Users.objects.get(password=password)
        except:
            user = None
            pass1 = None

        if user and pass1:
            refresh = RefreshToken.for_user(user)
            data = {
                'message' : 'Welcome! here is your access token c:',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)