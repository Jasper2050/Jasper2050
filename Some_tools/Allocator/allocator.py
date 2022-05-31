# -*- coding: utf-8 -*-

import pandas as pd

"The parameters that need to be adjusted according to DR/REC model"
"————————————————————————————————————————————"

day = [[1,0,0,0]]

week = [[1,,,],
        [1,,,],
        [1,,,],
        [1,,,],
        [1,,,],
        [1,,,],
        [1,,,]]

option = 'Week' # Week or Day

"————————————————————————————————————————————"

day = pd.DataFrame(day)
week = pd.DataFrame(week)

file = pd.DataFrame([])

if option == 'Week':
    for z in range(int(8760/7)):
        file = pd.concat([file,week],axis=0)
    file = pd.concat([file,week.iloc[:3,:]])
    
if option == 'Day':
    for z in range(int(8760)):
        file = pd.concat([file,day],axis=0)

 
file.to_csv('Pv_split.csv')
