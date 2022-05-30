import os
import pandas as pd
import numpy as np
from PV import *

  """
  customer_0 is the microbrewery
  customer_x is not the necessary input data. It represents community consumers and only works in the REC model
  """

def number_customers():
    files = os.listdir(r'..\Input_Data\customer_consumption')
    num_customers = len(files)
    return num_customers

def consumption_data(path):
    consumption = pd.read_csv(path)
    return np.array(consumption)

        
def customer_data_profile(path,pv):
    """
    Input parameter:
    annual_consumption, unit KWh
    annual_consumption is the total consumption of consumer
    pv, unit KWh
    PV  has to be a np.array with length of 8760

    Output parameter:
    consumer_data
    consumer_data has 'PV generation','Consumption','Surplus','Grid consumption'
    """
    surplus = []
    grid_con = []
    pv_generation = pv.PVGeneration()
    front_file = pd.read_csv(r'..\Input_Data\front.csv',engine = "python")
    front_matrix = np.array(front_file)
    consumption_curve = consumption_data(path)
    consumer_data = np.hstack((pv_generation,consumption_curve))
    consumer_data = np.hstack((front_matrix,consumer_data))
    for i in range(len(consumer_data)):
        a=consumer_data[i,2]-consumer_data[i,3]
        if a <=0:
            surplus.append(0)
            grid_con.append(-a)
        else:
            surplus.append(a)
            grid_con.append(0)
    surplus = np.array(surplus)
    grid_con = np.array(grid_con)
    s_g=np.transpose(np.vstack((surplus,grid_con)))
    consumer_data=np.hstack((consumer_data,s_g))
    return consumer_data
