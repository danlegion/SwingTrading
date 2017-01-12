
class Trend(object):

    def toJson(self):
        j = {'stock': self.symbol,
            'inital': self.initial_close,
            'final': self.final_close,
            'period high': self.period_high,
            'period low': self.period_low,
            'delta to high': "${0:.2f} - {1:.1f}%".format(self.delta_to_high, self.delta_to_high_percent),
            'delta to low': "${0:.2f} - {1:.1f}%".format(self.delta_to_low, self.delta_to_low_percent),
            'advice': self.notification,
            'trends': self.trends}
        return j

    def __str__(self):
        s =  """
        initial: {0}
        final: {1}
        period high: {2}
        period low: {3}
        delta to high: {4:.2f}\t {5:.1f}%
        delta to low: {6:.2f}\t {7:.1f}%
        {8}"""
        return s.format(self.initial_close,
        self.final_close,
        self.period_high,
        self.period_low,
        self.delta_to_high, self.delta_to_high_percent,
        self.delta_to_low, self.delta_to_low_percent,
        self.notification)

    def __init__(self, partial, symbol):
        self.symbol = symbol
        self.delta_to_high_percent = 0
        self.delta_to_low_percent = 0
        self.partial = partial
        self.initial_close = float(self.partial[-1]['Close'])
        self.final_close = float(self.partial[0]['Close'])
        self.period_high = self.getPeriodHigh()
        self.period_low = self.getPeriodLow()
        self.delta_to_high = self.period_high - self.final_close
        self.delta_to_low = self.final_close - self.period_low
        self.calculateDeltaPercentage()
        self.trends = []
        self.notification = ""
        self.swings = Swings()
        self.calculateTrends()
        self.computeAdvice()

    def getPeriodHigh(self):
        result = None
        for day in self.partial:
            close = float(day['Close'])
            if result is None or close > result:
                result = close
        return result

    def getPeriodLow(self):
        result = None
        for day in self.partial:
            close = float(day['Close'])
            if result is None or close < result:
                result = close
        return result

    def calculateDeltaPercentage(self):
        self.delta_to_high_percent = (self.delta_to_high * 100) / self.final_close
        self.delta_to_low_percent = (self.delta_to_low * 100) / self.final_close

    def calculateTrends(self):
        j = 0
        shares = self.partial[::-1]
        while j < len(self.partial)-8:
            tmp_shares = shares[j:j+8]
            i = 3

        #repeat this for a size of 5 days every day

        #this method right now represents only 1 day
            while i < len(tmp_shares):
                cur = tmp_shares[i]['Close']
                prev = tmp_shares[i-1]['Close']
                tprv = tmp_shares[i-2]['Close']
                self.swings.computeTrends(cur, prev, tprv)
                i += 1
            self.trends.append(self.swings.latest_trend)
            j += 1


#store the latest trend and analyze:
    # - if latest 2 trends are up check the previous if  2 or more previous are down could be time to buy
    # - if latest 2 trends are down check the previous if 2 or more previous are up could be time to sell
    def computeAdvice(self):
        trends = self.trends[::-1]

        if(trends[0] == trends[1] and trends[2] == trends[3] and trends[1] != trends[2]):
            if(trends[0] == "up"):
                self.notification = "POSSIBLE BUY OPPORTUNITY"
            elif(trends[0] == "down"):
                self.notification = "POSSIBLE SELL TIME"
        else:
            self.notification = "no changes to {0} trend".format(trends[0].upper())



    #get high for period
    #get low for period
    #analyze trend (
        #how many deltas
        #how far from high/low,
        #how many corrections??,
        #how many uptrends,
        #how many downtrends)

    #Algorithm for calculating swing trend:
    #the more up trends vs down trends higher confidence of real uptrend
    #the more down trends vs up trends highger confidence of real downtrend

    #Result: number of up trends and number of down trends
    #uptrend is: at least 2 swing up in a row OR at least 3 higher highs in a row
    #downtrend is: at least 2 swing down in a row OR at least 3 lower lows in a row

    #note for there to be 2 swingups in a row there has to be a swingdown in the middle
    #swingup = prince -> lower -> higher
    #swingdown  = price -> higher -> lower


class Swings(object):
    """docstring for Lowers"""
    def __str__(self):
        s =  """
        Up trends count:{0}
        Down trends count: {1}
        Trend: {2}"""
        return s.format(self.uptrend_count, self.downtrend_count, self.latest_trend.upper())


    def __init__(self):
        self.last_swing = ""
        self.downtrend_count = 0
        self.uptrend_count = 0
        self.confidence_level = 0

        self.swings = []
        self.latest_trend = ""
        self.temp_trend = ""

    def capture(self,swing):
        self.swings.append(swing)

    def computeTrends(self, cur, p, pp):
        if cur < p:
            self.temp_trend = "down"
        elif cur > p:
            self.temp_trend = "up"

        if cur < pp and self.temp_trend == "down":
            self.downtrend_count += 1
            self.latest_trend = "down"
        elif cur < pp and self.temp_trend == "up":
            #this could be a correction
            pass
        elif cur > pp and self.temp_trend == "up":
            self.uptrend_count += 1
            self.latest_trend = "up"
        elif cur > pp and self.temp_trend == "down":
            #this could be a correction
            pass
