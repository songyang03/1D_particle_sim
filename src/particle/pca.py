from sklearn.decomposition import PCA
import h5py
import numpy as np
from particle.dmi import dmi
from particle.fnn import fnn
import matplotlib.pyplot as plt
with h5py.File("k0p35_a0p10_nppc500_t40_no_w_sample200.h5", "r") as f:
    v=f["particles"]["v"][:]
    x=f["particles"]["x"][:]
    count=0
    a=list()
    for p in [2]:
        X = np.column_stack([x[:, p], v[:, p]])   # (200, 2)
        pac=PCA(n_components=1)
        pca = pac.fit_transform(X)
        loadings = pac.components_    # 载荷矩阵 V，每行是一个主成分
        mean = pac.mean_    
        for j, pc in enumerate(loadings):
             print(f"PC{j+1} = "f"{pc[0]:.4f}·x + {pc[1]:.4f}·v")    
        # tau=dmi(pca[:,0])
        # k=fnn(pca[:,0], tau)
        # a.append(k[0])
        # print(pca.shape)
        # print(x[:,p].shape)
    # fig, ax = plt.subplots()
    # ax.plot(range(1, len(a) + 1), a, "o-")
    # ax.set_title("FNN Method")
    # plt.show()
    # print(a)