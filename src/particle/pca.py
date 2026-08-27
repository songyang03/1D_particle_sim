from sklearn.decomposition import PCA
import h5py
import numpy as np
from particle.dmi import dmi
from particle.fnn import fnn
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
with h5py.File("k0p35_a0p10_nppc500_t40_no_w_sample200.h5", "r") as f:
    v=f["particles"]["v"][:]
    x=f["particles"]["x"][:]
    count=0
    a=list()
    for p in [5]:
        X = np.column_stack([x[3000:3100,p], v[3000:3100,p]])   # (1000, 2)
        pac=PCA(n_components=2)
        scaler = StandardScaler()
        X_z = scaler.fit_transform(X) 
        pca = pac.fit(X_z)
        loadings = pac.components_    # 载荷矩阵 V，每行是一个主成分
        mean = pac.mean_    
        for j, pc in enumerate(loadings):
            print(f"PC{j+1} = "f"{pc[0]:.4f}·x + {pc[1]:.4f}·v")  

        # print(X_z.shape)
        # pca = PCA().fit(X_z)
        evr = pca.explained_variance_ratio_
        print(f"主成分方差占比: {np.round(evr,4)}")

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