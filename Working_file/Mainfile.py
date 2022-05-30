from PV import *
from Consumption import *
from Energy_flux import *
import pandas as pd
import numpy as np
import time
import os
import csv

"This Mainfile is the only one that need to run"

"The parameters should be adjusted according to operation model: a)DR or b)REC"
"————————————————————————————————————————————"
"Adjusting PV parameters"
area = 2.576 # m^2
panel_efficiency = 0.203
loss = 0.8
number_panels = 20

"Adjusting battery parameters"
   
deep_battery = 0.05  #The maximum allowed charge deepth 
bat_charge_speed = 1400 #charging speed, Wh

"Adjusting charging time"
char_time_start = 3  #charging start time
char_time_stop = 4   #charging stop time

"Capacity of  battery"
capacity_battery = [9000,0,0,0] #batter's capacity_battery, Wh 

"————————————————————————————————————————————"

char_time_start = char_time_start + 1 # make the charging data start to appear on the next hour of start time

"The number of components have to match the number of customers"
pv_allocation = pd.read_csv(r'..\Input_Data\PV_split\Pv_split.csv')
pv_allocation = pv_allocation.iloc[:,1:]

"The parameters you do not need to change"
n_coustomer = number_customers() # number of customers, depend on number of consumptions files you upload
pv = PV(area,panel_efficiency,loss,number_panels)

"Creating Energy flux data file"
for i in range(n_coustomer):
    parameters_consumption = [1,capacity_battery[i],deep_battery,bat_charge_speed,char_time_start,char_time_stop]
    in_file_prefix = r'..\Input_Data\customer_consumption\consumption_data'
    in_file_name = in_file_prefix + str(i) + '.csv' 
    out_file_prefix = r'..\Output_Data\EnergyFlux_data\con_gen_data'
    out_file_name = out_file_prefix + str(i) + '.csv' 
    parameters_consumption[0] =  pv_allocation.iloc[:,i]
    with open(out_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(consumer_profile(in_file_name,pv,parameters_consumption))

#long process here
time.sleep(10)
done = True

"Billing Customers to be added"

print("Please Answer with Yes or No")
