# vehicle document schema

{
    _id : "<ObjectID>"
    vehicle_tag : "PEBL1"
    business_id : "2"              # 2 for pharmeasy
    branch_id : "2"                # 2 for jaipur branch
    rider_id : "rider_id"
    battery_id : "battery_id"       # How to handle battery input while vehicle assigning for the first time
    iot_id : "iot_id"               # confirm. According to me, there is one imei for one iot
    service_partner_id : ""
    
    chassis_number : "chassis_number"
    chassis_warranty_end_dateTime : "ISODateTime"
    
    motor_no : ""
    motor_warranty_end : "ISODateTime"
    
    converter_number : ""
    converter_warranty_end : "ISODateTime"     # Change to epoch time if required
    
    controller_no : ""
    controller_warranty_end : "ISODatetime"

    vehicle_brand : "suzuki"
    vehicle_model : "stype"
    vehicle_make : "loev"
    manufacturing_year : "1983"
    vehicle_number : "number_plate"
    motor_type : "BLDC hub motor"
    ignition_type : "keyless"      # we can include many more vehicle attributes but they are useless as they can be found from the vehicle model document if required

    invoice_date : "ISODate"       # how to store invoice? Either seperate document for invoice or vehicle cost can be included in vehicle document base
    invoice_number : "invoice_number"
    recieving_date : "ISODate"

    deployed_city : "Jaipur"
    location : {
        latitude : "56.9876543"
        longitude : "87.9887643"  # location comes from IOT device
    }

    ignition_status : "0"

    previous_riders : ["rider_id1", "rider_id2"...]
    repairs : ["repair_id1", "repair_id2"...]

    insurance : {
        insurance_status : "yes/no"
        insurance_first_party_start_date : ""
        insurance_third_party_end_date : ""
        insurance_first_party_end_date : ""
        insurance_third_party_end_date : ""
        insurance_policy_number : ""
        insurance_sum_insured : ""
        insurance_premium : ""
        
    }
    
    insurance_claim : {
    
    
    
    }

    battery_swaps : {
        battery_into_vehicle: "id"          # battery in logged by mechanic through app
        battery_into_vehicle_soc : "90"
        battery_out_of_vehicle : "id"        # battery out logged by mechanic
        battery_out_of_vehicle_soc : "20"
        swap_time : ""            # swap time comes from mechanics app when battery is swapped
        swap_station_id : "23"

        battery_into_vehicle: "id"          # battery in logged by mechanic through app
        battery_into_vehicle_soc : "90"
        battery_out_of_vehicle : "id"        # battery out logged by mechanic
        battery_out_of_vehicle_soc : "20"
        swap_time : ""            # swap time comes from mechanics app when battery is swapped
        swap_station_id : "23"
        
        battery_in: "id"  # battery in logged by mechanic through app
        battery_out: "id"  # battery out logged by mechanic
        swap_time: ""  # swap time comes from mechanics app when battery is swapped
        swap_station_id: "23"
    }

    # preventive maintenance

    preventive_maintenance : {


        last_service_in_time : "ISODateTime"                 # How will this be updated? The person who does preventive maintenance looks after this
        last_service_out_time : "ISODateTime"
        servicing_partner_id : "2"                           # Add kms run from last service
        kms_from_last_service : "2500"                       # Is set to 0 when service is approved by rider
                                                             # What are standard services in preventive maintenance
        service_elements : {

        }

    }



}

