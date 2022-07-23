from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.decorators import action

from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=['get'], detail=False)
    def category(self, request, pk=None):
        cats = Category.objects.all()
        return Response({'cats': [c.title for c in cats]})
    # class NewsListAPIView(generics.ListAPIView):
# queryset = News.objects.all()
# serializer_class = NewsSerializer


# class NewsUpdateApiView(generics.UpdateAPIView):
# queryset = News.objects.all()
# serializer_class = NewsSerializer


# class NewApiView(generics.RetrieveUpdateDestroyAPIView):
# lookup_url_kwarg = 'new_pk'
# queryset = News.objects.all()
# serializer_class = NewsSerializer

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
