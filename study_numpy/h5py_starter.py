import numpy as np
import h5py

d1 = np.random.random(size = (10000,1000,4))
d2 = np.random.random(size = (10000,200))

print(d1.shape, d2.shape)

hf = h5py.File('data.gz.h5', 'w')

compress_mode = True

if compress_mode:
    hf.create_dataset('dataset_1', data=d1, compression="gzip", compression_opts=9)
    hf.create_dataset('dataset_2', data=d2, compression="gzip", compression_opts=9)
else:
    hf.create_dataset('dataset_1', data=d1)
    hf.create_dataset('dataset_2', data=d2)

hf.close()