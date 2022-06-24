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
        new_news = News.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            is_published=request.data['is_published'],
            category_id=request.data['category_id']
        )
        return Response({'created data': NewsSerializer(new_news).data})
