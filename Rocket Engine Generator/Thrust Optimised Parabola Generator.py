import math
import numpy as np
from bisect import bisect_left
import matplotlib.pyplot as plt

def bell_nozzle(k, aratio, Rt, l_percent):
    entrant_angle = -125
    ea_radian = math.radians(entrant_angle)
    if l_percent == 60:
        Lnp = 0.6
    elif l_percent == 80:
        Lnp = 0.8
    elif l_percent == 90:
        Lnp = 0.9
    else:
        Lnp = 0.7
    angles = find_wall_angles(aratio, throat_radius, l_percent)
    nozzle_length = angles[0]
    theta_n = angles[1]
    theta_e = angles[2]
    data_intervel = 50
    ea_start = ea_radian
    ea_end = -math.pi / 2
    angle_list = np.linspace(ea_start, ea_end, data_intervel)
    xe = []
    ye = []
    for i in angle_list:
        xe.append(1.5 * Rt * math.cos(i))
        ye.append(1.5 * Rt * math.sin(i) + 2.5 * Rt)
    ea_start = -math.pi / 2
    ea_end = theta_n - math.pi / 2
    angle_list = np.linspace(ea_start, ea_end, data_intervel)
    xe2 = []
    ye2 = []
    for i in angle_list:
        xe2.append(0.382 * Rt * math.cos(i))
        ye2.append(0.382 * Rt * math.sin(i) + 1.382 * Rt)
    Nx = 0.382 * Rt * math.cos(theta_n - math.pi / 2)
    Ny = 0.382 * Rt * math.sin(theta_n - math.pi / 2) + 1.382 * Rt
    Ex = Lnp * ((math.sqrt(aratio) - 1) * (Rt/0.7)) / math.tan(math.radians(15))
    Ey = math.sqrt(aratio) * (Rt/1)
    m1 = math.tan(theta_n)
    m2 = math.tan(theta_e)
    C1 = Ny - m1 * Nx
    C2 = Ey - m2 * Ex
    Qx = (C2 - C1) / (m1 - m2)
    Qy = (m1 * C2 - m2 * C1) / (m1 - m2)
    int_list = np.linspace(0, 1, data_intervel)
    xbell = []
    ybell = []
    for t in int_list:
        xbell.append(((1 - t) ** 2) * Nx + 2 * (1 - t) * t * Qx + (t ** 2) * Ex)
        ybell.append(((1 - t) ** 2) * Ny + 2 * (1 - t) * t * Qy + (t ** 2) * Ey)
    nye = [-y for y in ye]
    nye2 = [-y for y in ye2]
    nybell = [-y for y in ybell]
    return angles, (xe, ye, nye, xe2, ye2, nye2, xbell, ybell, nybell)
def find_wall_angles(ar, Rt, l_percent):
    a_ratio = [4, 5, 10, 20, 30, 40, 50, 100]
    theta_n_60 = [20.5, 20.5, 16.0, 14.5, 14.0, 13.5, 13.0, 11.2]
    theta_n_80 = [21.5, 23.0, 26.3, 28.8, 30.0, 31.0, 31.5, 33.5]
    theta_n_90 = [20.0, 21.0, 24.0, 27.0, 28.5, 29.5, 30.2, 32.0]

    theta_e_60 = [26.5, 28.0, 32.0, 35.0, 36.2, 37.1, 35.0, 40.0]
    theta_e_80 = [14.0, 13.0, 11.0, 9.0, 8.5, 8.0, 7.5, 7.0]
    theta_e_90 = [11.5, 10.5, 8.0, 7.0, 6.5, 6.0, 6.0, 6.0]
    f1 = ((math.sqrt(ar) - 1) * Rt) / math.tan(math.radians(15))
    if l_percent == 60:
        theta_n = theta_n_60
        theta_e = theta_e_60
        Ln = 0.6 * f1
    elif l_percent == 80:
        theta_n = theta_n_80
        theta_e = theta_e_80
        Ln = 0.8 * f1
    elif l_percent == 90:
        theta_n = theta_n_90
        theta_e = theta_e_90
        Ln = 0.9 * f1
    else:
        theta_n = theta_n_80
        theta_e = theta_e_80
        Ln = 0.8 * f1
    x_index, x_val = find_nearest(a_ratio, ar)
    if round(a_ratio[x_index], 1) == round(ar, 1):
        return Ln, math.radians(theta_n[x_index]), math.radians(theta_e[x_index])
    if x_index > 2:
        ar_slice = a_ratio[x_index - 2:x_index + 2]
        tn_slice = theta_n[x_index - 2:x_index + 2]
        te_slice = theta_e[x_index - 2:x_index + 2]
        tn_val = interpolate(ar_slice, tn_slice, ar)
        te_val = interpolate(ar_slice, te_slice, ar)
    elif (len(a_ratio) - x_index) <= 1:
        ar_slice = a_ratio[x_index - 2:len(x_index)]
        tn_slice = theta_n[x_index - 2:len(x_index)]
        te_slice = theta_e[x_index - 2:len(x_index)]
        tn_val = interpolate(ar_slice, tn_slice, ar)
        te_val = interpolate(ar_slice, te_slice, ar)
    else:
        ar_slice = a_ratio[0:x_index + 2]
        tn_slice = theta_n[0:x_index + 2]
        te_slice = theta_e[0:x_index + 2]
        tn_val = interpolate(ar_slice, tn_slice, ar)
        te_val = interpolate(ar_slice, te_slice, ar)
    return Ln, math.radians(tn_val), math.radians(te_val)
