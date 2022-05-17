# repair document schema

{
    repair_id : "<objectID>"
    business_branch_id : "PE1"
    rider_id : "rider_id"
    mechanic_id : "mechanic_id"          # after the mechanic is assigned to the rider
    vehicle_id : "vehicle_id"
    battery_id : "battery_id"            # should we include battery id here or not as it is already connected to vehicle
    iot_id : ""
    charger_id : "charger_id"
    
    operation_manager_raised : "0"       # Boolean value that signifies if the request is raised from app or dashboard

    repair_raise_time : "ISODatetime"    # noted when rider raises the issue
    repair_resolve_time : "ISODatetime"  # noted when mechanic completes the request
    repair_status : "0"                  #

    issue_raise_address : {
        latitude : "56.0098890"
        longitude : "76.0083335"
        street : "gulmohar road"         # All the other information than lat long is obtained from google geocoding API
        landmark : "H10"                 # This helps in better analysis of requests
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
    }


    rider_issues{
        issue_number : "1"
        issue_category : "predefined issue category"      # see whether multiple issues can be accomodated in single repair document
        issue_subcategory : "predefined issue subcategory"   # Which mechanic is assigned if multiple issues are raised by a single mechanic. Think data structure to handle this
        issue_images: ["matrix of images uploaded by rider"]  # compulsory
        issue_audio: "rider's audio file"
        issue_description: "text from rider"                  # compulsory
        issue_inventory_consumed : [""]


        issue_number : "2"
        issue_category : "predefined issue category"
        .
        .
        .

    }

    repairs_made{
        repair_number: "1"
        issue_category: "predefined issue category"         # see whether multiple issues can be accomodated in single repair document
        issue_subcategory: "predefined issue subcategory"    # Which mechanic is assigned if multiple issues are raised by a single mechanic. Think data structure to handle this
        issue_images: ["matrix of images uploaded by rider"]  # compulsory
        issue_audio: "rider's audio file"
        issue_description: "text from rider"  # compulsory
        issue_inventory_consumed: [""]


        issue_number: "2"
        issue_category: "predefined issue category"
            .
            .
            .

    }


    rating_by_rider : "4"
    rating_by_mechanic : "3"
    rider_approval : "1"

    payment_status : "0"             # will be set to 1 after the payment request from mechanics app is completed

    amount : {
        repair_amounts : {
            servicing_fee : "200"
            repair_1_amount : "56"     # How to generate amount for repair. Either standard from some master rates. But how to accomodate for flexibility in repairs.
            repair_2_amount : "76"
            repair_3_amount : "89"
        }
        total : "total amount"
        tax :                          # Ask Somil what is the taxation process for mechanic
    }

}
