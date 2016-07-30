from yahoo_finance import Share


def swings(shares, ll):
    i = 3
    print ll.cur_low
    while i < len(shares):
        cur = shares[i]['Close']
        prev = shares[i-1]['Close']
        tprv = shares[i-2]['Close']
        if(cur > prev and prev < tprv):
            print "Swing Up\t" + shares[i]['Date']
        elif(cur < prev and prev > tprv):
            print "Swing Down\t" + shares[i]['Date']
            analyzeDownTrend(cur, ll)
        elif(cur > prev):
            print "Up"

        i += 1
    print ll.cur_low


def init():
    share = Share('YHOO')
    hist = share.get_historical('2015-12-03', '2016-02-18')
    hist = hist[::-1]
    ll = Lowers(hist[3]['Close'])
    swings(hist, ll)


def analyzeDownTrend(share, lowers):
    # print lowers.cur_low + "   cur: " + share
    if lowers.cur_low > share:
        lowers.drop_number += 1
    if lowers.drop_number >= 3:
        print "---------Lower Low"
    lowers.set_prev_low(share)


class Lowers(object):
    """docstring for Lowers"""
    def __init__(self, low):
        self.cur_low = low
        self.lowest = low
        self.drop_number = 0
        self.confidence_level = 0

    def set_prev_low(self, new_low):
        self.cur_low = new_low
        if(self.cur_low < self.lowest):
            self.lowest = self.cur_low

# check for lower lows after seeing a swing up (3 times for higher confidence)
# this will determine a down trend
