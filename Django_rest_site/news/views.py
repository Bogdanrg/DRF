from django.forms import model_to_dict
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class NewsListAPI(APIView):
    def get(self, request):
        lst = News.objects.all()
        model_sr = NewsSerializer(lst, many=True)
        return Response({'news': model_sr.data})

    def post(self, request):
        model_sr = NewsSerializer(data=request.data)
        model_sr.is_valid(raise_exception=True)
        model_sr.save()
        return Response({'created data': NewsSerializer(model_sr).data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "invalid pk"})
        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response({'error': "invalid pk"})
        serializer = NewsSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()
        return Response({"news": serializer.data})
