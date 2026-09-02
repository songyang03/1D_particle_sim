import torch
import numpy as np
import h5py
with h5py.File("k0p35_a0p10_nppc500_t40_no_w_sample200.h5", "r") as f:
    m1_amplitude= f["diagnostics"]["m1_amplitude"][:]
    weight_rms = f["diagnostics"]["weight_rms"][:]
    field_energy = f["diagnostics"]["field_energy"][:]
    v=f["particles"]["v"][:]
    x=f["particles"]["x"][:]
    t = np.arange(field_energy.shape[0]) * 0.01
x=torch.tensor(x, dtype=torch.float32).T
v=torch.tensor(v, dtype=torch.float32).T
net=torch.nn.Sequential(
    torch.nn.Linear(2, 1),
    torch.nn.ReLU(),
    torch.nn.Linear(1, 2)
)

print(x.shape, v.shape)

