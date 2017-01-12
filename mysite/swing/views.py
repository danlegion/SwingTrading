from yahoo_finance import Share
from django.views import View
from django.http import HttpResponse
from logic.trends import Trend
import json


class Swing(View):

    def get(self, request):
        stocks = ['CVE.TO', 'GOOG', 'HBC.TO']
        data = []
        for symbol in stocks:
            share = Share(symbol)
            values = share.get_historical('2016-12-01', '2017-01-11')
            data.append(Trend(values, symbol).toJson())
        return HttpResponse(json.dumps(data))
