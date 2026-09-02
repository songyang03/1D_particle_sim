import numpy as np
from scipy.spatial import cKDTree
from particle.dmi import dmi
import h5py
import matplotlib.pyplot as plt
def fnn(series, tau, max_dim=10, R_tol=10.0,
        theiler=0):
    series = np.asarray(series, dtype=float)
    n = len(series)
    max_offset = (max_dim - 1) * tau
    centers = np.arange(n - max_offset)
    num = len(centers)
    k=list()
    for m in range(1, max_dim + 1):
        M = np.column_stack([series[centers + k * tau] for k in range(m)])
        tree = cKDTree(M[:-1])
        dists, idx = tree.query(M[:-1], k=2)
        ncount = 0
        for i in range(num-1):
            j = idx[i, 1]
            if abs(i - j) <= theiler:
                continue
            R_m = dists[i, 1]
            R_m1 = np.linalg.norm(M[i+1] - M[j+1])
            if R_m == 0:
                continue
            if (R_m1 / R_m > R_tol) :
                ncount += 1
        k.append(ncount / (num-m+1))     
    return k
if __name__ == "__main__": 
    with h5py.File("k0p35_a0p10_nppc500_t40_no_w_sample200.h5", "r") as f:
        m1_amplitude= f["diagnostics"]["m1_amplitude"][:]
        weight_rms = f["diagnostics"]["weight_rms"][:]
        field_energy = f["diagnostics"]["field_energy"][:]
        v=f["particles"]["v"][:]
        x=f["particles"]["x"][:]
        t = np.arange(field_energy.shape[0]) * 0.01

        a=list()
        for i in range(200):
            p=fnn(x[:1000,i], 1,2)
            a.append(p[0])
        fig, ax = plt.subplots()
        ax.plot(range(1, len(a) + 1), a, "o-")
        ax.set_title("FNN Method")
        plt.show()
        print(a)


        # num=103
        # p=fnn(x[:,num], 1)
        # fig, ax = plt.subplots(1,2)
        # ax[0].plot(range(1, len(p) + 1), p, "o-")
        # ax[0].set_title("FNN Method")
        # ax[1].plot(x[:,num], v[:,num])  
        # ax[1].set_title("Particle Phase Space")
        # ax[1].set_xlabel("x"); ax[1].set_ylabel("v")  
        # plt.show()