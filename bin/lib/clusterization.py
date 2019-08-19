# -*- coding: utf-8 -*-

from sklearn.cluster import MeanShift
import numpy as np
import pandas as pd

def clust(time1):    #11.53:
    
    dx ,dy = [],[]
    te = None
    
    #print(time1)
    
    for i in range(241):
        for j in range(241):
            if not np.isnan(time1[i][j]) and time1[i][j] > 10:
                dx.append(i)
                dy.append(j)

    dim = len(dx)
    
    # Check dimension
    if dim > 4:   
        for x in range(dim):
            dx.append(np.float32('nan'))
            dy.append(np.float32('nan'))

        matrix = np.ndarray(shape=(dim, 2), dtype='float32')
        pt = pd.DataFrame(columns=['x1','y1'])
    
        for x in range(dim):
            matrix[x] = (dx[x], dy[x])
            pt['x1'] = matrix[:,0]
            pt['y1'] = matrix[:,1]
        
        te = pt[['x1','y1']]
          
        #bandwidth = estimate_bandwidth(te, quantile=0.3)
        ms = MeanShift(bandwidth=2, bin_seeding=True, cluster_all=True, min_bin_freq=1,
         n_jobs=None, seeds=None)

        ms.fit(te)
        labels = ms.labels_
        
        #cluster_centers = ms.cluster_centers_
        #n_clusters_ = len(np.unique(labels))
        
#     colors = 10*['r.','g.','b.','c.','k.','y.','m.']
#     for i in range(len(te)):
#            #print(te['x1'][i])
#         plt.plot(te['x1'][i], te['y1'][i], colors[labels[i]], markersize = 10)
#         plt.title('Estimated number of clusters: %d' % n_clusters_)

# #         kmeans = KMeans().fit(te)
# #         labels = kmeans.labels_
# #         cluster_centers = kmeans.cluster_centers_
# #         n_clusters_ = len(np.unique(labels))

        te['cluster']=labels
    return te