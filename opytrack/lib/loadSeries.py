import xarray as xr
import os
import numpy as np

dataPath = 'data/'

def readFiles(date):
    sdate = date.isoformat()

    year   = sdate[0:4]
    month  = sdate[5:7]
    day    = sdate[8:10]
    hour   = sdate[11:13]
    minute = sdate[14:16]
    second = sdate[17:19]
    extension = '.nc'
    
    initialFile = ('sbmn_rain_rates_'+year+month+day+'_'+hour+minute+second+extension)
    
    interval = 10
    frames = np.zeros ((interval,241,241))
    
    for i in range(interval-1,-1,-1):
        file = (sorted(os.listdir(dataPath+year+month+day),reverse=True)[i])
        print('File Loaded at times :',i,file)
        lr = xr.open_dataset(dataPath+year+month+day+'/'+file)
        rr = lr.rain_rate
        frames[i] = rr
    
    return frames
