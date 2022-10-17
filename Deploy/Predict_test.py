#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:42:32 2022

@author: battisaco
"""
import requests

url = 'http://0.0.0.0:9697/Predict_resort'

booking = {
 "is_canceled": 0,
 "lead_time": 5.8377304,
 "arrival_date_month": 7,
 "stays_in_weekend_nights": 0,
 "stays_in_week_nights": 0,
 "adults": 2,
 "children": 0.0,
 "babies": 0,
 "meal": 0,
 "market_segment": 0,
 "distribution_channel": 0,
 "is_repeated_guest": 0,
 "previous_cancellations": 0,
 "previous_bookings_not_canceled": 0,
 "reserved_room_type": 0.0,
 "assigned_room_type": 0.0,
 "booking_changes": 3,
 "deposit_type": 0,
 "agent": 2.302585,
 "days_in_waiting_list": 0.0,
 "customer_type": 0,
 "adr": 0.0,
 "required_car_parking_spaces": 0,
 "total_of_special_requests": 0}

response = requests.post(url, json=booking).json()
print(response)

if response['cancel'] == True:
    print('Provavel cancelamento')
else:
    print('Provavel não cancelamento')