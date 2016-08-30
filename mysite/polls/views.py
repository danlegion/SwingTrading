from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
import json
from django.views import View
from rest_framework import generics

from rest_framework import serializers

# Create your views here.
class ObjSerializer(serializers.ModelSerializer):
	class Meta:
		model = {}
		fields = ('id', 'author')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ReactTest(View):
    def get(self, request):
        data = [
            {'name':"a",'value':2},
            {"name":"b","value":4},
            {"name":"c","value":3},
            {"name":"d","value":7},
        ]
        return HttpResponse(json.dumps(data))
        # return TemplateResponse(request,'index.html',data)
class ReactTestB(generics.ListCreateAPIView):
    # def get(self, request):
    queryset = {"id":1,"author":"pete"}
    serializer_class = ObjSerializer
