import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


#class NewsModel:
   # def __init__(self, title, content):
      #  self.title = title
       # self.content = content
##

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200,)
    content = serializers.CharField()
    upload_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=False)
    category_id = serializers.IntegerField()


#def encode():
    #model = NewsModel('Bogdan', 'Bogdan Tsimafeyeu')
    #model_sr = NewsSerializer(model)
    #print(model_sr.data)
   # json = JSONRenderer().render(model_sr.data)
    #print(json)


#def decode():
    #stream = io.BytesIO(b'{"title": "Bogdan", "content": "Bogdan Tsimafeyeu"}')
    #data = JSONParser().parse(stream)
   # model_sr = NewsSerializer(data=data)
   # model_sr.is_valid()
   ## print(model_sr.validated_data)
