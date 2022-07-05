from rest_framework import viewsets, generics
from rmc.models import User, Professional, Session
from rmc.serializer import ProfessionalSerializer, UserSerializer, SessionSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ProfessionalViewSet(viewsets.ModelViewSet):
    """Exibindo todos os profissionais"""
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SessionViewSet(viewsets.ModelViewSet):
    """Listando todas as sessões"""
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)