def interpolate(x_list, y_list, x):
    if any(y - x <= 0 for x, y in zip(x_list, x_list[1:])):
        raise ValueError("x_list must be in strictly ascending order!")
    intervals = zip(x_list, x_list[1:], y_list, y_list[1:])
    slopes = [(y2 - y1) / (x2 - x1) for x1, x2, y1, y2 in intervals]
    if x <= x_list[0]:
        return y_list[0]
    elif x >= x_list[-1]:
        return y_list[-1]
    else:
        i = bisect_left(x_list, x) - 1
        return y_list[i] + slopes[i] * (x - x_list[i])
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx, array[idx]
def plot_nozzle(contour):
    x = contour[0] + contour[6]
    y = contour[1] + contour[7]
    return x, y

"""---Original Variables for Nozzle Plot---"""
# Ratio of specific heats (for exhausts, minimal impact)
k = 1.2
# Nozzle length percntage (60, 80, 90)
l_percent = 80
# Ae / At
aratio = 77.5
# Radius of rocket engine throat
throat_radius = 25
# Calculates the graph points of the nozzle
angles, contour = bell_nozzle(k, aratio, throat_radius, l_percent)

"""---Position of the Chamber Injector---"""
r=-200

"""---Plots of the nozzle bell---"""
x = plot_nozzle(contour)[0]# x-axis
y = plot_nozzle(contour)[1]# y-axis

"""---Plots of the engine chamber---"""
a = [x[0], r]# x-axis
b = [y[0], y[0]]# y-axis


"""---Line for the engine chamber (end section line)---"""
c = [r, r]# x-axis
d = [throat_radius/2, y[0]]# y-axis


"""---Line for the engine nozzle (start section line)---"""
e = [x[x.index(max(x))], x[x.index(max(x))]]# x-axis
f = [throat_radius/2, y[y.index(max(y))]]# y-axis


"""---Graph settings editing """
plt.title("Graphical Representation of Engine Nozzle", fontsize=28)

plt.xlabel("Radial Distance (mm / x-axis)")
plt.ylabel("Axial Distance (mm / y-axis)")
plt.xticks(np.arange(r, max(x)+max(x)/4, 25))
plt.yticks(np.arange(throat_radius/2, max(y)+max(y)/8, 12.5))

plt.subplots_adjust(left=0.0575, bottom=0.0675, right=0.975, top=0.925, wspace=0, hspace=0)
plt.plot(a, b, c, d, e, f, x, y, linestyle="-", color="black", linewidth=1)
plt.text(-235, max(y)+2, 'This is a test label for a rocket engine nozzle graph', fontsize=8, bbox=dict(facecolor='white'))
plt.grid(linestyle='--', linewidth=0.5)

plt.show()
