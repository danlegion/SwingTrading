from yahoo_finance import Share
import json

def init():
    share = Share('CVE.TO')
    hist = share.get_historical('2015-12-03', '2017-01-09')
    with open('data-cve.txt', 'w') as file:
        for item in hist:
            print (json.dumps(item))
            file.write(json.dumps(item))
            file.write("\n")
