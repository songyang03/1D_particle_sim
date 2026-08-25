import h5py
import numpy as np
import matplotlib.pyplot as plt
with h5py.File("k0p35_a0p10_nppc500_t40_no_w_sample200.h5", "r") as f:
    m1_amplitude= f["diagnostics"]["m1_amplitude"][:]
    weight_rms = f["diagnostics"]["weight_rms"][:]
    field_energy = f["diagnostics"]["field_energy"][:]
    v=f["particles"]["v"]
    x=f["particles"]["x"]
    t = np.arange(field_energy.shape[0]) * 0.01
    fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
    axes[0].plot(t, field_energy);  axes[0].set_ylabel("field_energy")
    axes[1].plot(t, m1_amplitude);  axes[1].set_ylabel("m1_amplitude")
    axes[2].plot(t, weight_rms); axes[2].set_ylabel("weight_rms")
    axes[2].set_xlabel("time (s)")
    plt.tight_layout()
    plt.show()