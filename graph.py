import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# this function plots our masterList
def plotReviewOverTime(masterList):
    xVals,fiveStarVals,fourStarVals,threeStarVals,twoStarVals,oneStarVals = [],[],[],[],[],[]

    for item in masterList:
       xVals.append(item['date'])
       fiveStarVals.append(item['reviews'][5])
       fourStarVals.append(item['reviews'][4])
       threeStarVals.append(item['reviews'][3])
       twoStarVals.append(item['reviews'][2])
       oneStarVals.append(item['reviews'][1])
    
    # Plot all graphs 
    plt.figure()
    plt.plot(xVals, fiveStarVals,label = "5 Star")
    plt.plot(xVals, fourStarVals,label = "4 Star")
    plt.plot(xVals, threeStarVals,label = "3 Star")
    plt.plot(xVals, twoStarVals,label = "2 Star")
    plt.plot(xVals, oneStarVals,label = "1 Star")

    # Label axis
    plt.title('Amazon Reviews')
    plt.xlabel('Dates')
    plt.ylabel('Number of Reviews')

    #ax=plt.gca()
    plt.gcf().autofmt_xdate()

    plt.legend()
    plt.show()

