import math
import numpy as np
import matplotlib.pyplot as plt

# Define constants
dt = 0.1  # time step
g = 9.81  # acceleration due to gravity
total_time = 12.1

# Define initial conditions
x = 0.0  # initial horizontal position
y = 0.0  # initial vertical position
vx = 100.0  # initial horizontal velocity
vy = 0.0  # initial vertical velocity
theta = math.pi / 4  # initial angle of launch
vyPlot = []
yPlot = []
vxPlot = []
xPlot = []

# Define target position
target_x = 100.0
target_y = 26-005.0

# Define gains for the controller
Kp = 0.1
Kd = 0.01

# Initialize variables for the controller
error = 0.0
error_deriv = 0.0

def clt(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]

# Simulate rocket flight
while y >= 0.0:
    t = total_time
    # Calculate error
    error = target_x - x
    last_error = error

    # Calculate derivative of error
    error_deriv = (error - last_error) / dt

    # Calculate control signal
    control_signal = Kp * error + Kd * error_deriv

    # Update rocket state
    ax = control_signal * math.cos(theta)  # horizontal acceleration
    ay = control_signal * math.sin(theta) - g  # vertical acceleration
    vx = vx + ax * dt
    vy = vy + ay * dt
    x = x + vx * dt
    y = y + vy * dt

    # Print rocket state
    print("t={:.1f}, x={:.1f}, y={:.1f}, vx={:.1f}, vy={:.1f}, theta={:.1f}, control_signal={:.1f}".format(t, x, y, vx, vy, theta, control_signal))
    vyPlot.append(vy)
    yPlot.append(y)
    vxPlot.append(vx)
    xPlot.append(x)

    total_time = total_time - dt

cep_x_i = xPlot.index(clt(xPlot, target_x))
cep_y_i = yPlot.index(clt(yPlot, target_y))
diff = max(cep_x_i, cep_y_i) - min(cep_x_i, cep_y_i)
dixes = diff/2
minR, maxR = 0, 0
if int(dixes) != float(dixes):
    minR = diff+1
    maxR = diff-1
elif int(dixes) == float(dixes):
    minR = diff
    maxR = diff
x1 = xPlot[minR]
x2 = xPlot[maxR]
y1 = yPlot[minR]
y2 = yPlot[maxR]
x_cep = (x1+x2)/2
y_cep = (y1+y2)/2
print(f"{x_cep}, {y_cep}")

# Plot results
plt.plot(xPlot, yPlot)
plt.plot(target_x, target_y, 'x')
plt.text(x_cep, y_cep, '({}, {})'.format(x_cep, y_cep))
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.show()
