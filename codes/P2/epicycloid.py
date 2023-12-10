import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import sqrt, acos


# CONSTANTS
T_NUM_4000 = 4000
T_NUM_2000 = 2000

HUNDRED = 100
TWO_HUNDRED = 200
TWENTY_HUNDRED = 20000

SEVENTY = 70
TWENTY_FIVE = 25
ZERO = 0
ONE = 1
TWO = 2


# FUNCTIONS
def x_epicycloid(R, r): return (R+r) * np.cos(T) - r * np.cos((R+r)*T/r)
def y_epicycloid(R, r): return (R+r) * np.sin(T) - r * np.sin((R+r)*T/r)
def z_epicycloid(R, r, a, b, c, d): return (-a*x_epicycloid(R,r)-b*y_epicycloid(R,r)+d)/c

T = np.linspace(ZERO, SEVENTY*np.pi, T_NUM_2000)
A = np.linspace(ZERO, TWO*np.pi, HUNDRED)


# GENERAL FUNCTIONS
def x_outside_circle(r): return r * np.cos(A)
def y_outside_circle(r): return r * np.sin(A)
def z_outside_circle(R, r, a, b, c, d): return (-a * x_outside_circle(r) - b * y_outside_circle(r) + d)/c

def x_inside_circle(R): return R * np.cos(A)
def y_inside_circle(R): return R * np.sin(A)
def z_inside_circle(R, a, b, c, d): return (-a * x_inside_circle(R) - b * y_inside_circle(R) + d)/c

def x_center(R, r): return (R+r) * np.cos(T)
def y_center(R, r): return (R+r) * np.sin(T)
def z_center(R, r, a, b, c, d): return (-a*x_center(R,r)-b*y_center(R,r)+d)/c

def lines_r3(x, y, z, D):
    T = np.linspace(-D, D, T_NUM_4000)
    X = T * x
    Y = T * y
    Z = T * z
    plt.plot(X, Y, Z, color='black', linewidth=0.5)


def update_epicycloid(frame, R, r, a, b, c, d):
    for plots in [epicycloids, outside_circles, points, small_radius]:
        if len(plots) > 0:
            plots.pop().remove()
    epicycloid, = plt.plot(
        x_epicycloid(R, r)[:frame+1], y_epicycloid(R, r)[:frame+1], z_epicycloid(R, r, a, b, c, d)[:frame+1], color='firebrick')
    outside_circle, = plt.plot(
        x_center(R, r)[frame] + x_outside_circle(r), y_center(R, r)[frame] + y_outside_circle(r), z_center(R, r, a, b, c, d)[frame] + z_outside_circle(R, r, a, b, c, d), color='midnightblue')
    point, = plt.plot(
        x_epicycloid(R, r)[frame], y_epicycloid(R, r)[frame], z_epicycloid(R, r, a, b, c, d)[frame], color='red', markersize=3.5)
    epicycloids.append(epicycloid)
    outside_circles.append(outside_circle)
    points.append(point)


if __name__ == '__main__':

    while True:
        # ARRAYS
        epicycloids = []
        outside_circles = []
        points = []
        small_radius = []

        try:
            '''
            # TROCAR STRINGS DE INPUT
            R = float(input("Insira o raio do círculo maior: "))
            r = float(input("Insira o raio do círculo menor: "))
            a = float(input("Insira a: "))
            b = float(input("Insira b: "))
            c = float(input("Insira c: "))
            d = float(input("Insira d: "))
            '''
            r = 3
            R = 4
            a = 1
            b = 1
            c = 1
            d = 1

        except ValueError:
            print('Insira valores do tipo "FLOAT"...')

        # CONSTANTS
        D = (R+r)*2

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.grid()

        ax.set_xlabel('Eixo X')
        ax.axhline(0, color='black', linewidth=1)
        ax.set_xlim(-D, D)

        ax.set_ylabel('Eixo Y')
        ax.axvline(0, color='black', linewidth=1)
        ax.set_ylim(-D, D)

        ax.set_zlabel('Eixo Z')
        ax.set_zlim(-D, D)

        ax.grid()
        ax.set_box_aspect([np.ptp(c) for c in [ax.get_xlim(), ax.get_ylim(), ax.get_zlim()]])
        ax.set_title('epicycloid')
        
        lines_r3(ONE, ZERO, ZERO, D)
        lines_r3(ZERO, ONE, ZERO, D)
        lines_r3(ZERO, ZERO, ONE, D)

        # PLANE
        x_plane, y_plane = np.linspace(-D, D, TWO_HUNDRED), np.linspace(-D, D, TWO_HUNDRED)
        X_plane, Y_plane = np.meshgrid(x_plane, y_plane)
        Z_plane = (-a * X_plane - b * Y_plane + d)/c

        ax.plot_surface(X_plane, Y_plane, Z_plane, color='violet', alpha=.25)

        try:
            elev_radians = acos(
                (a**2 + b**2) / sqrt((a**2 + b**2 + c**2) * (a**2 + b**2)))
            azimuth_radians = acos(a / sqrt(a**2 + b**2))
        except ZeroDivisionError:
            elev_radians, azimuth_radians = 1.5707963267948966, 1.5707963267948966
        elev = (180/np.pi) * elev_radians
        azimuth = (180/np.pi) * azimuth_radians
        ax.view_init(elev=elev, azim=azimuth)

        plt.plot(x_inside_circle(R), y_inside_circle(
            R), z_inside_circle(R, a, b, c, d), color='mediumslateblue')

        ani = animation.FuncAnimation(
            fig, update_epicycloid, fargs=(R, r, a, b, c, d), frames=TWENTY_HUNDRED, interval=TWENTY_FIVE)

        plt.show()
        break
