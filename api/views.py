from rest_framework import generics, permissions, renderers
from rest_framework.response import Response
from accounts.models import Profile
from .serializers import ApiSerializer, UserSerializer
from .permissions import IsOwnerReadOnly

class ApiList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ApiSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ApiSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly)
