import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d
import numpy as np

# PRESETS

fig = plt.figure()
ax = plt.axes(projection='3d')


K = 1/4

r = 30
R = r*K

V = abs(R/r)

D = (R+r)*2

ax.set_xlabel('Eixo X')
ax.set_xlim(-D,D)

ax.axhline(0,color = 'black', linewidth = 1)
ax.set_ylabel('Eixo Y')

ax.set_ylim(-D,D)
ax.axvline(0,color = 'black', linewidth = 1)

ax.set_zlim(-D,D)

ax.grid()

ax.set_aspect('equal')
ax.set_title('hypocycloid')

T = np.linspace(0,70*np.pi,2000)
A = np.linspace(0,2*np.pi,100)


# FUNCTIONS

x_hypocycloid = (R-r) * np.cos(T) + r * np.cos((R-r)*T/r)
y_hypocycloid = (R-r) * np.sin(T) + r * np.sin((R-r)*T/r)


x_outside_circle, y_outside_circle = r * np.cos(A), r * np.sin(A)
x_inside_circle, y_inside_circle = R * np.cos(A), R * np.sin(A)


# ARRAYS

hypocycloids = []
outside_circles = []
points = []
small_radius = []

#ax = plt.figure().add_subplot(projection='3d')


plt.plot(x_inside_circle, y_inside_circle, color = 'mediumslateblue')

def update(frame):
    for plots in [hypocycloids,outside_circles,points,small_radius]:
        if len(plots)>0:
            plots.pop().remove()
    hypocycloid, = plt.plot(x_hypocycloid[:frame+1], y_hypocycloid[:frame+1],color = 'firebrick')
    outside_circle, = plt.plot(x_center[frame] + x_outside_circle, y_center[frame] + y_outside_circle, color = 'midnightblue')
    point, = plt.plot(x_hypocycloid[frame],y_hypocycloid[frame],'ko',color = 'red',markersize = 3.5)
    hypocycloids.append(hypocycloid)
    outside_circles.append(outside_circle)
    points.append(point)


x_center = (R-r) * np.cos(T)
y_center = (R-r) * np.sin(T)
#z_center = (R-r) * np.sin(T)

ani = animation.FuncAnimation(fig, update, frames=2000, interval=75*V)


plt.show()
