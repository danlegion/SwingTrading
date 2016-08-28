from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
import json
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ReactTest(View):
    def get(self, request):
        data = {"id":1,"author":"pete"}
        return HttpResponse(json.dumps(data))
        # return TemplateResponse(request,'index.html',data)
class ReactTestB(View):
    def get(self, request):
        data = {"id":1,"author":"pete"}
        return HttpResponse(json.dumps(data))
