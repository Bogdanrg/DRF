from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class NewsListAPI(APIView):
    def get(self, request):
        lst = News.objects.all().values()
        return Response({'news': lst})

    def post(self, request):
        new_news = News.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            is_published=request.data['is_published'],
            category_id=request.data['cat_id']
        )
        return Response({'exit-code': model_to_dict(new_news)})
