import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
COLORED =False
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
    # if COLORED:
    #     scat = ax.scatter([], [], s=8, c=[], cmap="viridis", vmin=0)
    # else:
    scat = ax.scatter([], [], s=8, color="tab:blue", alpha=0.8)
    time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes,
                    va="top", fontsize=12)
    def update(i):
        xi = x[i]
        vi = v[i]
        scat.set_offsets(np.column_stack([xi, vi]))
        # if COLORED:
        #     scat.set_array(np.hypot(xi - xi.mean(), vi - vi.mean()))
        time_text.set_text(f"t = {i * 0.01:.2f} s")
        return scat, time_text
    # print(x[0][0], v[0][0])
    frames = np.arange(0, 4000, 4)
    xmin, xmax = 0.0, 18.0
    vmin, vmax = v.min(), v.max()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(vmin, vmax)
    ax.set_xlabel("x")
    ax.set_ylabel("v")
    ax.set_title("200 particles in phase space")
    ax.set_aspect("auto")
    ani = FuncAnimation(fig, update, frames=frames, interval=40, blit=True)

    
    # a=list()
    # for i in range(200):
    #     c1=0
    #     c2=0
    #     for j in range(4000):
    #         if v[j][i]>0:
    #             c1+=1
    #         elif v[j][i]<0:
    #             c2+=1
    #         if c1!=0 and c2!=0:
    #             break
    #     if c1!=0 and c2!=0:
    #          a.append(i)   
    # print(a)


    # plt.scatter(x[:,30], v[:,30], s=1)
    # plt.xlabel("x"); plt.ylabel("v")

    # ax.plot(x[:,58], v[:,58])  
    # ax.set_title("Particle Phase Space")
    # ax.set_xlabel("x"); ax.set_ylabel("v")  

    plt.show()
