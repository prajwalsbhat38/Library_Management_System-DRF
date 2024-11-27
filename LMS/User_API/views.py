from rest_framework.decorators import api_view, permission_classes
from .serializer import Registration_Serializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
@api_view(['POST',])
@permission_classes([AllowAny])
def register_user(request):
    serializer = Registration_Serializer(data = request.data, context = {'request': request})
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'response': 'Account Created',
            'username': user.username,
            'email': user.email,
            'token': {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        }
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)