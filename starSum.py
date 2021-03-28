import datetime

#This function sums up all reviews and creats a master list for plotting
def sumRatings(reviewList):
    #here we the whole list by the date value
    reviewList = sorted(reviewList, key=lambda k: k['date']) 
    masterList=[]
    oneStar,twoStar,threeStar,fourStar,fiveStar = 0,0,0,0,0

    # Loop through the list of reviews
    for item in reviewList:
        if(item['rating']==1):
            oneStar +=1
        elif(item['rating']==2):
            twoStar +=1
        elif(item['rating']==3):
            threeStar +=1
        elif(item['rating']==4):
            fourStar +=1
        elif(item['rating']==5):
            fiveStar +=1

        reviewDict = {1:oneStar,2:twoStar,3:threeStar,4:fourStar,5:fiveStar}
        Date_and_Total = {'date':item['date'],'reviews':reviewDict}
        masterList.append(Date_and_Total)

    # Print total star ratings for 1-5
    print("Total 5 star ratings: ", fiveStar)
    print("Total 4 star ratings: ", fourStar)
    print("Total 3 star ratings: ", threeStar)
    print("Total 2 star ratings: ", twoStar)
    print("Total 1 star ratings: ", oneStar)

    # Return the list to main
    return masterList
