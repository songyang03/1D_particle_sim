import torch
import numpy as np
import h5py
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

with h5py.File("k0p35_a0p10_nppc500_t40_no_w_sample200.h5", "r") as f:
    m1_amplitude= f["diagnostics"]["m1_amplitude"][:]
    weight_rms = f["diagnostics"]["weight_rms"][:]
    field_energy = f["diagnostics"]["field_energy"][:]
    v=f["particles"]["v"][:]
    x=f["particles"]["x"][:]
    t = np.arange(field_energy.shape[0]) * 0.01
x=torch.tensor(x, dtype=torch.float32).T
v=torch.tensor(v, dtype=torch.float32).T
# x=x.reshape(800200,1)
# v=v.reshape(800200,1)
# x=x[:600000]
# v=v[:600000]
x=x[1].unsqueeze(1)
v=v[1].unsqueeze(1)
x = (x - x.mean()) / x.std()
v = (v - v.mean()) / v.std()
input=torch.cat((x,v), dim=1)
print(input.shape)
dataset = MyDataset(input, input)
dataloader = DataLoader(
    dataset,
    batch_size=1024,
    shuffle=True,
    num_workers=0,
    drop_last=False,
)
net=torch.nn.Sequential(
    torch.nn.Linear(2, 1),
    torch.nn.ReLU(),
    torch.nn.Linear(1, 2),
)

optimizer = torch.optim.SGD(net.parameters(), lr=0.03)
for epoch in range(20):
 for data in dataloader:
    x, y = data
    optimizer.zero_grad()
    output = net(x)
    loss = torch.nn.functional.mse_loss(output, y)
    loss.backward()
    optimizer.step()
 l=torch.nn.functional.mse_loss(net(input),input)
 print("epoch:", epoch, "loss:", (float(l)))



