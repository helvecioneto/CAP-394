#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:21:02 2019

@author: hneto
"""
import pandas as pd

from lib.read_files import readData
from lib.clusterization import clust
from lib.createData import createData
from lib.centroid import centroidData


day = 20140923

def run():
    
    dados = readData(day)
    rrain = dados[0]
    wFiles = pd.DataFrame()
    
    for i in range(len(rrain)):
        clusters = clust(rrain[i])
        dataClusters = createData(day,i,clusters,rrain[i])
        #centroid = centroidData(dataClusters)
        wFiles = wFiles.append(dataClusters)

    wFiles.to_csv('../output/Moderate_Total_OUTPUT_'+str(day)+'.csv')     
    
run()
    
    
