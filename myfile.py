from yahoo_finance import Share

def swings(shares):
    i = 3
    while i < len(shares):
        if(shares[i] > shares[i-1] and shares[i-1] < shares[i-2]):
            print "Swing Up " + shares[i]['Date']
        elif(shares[i] < shares[i-1] and shares[i-1] > shares[i-2]):
            print "Swing Down " + shares[i]['Date']
        elif(shares[i] > shares[i-1]):
            print "Up"
        elif(shares[i] < shares[i-1]):
            print "Down"
        i += 1


def init():
    share = Share('YHOO')
    hist = share.get_historical('2016-02-01', '2016-04-15')
    hist = hist[::-1]
    swings(hist)



class Lowers(object):
    """docstring for Lowers"""
    def __init__(self):
        self.prev_low = 0
        self.lowest = 0
        self.drop_number = 0

    def set_prev_low(self, new_low):
        self.prev_low = new_low
        if(self.prev_low < self.lowest):
            self.lowest = self.prev_low

#check for lower lows after seeing a swing up (3 times for higher confidence)
#this will determine a down trend
