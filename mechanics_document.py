# mechanics document schema

{
    _id : "<ObjectID>"

    mechanic_first_name : "Raju"
    mechanic_middle_name : "kumar"        # can be null
    mechanic_last_name : "goyal"
    contact_number : "2222222222"
    email_id : "mechanic@gmail.com"
    dob : "ISODate"
    profile_pic : "[image]"

    address : {                           # embedded beacause of one to one mapping in address and shop owner
        shop_name : "Raju EV shop"        # what if a mechanic is registering away from his shop?
        shop_number : "212"
        street : "gulmohar road"
        landmark : "H10"
        village : "null"
        town : "null"
        city : "Mumbai"
        state : "Maharashtra"
        country : "India"
        pin: "400076"
        zone_code: "4"
        subzone_code: "40"
        district_code: "400"
        postoffice_code: "076"
        latitude : "19.1298002"          # Geocoding API
        longitude : "72.9129421"
    }

    timings : {
        opening_time : "0900"
        closing_time : "1900"
    }

    stats : {
        overall_rating : "4.7"                 # logic for rating would be average of all repairs
        total_repairs : "72"                   # These stats are obtaind from repair ids
        total_revenue : "4000"                 # updated after payment is done
        total_customers : "55"
    }

    active_working_status : "1"                         # opening closing timings of mechanic can be tracked through this
    garage_pics : ["pic1", "pic2"...]

    payment : {
        upi : "upi_id"
        bank_acc : "acc_no"
        bank_name : "canara_bank"
        ifsc : "ifsc code"
    }

    repairs : {                                              # repairs need to be linked else document size can increase
        tentative_repairs : ["repair_id1", "repair_id2"...]  # should we include tentative repairs. Think a little more about it
        accepted_repairs : ["repair_id3", "repair_id4"...]
        completed_repairs : ["repair_id5", "repair_id6"...]
        pending_payments_repairs : ["repair_id7", "repair_id8"]
    }

    riders : ["rider_id1, rider_id2, rider_id3"...]                        # rider is customer.

}
