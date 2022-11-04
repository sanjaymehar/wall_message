from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class Wallall(generics.ListAPIView):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer

class WallGetData(generics.RetrieveAPIView):
    queryset = Wall.objects.all()
    serializer_class = WallCreateSerializer


class Wallcreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Wall.objects.all()
    serializer_class = WallCreateSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WallUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Wall.objects.all()
    serializer_class = WallUpdateSerializer1

    def update(self, request, *args, **kwargs):
        print(request.data,"dataaa")
        tid=self.kwargs['pk']
        data=Wall.objects.get(id=tid)
        owner=data.user.id 
        cuser=self.request.user.id
        if int(owner)!=cuser:
            return Response({'error': 'Unauthorized Access'}, status=401)
        else:
                return super(WallUpdate, self).update(request, *args, **kwargs)

class WallDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Wall.objects.all()
    serializer_class = WallUpdateSerializer1

    def delete(self, request, *args, **kwargs):
        print(request.data,"dataaa")
        tid=self.kwargs['pk']
        data=Wall.objects.get(id=tid)
        owner=data.user.id 
        cuser=self.request.user.id
        if int(owner)!=cuser:
            return Response({'error': 'Unauthorized Access'}, status=401)
        else:
                return super(WallDelete, self).delete(request, *args, **kwargs)

