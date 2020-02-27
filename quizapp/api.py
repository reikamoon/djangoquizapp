from rest_framework import generics, permissions, status
from knox.models import AuthToken
from .serializers import RegisterSerializer, UserSerializer

class RegisterAPI(generics.GenericAPIView):
 serializer_class = RegisterSerializer

def post(self, request, *args, **kwargs):
 serializer = self.get_serializer(data=request.data)
 serializer.is_valid(raise_exception=True)
 user = serializer.save()
 return Response({
 "user": UserSerializer(user, context=self.get_serializer_context()).data,
 "token": AuthToken.objects.create(user)[1]
 })
