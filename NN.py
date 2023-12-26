import numpy as np



def sinoid (x):
    return 1/(1+np.exp(-x))


input_lay= np.array([])
output_lay= np.array([])

np.random.seed(1)
weight= 2* np.random.random((250000, 1))- 1
