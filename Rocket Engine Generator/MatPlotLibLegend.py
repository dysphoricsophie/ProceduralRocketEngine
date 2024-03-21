import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
from mplcursors import cursor

def ExhaustVelocity(ex, MaxVel):
    tbr = MaxVel/(((ex+4.5) - (93/20))**0.531)
    if tbr > 100000:
        tbr = (tbr/ 299792458) * 100
    else:
        tbr = tbr/1000
    return tbr
def ExhaustMessage(ex, MaxVel):
    tbr = MaxVel/(((ex+4.5) - (93/20))**0.531)
    if tbr > 100000:
        label = "Average exhaust velocity (%c)"
    else:
        label = "Average exhaust velocity (km/s)"
    return label
def drange(start, stop, step):
    while start < stop:
            yield start
            start += step

MolWts = []
colors = ["red", "blue", "orange", "green", "purple", "gray", "pink", "black"]
items_M = ["R_ISOTOPE", "SOLENG", "LQDENG", "GASENG", "NSWR02", "NSWR98"]
MaxVels = [12400, 24200, 39240, 81620, 156960, 4725000]
items_SOL = ["NORMAL", "LEUNTR", "LPNTR", "CERMET", "PEBBLE"]
SOL_Vels = [11000, 21220, 24200, 19620, 19060]
items_GAS = ["CLOSED", "OPEN"]
GAS_Vels = [40810, 81620]
items_NSWR = ["NORMAL", "ZUBRIN"]
NSWR_Vels = [121200, 156960]
EngineTypes = ["RadioIsotope Engine", "Solid Core Engine", "Liquid Core Engine", "Gaseous Core Engine",
               "NuclearSalt Water (3%)", "NuclearSalt Water (90%)"]

for x in drange(1, 28, 1):
    MolWts.append(x)
xs, fig = np.array(MolWts), pylab.gcf()
fig.canvas.manager.set_window_title('Exhaust Velocity against Exhaust Mass')
plt.subplots_adjust(left=0.05675, bottom=0.065, right=0.98, top=0.825, wspace=0.275, hspace=0.4)

for xe in range(0,6):
    jill, xlabel = "", ""
    CurrMaxVel, EngineType, arrayT, MAIN, arrayT = MaxVels[xe], EngineTypes[xe], [], [], []
    plt.subplot(2, 3, xe+1)
    plt.title(EngineType, fontsize=16)
    if EngineType == "Solid Core Engine":
        for x in MolWts: arrayT.append(ExhaustVelocity(x, SOL_Vels[0]))
        ys1 = np.array(arrayT)
        arrayT = []
        for x in MolWts: arrayT.append(ExhaustVelocity(x, SOL_Vels[1]))
        ys2 = np.array(arrayT)
        arrayT = []
        for x in MolWts: arrayT.append(ExhaustVelocity(x, SOL_Vels[2]))
        ys3 = np.array(arrayT)
        arrayT = []
        for x in MolWts: arrayT.append(ExhaustVelocity(x, SOL_Vels[3]))
        ys4 = np.array(arrayT)
        arrayT = []
        for x in MolWts: arrayT.append(ExhaustVelocity(x, SOL_Vels[4]))
        ys5 = np.array(arrayT)
        arrayT = []
        plt.plot(xs, ys1, marker='.', linestyle="-", color=colors[xe], label=items_SOL[0], linewidth=1.1)
        plt.plot(xs, ys2, marker='.', linestyle="-", color=colors[xe+1], label=items_SOL[1], linewidth=1.1)
        plt.plot(xs, ys3, marker='.', linestyle="-", color=colors[xe+2], label=items_SOL[2], linewidth=1.1)
        plt.plot(xs, ys4, marker='.', linestyle="-", color=colors[xe+3], label=items_SOL[3], linewidth=1.1)
        plt.plot(xs, ys5, marker='.', linestyle="-", color=colors[xe+4], label=items_SOL[4], linewidth=1.1)
        plt.yticks(np.arange(min(ys2) - min(ys3) / 5, max(ys3) + max(ys3) / 10, max(ys3) / 10))
    if EngineType == "Gaseous Core Engine":
        for x in MolWts: arrayT.append(ExhaustVelocity(x, GAS_Vels[0]))
        ys1 = np.array(arrayT)
        arrayT = []
        for x in MolWts: arrayT.append(ExhaustVelocity(x, GAS_Vels[1]))
        ys2 = np.array(arrayT)
        arrayT = []
        plt.plot(xs, ys1, marker='.', linestyle="-", color=colors[xe], label=items_GAS[0], linewidth=1.1)
        plt.plot(xs, ys2, marker='.', linestyle="-", color=colors[xe+1], label=items_GAS[1], linewidth=1.1)
        plt.yticks(np.arange(min(ys1) - min(ys2) / 5, max(ys2) + max(ys2) / 10, max(ys2) / 10))
    if EngineType == "NuclearSalt Water (3%)":
        for x in MolWts: arrayT.append(ExhaustVelocity(x, NSWR_Vels[0]))
        ys1 = np.array(arrayT)
        arrayT = []
        for x in MolWts: arrayT.append(ExhaustVelocity(x, NSWR_Vels[1]))
        ys = np.array(arrayT)
        arrayT = []
        plt.plot(xs, ys1, marker='.', linestyle="-", color=colors[xe], label=items_GAS[0], linewidth=1.1)
        plt.plot(xs, ys2, marker='.', linestyle="-", color=colors[xe+1], label=items_GAS[1], linewidth=1.1)
        plt.yticks(np.arange(min(ys1) - min(ys2) / 5, max(ys2) + max(ys2) / 10, max(ys2) / 10))
    else:
        for x in MolWts: xlabel = ExhaustMessage(x, CurrMaxVel), arrayT.append(ExhaustVelocity(x, CurrMaxVel))
        ys = np.array(arrayT)
        arrayT = []
        plt.plot(xs, ys, marker='.', linestyle="-", color=colors[0], label=items_M[xe], linewidth=1.1)
        plt.yticks(np.arange(min(ys) - min(ys) / 5, max(ys) + max(ys) / 10, max(ys) / 10))
    plt.grid(linestyle='--', linewidth=1)
    plt.xlabel('Average Exhaust products molecular mass (AMU/Da)')
    plt.ylabel(xlabel)
    #cursor(hover=True)
    plt.title(EngineType, fontsize=16)
    plt.xticks(np.arange(0, 30, 2))
    plt.legend(loc="upper right")
plt.suptitle("Exhaust Velocity against Exhaust Mass", fontsize=32)
plt.show()