
class Trend(object):

    def __str__(self):
        s =  """
        initial: {0}
        final: {1}
        period high: {2}
        period low: {3}
        delta to high: {4:.2f}\t {5:.1f}%
        delta to low: {6:.2f}\t {7:.1f}%"""
        return s.format(self.initial_close,
        self.final_close,
        self.period_high,
        self.period_low,
        self.delta_to_high, self.delta_to_high_percent,
        self.delta_to_low, self.delta_to_low_percent)

    def __init__(self, partial):
        self.delta_to_high_percent = 0
        self.delta_to_low_percent = 0
        self.partial = partial
        self.initial_close = float(self.partial[-1]['Close'])
        self.final_close = float(self.partial[0]['Close'])
        self.period_high = self.getPeriodHigh()
        self.period_low = self.getPeriodLow(partial)
        self.delta_to_high = self.period_high - self.final_close
        self.delta_to_low = self.final_close - self.period_low
        self.calculateDeltaPercentage()

    def getPeriodHigh(self):
        result = None
        for day in self.partial:
            close = day['Close']
            if( result == None or close > result):
                result = close
        return float(result)

    def getPeriodLow(self, partial):
        result = None
        for day in partial:
            close = day['Close']
            if( result == None or close < result):
                result = close
        return float(result)

    def calculateDeltaPercentage(self):
        self.delta_to_high_percent = (self.delta_to_high * 100) / self.final_close
        self.delta_to_low_percent = (self.delta_to_low * 100) / self.final_close


    #get high for period
    #get low for period
    #analyze trend (
        #how many deltas
        #how far from high/low,
        #how many corrections)
    #
