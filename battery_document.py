#battery document schema

{
    _id : "<ObjectID"
    battery_invoice_number : ""
    battery_serial_number : " "
    vehicle_id : "vehicle_id"
    battery_iot_id : "imei"         # battery iot
    battery_iot_oem : "neuron"
    battery_tag : "tag"
    series_parallel : ""    #ask exact term to shubham
    battery_type : "lithium phosphate"
    battery_ : "emuron"

 # Smart batteries. What data would be provided by smart batteries. Discuss at length with Shubham
    #best performance of battery
    #best life cycle
    #minimal risk

    cell_specification : ""
    operating_voltage : ""
    individual_cell_voltage : ""
    battery_capacity : ""
    battery_max_charging_current  : ""
    battery_max_discharge_current : ""
    battery_pack_current : ""
    temperature_of_cells : ""
    number_of_cycles : ""
    warranty : ""
    state_of_charge : ""
    location : {
        latitude : ""
        longitude : ""
}

    swap_data : {
        vehicle_id : "893e83"
        rider_id : "raju"
        swap_timestamp : "ISODatetime"
        soc : ""
        flag : "insert"
        swap_station_id : "23"

        vehicle_id : "82383e"
        rider_id : "raju"
        swap_timestamp : "ISODatetime"
        soc : ""
        flag : "back_to_station"
        swap_station_id : "23"

        vehicle_id: "82383e"
        rider_id : "raju"
        swap_timestamp: "ISODatetime"        # Should we allow this? Mostly not but discuss this with Somil and Team
        soc : ""
        flag: "vehicle_to_vehicle"
        swap_station_id : "null"
    }


}
