import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# CONSTANTS
T_NUM_4000 = 4000
T_NUM_2000 = 2000

HUNDRED = 100
ZERO = 0
SEVENTY = 70
TWO = 2


# FUNCTIONS
def x_hypocycloid(r, k): return r*(k-1)*np.cos(T) + r*np.cos((k-1)*T)
def y_hypocycloid(r, k): return r*(k-1)*np.sin(T) - r*np.sin((k-1)*T)


T = np.linspace(ZERO, SEVENTY*np.pi, T_NUM_2000)
A = np.linspace(ZERO, TWO*np.pi, HUNDRED)


# GENERAL FUNCTIONS
def x_outside_circle(r): return r * np.cos(A)
def y_outside_circle(r): return r * np.sin(A)


def x_inside_circle(R): return R * np.cos(A)
def y_inside_circle(R): return R * np.sin(A)


def x_center(R, r): return (R-r) * np.cos(T)
def y_center(R, r): return (R-r) * np.sin(T)


def lines_r3(x, y, z, D):
    T = np.linspace(-D, D, T_NUM_4000)
    X = T * x
    Y = T * y
    Z = T * z
    plt.plot(X, Y, Z, color='black', linewidth=0.5)


def update_hypocycloid(frame, R, r, K):
    for plots in [hypocycloids, outside_circles, points, small_radius]:
        if len(plots) > 0:
            plots.pop().remove()
    hypocycloid, = plt.plot(
        x_hypocycloid(r, K)[:frame+1], y_hypocycloid(r, K)[:frame+1], color='firebrick')
    outside_circle, = plt.plot(
        x_center(R, r)[frame] + x_outside_circle(r), y_center(R, r)[frame] + y_outside_circle(r), color='midnightblue')
    point, = plt.plot(
        x_hypocycloid(r, K)[frame], y_hypocycloid(r, K)[frame], color='red', markersize=3.5)
    if frame > 0:
        small_radius_line, = plt.plot(
            [x_center(R, r)[frame - 1], x_hypocycloid(r, K)[frame - 1]],
            [y_center(R, r)[frame - 1], y_hypocycloid(r, K)[frame - 1]],
            linestyle='dashed', color='green'
        )
    hypocycloids.append(hypocycloid)
    outside_circles.append(outside_circle)
    points.append(point)

    if frame > 0:
        small_radius.append(small_radius_line)

if __name__ == '__main__':

    while True:
        # ARRAYS
        hypocycloids = []
        outside_circles = []
        points = []
        small_radius = []

        try:
            '''
            # TROCAR STRINGS DE INPUT
            K = float(input("Insira K: "))
            r = float(input("Insira o raio do círculo menor: "))
            '''
            K = 4
            r = 4

        except ValueError:
            print('Insira valores do tipo "FLOAT"...')

        # CONSTANTS
        R = r*K
        V = abs(R/r)
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
        ax.set_title('hypocycloid')

        lines_r3(1, 0, 0, D)
        lines_r3(0, 1, 0, D)
        lines_r3(0, 0, 1, D)

        # PLANE
        x_plane, y_plane = np.linspace(-D, D, 200), np.linspace(-D, D, 200)
        X_plane, Y_plane = np.meshgrid(x_plane, y_plane)

        plt.plot(x_inside_circle(R), y_inside_circle(
            R), color='mediumslateblue')

        ani = animation.FuncAnimation(
            fig, update_hypocycloid, fargs=(R, r, K), frames=500, interval=SEVENTY)

        plt.show()
        break
