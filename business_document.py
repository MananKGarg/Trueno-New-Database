# partner b2b businesses document schema

{
    _id : "1"   # Say pharmeasy
    name : "pharmeasy"
    poc : "sameer"               # depends company to company
    contact : ""                 # What more information about a business do we need to store
    email : ""
    head_office_location : ""
    total_vehicles : "67"
    total_batteries : "98"       # Sum from all sub branches
    registered_riders : "54"
    total_chargers : "30"

    branches : {

        branch_no : "1"
        branch_address : {
            branch_name : "Raju EV shop"
            branch_number : "212"
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

        branch_poc : "Amit Bhardwaj"
        contact : "2345123423"
        email : "amit.bhardwaj@pharmeasy.in"
        branch_vehicles : "34"
        branch_batteries : "23"
        branch_chargers : "5"
        branch_registered_riders : "23"



        branch_no: "2"
        branch_address: {
            branch_name: "Raju EV shop"
            branch_number: "212"
            street: "gulmohar road"
            landmark: "H10"
            village: "null"
            town: "null"
            city: "Mumbai"
            state: "Maharashtra"
            country: "India"
            pin: "400076"
            zone_code: "4"
            subzone_code: "40"
            district_code: "400"
            postoffice_code: "076"
            latitude: "19.1298002"  # Geocoding API
            longitude: "72.9129421"
        }

        branch_poc: "Amit Bhardwaj"
        contact: "2345123423"
        email: "amit.bhardwaj@pharmeasy.in"
        branch_vehicles: "34"
        branch_batteries: "23"
        branch_chargers: "5"
        branch_registered_riders: "23"
        branch_issues : "35"                     # see what logic can be defined for this







    }



}
