from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, filters, generics, permissions
from users.models import NewUser


class CustomUserCreate(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class BlacklistTokenUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer
    queryset = NewUser.objects.all()

    def get(self, request, *args, **kwargs):
        user_count = self.get_queryset().count()
        data = {
            'user_count': user_count,
        }
        return Response(data)

    