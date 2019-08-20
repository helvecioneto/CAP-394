# -*- coding: utf-8 -*-

import pandas as pd

def centroidData(clus):
    
    if isinstance(clus,pd.DataFrame):
        centroid = pd.DataFrame()
#        print(len(clus['N_Cluster']))
        for i in range(len(clus['N_Cluster'])):
            ct = clus.loc[clus['ID_CLUS'] == i ]
            ct = ct.loc[ct['RAIN_FALL'] == ct['RAIN_FALL'].mean()]
            centroid = centroid.append(ct)
    else:
        return None
    return centroid