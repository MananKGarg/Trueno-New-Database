#rider document schema

{
    _id : "<ObjectID>"
    business_id : "Pharmeasy"     # PE for pharmeasy
    branch_id : "2"               # 2 for sodala branch
    rider_manager : "sameer saxena"   # can be id'ed but not really required
    vehicle_id : "vehicle tag"


    rider_first_name : "Mufaddal"
    rider_middle_name : "null"
    rider_last_name : "Moni"
    rider_aadhar : "1234-1234-1234"  # can be validated through api's of government databases. startup - invoid
    rider_dl_number : "12345678"

    rider_aadhar_image_front : []  # We can either store image directly in database or save it in storage and have url's here. This cn be decided later
    rider_aadhar_image_back : []
    rider_dl_image : []

    stats : {
        distance_travelled : "1230"  # In kms, updated with gps
        rating : "4.5"               # rating can be decided according to a formula that incorporates mechanic rating as well as rash driving status rating
    }

    location : {                      # taken from phone app
        latitude :                    # should rider's location be updated regularly from phone app when we are already getting vehicle location from iot
        longitude :
    }

    previous_vehicles : ["vehicle_id1","" ]
    rider_contact : "1111111111"
    email_id : "rider@gmail.com"
}



