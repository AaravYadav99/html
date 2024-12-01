def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city =="Dharan":
        return 140
    elif city =="kathmandu":
        return 500
    elif city =="janakpur":
        return 300
    
def rental_car_cost(days):
    if days>=7:
        return 48*days -50
    elif days>=3:
        return 48*days - 29
    else:
        return  48*days
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+plane_ride_cost(city)+hotel_cost(days)+spending_money
print("the total cost is to Dharan",trip_cost("Dharan",7,2000))
     
    