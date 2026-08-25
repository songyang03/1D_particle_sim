import h5py
import numpy as np
import matplotlib.pyplot as plt
with h5py.File("k0p35_a0p10_nppc500_t40_no_w_sample200.h5", "r") as f:
    m1_amplitude= f["diagnostics"]["m1_amplitude"][:]
    weight_rms = f["diagnostics"]["weight_rms"][:]
    field_energy = f["diagnostics"]["field_energy"][:]
    v=f["particles"]["v"][:]
    x=f["particles"]["x"][:]
    t = np.arange(field_energy.shape[0]) * 0.01
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False  
    fig = plt.figure(figsize=(14, 5))
    ax = fig.add_subplot(1, 1, 1)
    plt.scatter(x[0], v[0], s=5)
    plt.xlabel("x"); plt.ylabel("v")
    plt.show()
 