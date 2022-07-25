from django.forms import model_to_dict
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .paginations import *
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .permissions import *

# class NewsViewSet(viewsets.ModelViewSet):
#    serializer_class = NewsSerializer
#
#    def get_queryset(self):
#        if self.kwargs.get('pk', None):
#            return News.objects.filter(pk=self.kwargs.get('pk'))
#        return News.objects.all()[:3]
#
#    @action(methods=['get'], detail=False, url_path='category',
#            url_name='category')
#    def category(self, request):
#        cats = Category.objects.all()
#        return Response({'cats': [c.title for c in cats]})


class NewUpdateApiView(generics.RetrieveUpdateAPIView):
    lookup_url_kwarg = 'new_pk'
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (SessionAuthentication, )


class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = NewsCustomSetPagination


class NewDeleteAPIView(generics.RetrieveDestroyAPIView):
    lookup_url_kwarg = 'new_pk'
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )


# class NewsListAPI(APIView):
#   def get(self, request):
#        lst = News.objects.all()
#        model_sr = NewsSerializer(lst, many=True)
#        return Response({'news': model_sr.data})
#
#   def post(self, request):
#       print(request.data)
#       mod#el_sr = NewsSerializer(data=request.data)
#       model_sr.is_valid(raise_exception=True)
#       model_sr.save()
#       return Response({'created data': NewsSerializer(model_sr).data})
#
#   def put(self, request, *args, **kwargs):
#       pk = kwargs.get('pk', None)
#       if not pk:
#           return Response({'error': "invalid pk"})
#       try:
#           instance = News.objects.get(pk=pk)
#       except:
#           return Response({'error': "invalid pk"})
#       serializer = NewsSerializer(data=request.data, instance=instance)
#       serializer.is_valid()
#       serializer.save()
#        return Response({"news": serializer.data})
#
#    def delete(self, request, *args, **kwargs):
#        pk = kwargs.get('pk', None)
#        post = News.objects.get(pk=pk)
#        post.delete()
#       return Response('qweqw')
