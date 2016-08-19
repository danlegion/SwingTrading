from yahoo_finance import Share
import json


def swings(shares, ll):
    i = 3
    inital_lowest = ll.lowest
    print "Inital lowest " + inital_lowest

    while i < len(shares):
        cur = shares[i]['Close']
        prev = shares[i-1]['Close']
        tprv = shares[i-2]['Close']
        if(cur > prev and prev < tprv):
            print "Swing Up\t" + shares[i]['Date']
        elif(cur < prev and prev > tprv):
            print "Swing Down\t" + shares[i]['Date']
            analyzeDownTrend(cur, ll)
        elif(cur > prev and prev > tprv):
            print "Up"
        elif(cur < prev and prev < tprv):
            analyzeDownTrend(cur, ll)
            print "Down"

        i += 1
    print "lowest: {0}, inital low: {1}, current low: {2}".format(ll.lowest, inital_lowest, ll.cur_low)


def init():
    share = Share('YHOO')
    hist = share.get_historical('2015-12-03', '2016-02-18')
    hist = hist[::-1]
    ll = Lowers(hist[2]['Close'])
    swings(hist, ll)

def initFromFile():
    with open('data-bce.txt', 'r') as file:
        hist = []
        lines = file.readlines()
        for item in lines:
            item = item.replace("'","\"")
            hist.append(json.loads(item))

        hist = hist[::-1]
        ll = Lowers(hist[2]['Close'])
        swings(hist, ll)


# def run():
#     reload()
#     initFromFile()


def analyzeDownTrend(share, lowers):
    # print lowers.cur_low + "   cur: " + share
    cur_drops = lowers.drop_number
    if lowers.cur_low > share:
        lowers.drop_number += 1
        lowers.set_prev_low(share)
    if lowers.drop_number >= 3 and cur_drops != lowers.drop_number:
        print "---------{0} Lower Lows at {1}".format(lowers.drop_number, lowers.cur_low)



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
