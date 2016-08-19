from yahoo_finance import Share

def init():
    share = Share('BCE.TO')
    hist = share.get_historical('2015-12-03', '2016-08-18')
    with open('data-bce.txt', 'w') as file:
        for item in hist:
            print (item)
            file.write(str(item))
            file.write("\n")
