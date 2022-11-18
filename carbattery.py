import json
import datetime

def estimatecarbattery():
    
    name = input("enter your name")
    phonenumber = eval(input("enter your mobile number"))
    currentbattery= eval(input("current battery percentage")) 
    fullcharge= eval(input("fullchargecapacity"))
    totaldistance = eval(input("totaldistance"))
    distance_covered = eval(input("current distance"))
    started_at = datetime.datetime.now()
    started_at = started_at.strftime("%Y-%m-%d")
    
    percentage = fullcharge/100
    remainingdistance= totaldistance - distance_covered
    remainingbattery =(remainingdistance/percentage)-currentbattery
    remainingdistance=totaldistance-distance_covered
    requiredbattery=remainingdistance*percentage


    new_users = {

        
            
            'name': name,
            'phone': phonenumber,
            'requiredbattery': [{
                'currentbattery': currentbattery,
                'fullcharge': fullcharge,
                'distance_covered': distance_covered,
                'remainingdistance': remainingdistance,
                'started_at': started_at,
            }],
        }
    print(new_users)
        
   
    
    print("batterycharge required to reach destination",remainingbattery)
    print("remainingdistance",remainingdistance,"km")
    print("required battery ", requiredbattery)
    return new_users


def write_extracted(data):
    print(data)
    json_format = json.dumps(data, indent=3)
    print(json_format)
    y = open('/home/gowshali/travel_details', 'w')
    y.write(json_format)
    y.close
data=estimatecarbattery()   
write_extracted(data)
# get the user detail name,mobile number,trip total distance, current battery , battery required, remaining distance to cover
# get the hours and min sec
# write in to json file 



# def estimatecarbattery():
# #     try:
#         currentbattery = eval(input("current battery percentage"))
#         fullcharge_distance = eval(input("fullchargecapacity_distance"))
#         totaldistance = eval(input("totaldistance"))

#     except Exception as e:
#         print("Value error occured")
        
#     else:
#         km_per_charge=100/fullcharge_distance
#         print("km per charge" , km_per_charge)
#         distance_covered=currentbattery*km_per_charge
#         remainingdistance=totaldistance-distance_covered
#         requiredbattery=remainingdistance*km_per_charge
#         print("batterycharge required to reach destination", int(requiredbattery),"%")
#         print("remainingdistance", int(remainingdistance), "km")

# estimatecarbattery()

