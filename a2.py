def hotelCost(numOfNights):
    return 200 * numOfNights
def vehicalCost(numOfDays):
    if(numOfDays>7):
        return(numOfDays *100) -100
    elif numOfDays>3 and numOfDays<=7:
        return(numOfDays*100)- 20
    else:
        return numOfDays*100
def planeCost(distance):
    return 150 * distance
def changeCurrency(amount):
    return amount/277
nights= int(input("Enter number of nights : "))
days= int(input("Enter number of days : "))
distance= int(input("Enter the distance : "))
totalCost=hotelCost(nights)+vehicalCost(days) + planeCost(distance)
print("The total cost of the trip is : PKR " , totalCost)
print("The total cost in USD would be : $ " , changeCurrency(totalCost))