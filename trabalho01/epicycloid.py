import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# PRESETS
fig = plt.figure()
ax = plt.axes(projection='3d')

r = 1/20

V = abs(r)

K = 10*(1/V)

D = r*2

ax.set_xlabel('Eixo X')
ax.set_xlim(-D,D)

ax.axhline(0,color = 'black', linewidth = 1)
ax.set_ylabel('Eixo Y')

ax.set_ylim(-D,D)
ax.axvline(0,color = 'black', linewidth = 1)

ax.set_zlim(-D,D)

ax.grid()

ax.set_aspect('equal')
ax.set_title('Epicicloide')

T = np.linspace(0,70*np.pi,2000)
A = np.linspace(0,2*np.pi,100)


# FUNCTIONS

x_helix = r * np.cos(T)
y_helix = r * np.sin(T)
z_helix = r

x_outside_circle, y_outside_circle = r * np.cos(A), r * np.sin(A)
x_inside_circle, y_inside_circle = r * np.cos(A), r * np.sin(A)


# ARRAYS

function = []
outside_circles = []
points = []

plt.plot(x_inside_circle, y_inside_circle, color = 'mediumslateblue')

def update(frame):
    for plots in [function,outside_circles,points]:
        if len(plots)>0:
            plots.pop().remove()
    curve, = plt.plot(x_helix[:frame+1], y_helix[:frame+1] ,color = 'firebrick')
    outside_circle, = plt.plot(x_center[frame] + x_outside_circle, y_center[frame] + y_outside_circle, color = 'midnightblue')
    point, = plt.plot(x_helix[frame],y_helix[frame],'ko',color = 'red', markersize = 3.5)
    function.append(curve)
    outside_circles.append(outside_circle)
    points.append(point)


x_center = r * np.cos(T)
y_center = r * np.sin(T)

ani = animation.FuncAnimation(fig, update, frames=2000, interval=75*V)

