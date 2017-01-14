from yahoo_finance import Share
from django.views.generic import View
from django.http import HttpResponse
from logic.trends import Trend
import json
from datetime import date, timedelta


class Swing(View):

    def get(self, request):
        trends = self.analyze()
        data = []
        for trend in trends:
            data.append(trend.toJson())
        return HttpResponse(json.dumps(data))

    # trends the stocks for the past 30 days
    def analyze(self):
        stocks = ['CVE.TO', 'GOOG', 'HBC.TO', 'CNQ.TO']
        today = str(date.today())
        start_date = str(date.today() - timedelta(days=30))

        data = []
        for symbol in stocks:
            share = Share(symbol)
            values = share.get_historical(start_date, today)
            data.append(Trend(values, symbol))
        return data
