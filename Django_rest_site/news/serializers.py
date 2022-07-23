import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import News


# class NewsModel:
# def __init__(self, title, content):
#  self.title = title
# self.content = content


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

# def encode():
# model = NewsModel('Bogdan', 'Bogdan Tsimafeyeu')
# model_sr = NewsSerializer(model)
# print(model_sr.data)
# json = JSONRenderer().render(model_sr.data)
# print(json)


# def decode():
# stream = io.BytesIO(b'{"title": "Bogdan", "content": "Bogdan Tsimafeyeu"}')
# data = JSONParser().parse(stream)
# model_sr = NewsSerializer(data=data)
# model_sr.is_valid()
# print(model_sr.validated_data)
