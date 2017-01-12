from yahoo_finance import Share
from django.views import View
from django.http import HttpResponse
from logic.trends import Trend
import json
from datetime import date, timedelta


class Swing(View):

    # trends the stocks for the past 30 days
    def get(self, request):
        today = str(date.today())
        start_date = str(date.today() - timedelta(days=30))
        stocks = ['CVE.TO', 'GOOG', 'HBC.TO']
        data = []
        for symbol in stocks:
            share = Share(symbol)
            values = share.get_historical(start_date, today)
            data.append(Trend(values, symbol).toJson())
        return HttpResponse(json.dumps(data))
