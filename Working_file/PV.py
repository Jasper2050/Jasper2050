import pandas as pd
import numpy as np

class PV:

    def __init__(self,area=2.5764,panel_efficiency=0.203,loss=0.8,number_panels=40): #PV parameters
                 
        "Initialize PV data"
        self.area = area
        self.panel_efficiency = panel_efficiency
        self.loss = loss
        self.number_panels = number_panels
        
        "Initialize consumption data"
        
    def PVGeneration(self):
        "generate PV generation profile"
        path1 = pd.read_csv(r'..\Input_Data\irradiation\irradiation_file.csv',engine = "python")
        irradiation = np.array(path1.loc[:,['Irradiation_W']])
        pv_generation = irradiation*self.area*self.panel_efficiency*self.loss*self.number_panels
        return np.array(pv_generation)

    def ss(self):
        return(self.area)
