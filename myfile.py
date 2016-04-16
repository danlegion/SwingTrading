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

# def checkSwingUp(shares):
#     i=3
#     while i < len(shares):
#         if(shares[i] > shares[i-1] and shares[i-1] < shares[i-2]):
#             print "Swing Up " + shares[i]['Date']
#         i += 1
#
#
# def checkSwingDown(shares):
#     i = 3
#     while i < len(shares):
#         if(shares[i] < shares[i-1] and shares[i-1] > shares[i-2]):
#             print "Swing Down " + shares[i]['Date']
#         i += 1


def init():
    share = Share('YHOO')
    hist = share.get_historical('2016-02-01', '2016-04-15')
    hist = hist[::-1]
    swings(hist)
