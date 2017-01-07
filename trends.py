
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
        self.swingups_count = 0
        self.swingdowns_count = 0
        self.calculateTrends()

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

    def calculateTrends(self):
        i = 3
        shares = self.partial[::-1]
        ll = Swings(shares[2]['Close'])
        inital_lowest = ll.lowest
        print "Inital lowest: " + inital_lowest

        while i < len(shares):
            cur = shares[i]['Close']
            prev = shares[i-1]['Close']
            tprv = shares[i-2]['Close']
            if(cur > prev and prev < tprv):
                print "Swing Up\t" + shares[i]['Date'] +' ' + cur
                ll.capture("swingup")
            elif(cur < prev and prev > tprv):
                print "Swing Down\t" + shares[i]['Date'] + ' ' + cur
                ll.capture("swingdown")
            elif(cur > prev and prev > tprv):
                print "Up" + ' ' + cur
                ll.capture("up")
            elif(cur < prev and prev < tprv):
                print "Down" + ' ' + cur
                ll.capture("down")


            i += 1
        print ll.swings




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
    def __init__(self, low):
        self.cur_low = low
        self.cur_high = low
        self.lowest = low
        self.highest = low

        self.last_swing = ""
        self.swingups_count = 0
        self.swingdowns_count = 0
        self.confidence_level = 0

        self.swings = []

    def capture(self,swing):
        self.swings.append(swing)

    def computeTrends():
        i = 1
        while i < len(self.swings):
            swing = self.swing[i]





    # def analyzeSwing(self, share, swing):
    #     print "curLow: {0}, curHigh:{1}, Cur:{2}, Swing:{3} ".format(self.cur_low, self.cur_high, share, swing)
    #     if swing == 'up':
    #         if(self.last_swing == 'down'):
    #             self.swingups += 1
    #         # pass
    #     elif swing == 'down':
    #         self.analyzeDownTrend(share)
    #
    # def analyzeDownTrend(self, share):
    #     # print self.cur_low + "   cur: " + share
    #     if(self.last_swing == "up"):
    #         self.swingdowns_count += 1
    #
    #     cur_drops = self.drop_number
    #     if self.cur_low > share:
    #         self.drop_number += 1
    #         self.set_prev_low(share)
    #
    #     if self.drop_number >= 3 and cur_drops != self.drop_number:
    #         print "---------{0} Lower Lows at {1}".format(self.drop_number, self.cur_low)
