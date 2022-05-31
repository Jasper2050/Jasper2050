import pandas as pd
import numpy as np
import csv

"The parameters can be adjusted"
"————————————————————————————————————————————"
annual_consumption = 42599.56  #  unit kWh

"————————————————————————————————————————————"

def consumption_curve(annual_consumption):

    """
    Input parameter:
    annual_consumption, unit KWh

    Output parameter:
    c_curve is the consumption curve of consumer, unit KWh
    """
        
    df_consumption_curve = pd.read_csv(r'consumption_curve.csv')
    sum_consumption=sum(df_consumption_curve.loc[:,'CONSUMPTION'])
    c_curve=1000*df_consumption_curve.loc[:,'CONSUMPTION']*annual_consumption/sum_consumption
    
    return c_curve


file_name = 'consumption_data'
curve = consumption_curve(annual_consumption)
curve.to_csv(file_name,index=False)
