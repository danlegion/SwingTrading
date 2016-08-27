from yahoo_finance import Share
import json

def init():
    share = Share('BCE.TO')
    hist = share.get_historical('2015-12-03', '2016-08-18')
    with open('data-bce.txt', 'w') as file:
        for item in hist:
            print (json.dumps(item))
            file.write(json.dumps(item))
            file.write("\n")
