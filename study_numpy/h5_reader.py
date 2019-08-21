import numpy as np
import h5py

hf = h5py.File('data.gz.h5', 'r')
print(hf.keys())
n1 = np.array(hf.get('dataset_1'))
print(n1.shape)

hf.close()
