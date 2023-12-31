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
def x_hypotrocycloid(R, r, d): return (R-r) * np.cos(T) + d * np.cos((R-r)*T/r)
def y_hypotrocycloid(R, r, d): return (R-r) * np.sin(T) + d * np.sin((R-r)*T/r)


T = np.linspace(ZERO, SEVENTY*np.pi, T_NUM_2000)
A = np.linspace(ZERO, TWO*np.pi, HUNDRED)


# GENERAL FUNCTIONS
def x_outside_circle(d): return d * np.cos(A)
def y_outside_circle(d): return d * np.sin(A)


def x_inside_circle(R): return R * np.cos(A)
def y_inside_circle(d): return d * np.sin(A)


def x_center(R, r): return (R-r) * np.cos(T)
def y_center(R, r): return (R-r) * np.sin(T)


def lines_r3(x, y, z, D):
    T = np.linspace(-D, D, T_NUM_4000)
    X = T * x
    Y = T * y
    Z = T * z
    plt.plot(X, Y, Z, color='black', linewidth=0.5)


def update_hypotrocycloid(frame, R, r, d):
    for plots in [hypotrocycloids, outside_circles, points, dislocated_radius]:
        if len(plots) > 0:
            plots.pop().remove()
    hypotrocycloid, = plt.plot(
        x_hypotrocycloid(R, r, d)[:frame+1], y_hypotrocycloid(R, r, d)[:frame+1], color='firebrick')
    outside_circle, = plt.plot(
        x_center(R, r)[frame] + x_outside_circle(r), y_center(R, r)[frame] + y_outside_circle(r), color='midnightblue')
    point, = plt.plot(
        x_hypotrocycloid(R, r, d)[frame], y_hypotrocycloid(R, r, d)[frame], color='red', markersize=3.5)
    if frame > 0:
        dislocated_radius_line, = plt.plot(
            [x_center(R, r)[frame - 1], x_hypotrocycloid(R, r, d)[frame - 1]],
            [y_center(R, r)[frame - 1], y_hypotrocycloid(R, r, d)[frame - 1]],
            linestyle='dashed', color='green'
        )
    hypotrocycloids.append(hypotrocycloid)
    outside_circles.append(outside_circle)
    points.append(point)

    if frame > 0:
        dislocated_radius.append(dislocated_radius_line)


if __name__ == '__main__':

    while True:
        # ARRAYS
        hypotrocycloids = []
        outside_circles = []
        points = []
        dislocated_radius = []

        try:
            '''
            # TROCAR STRINGS DE INPUT
            R = float(input("Insira o raio do círculo maior: "))
            r = float(input("Insira o raio do círculo menor: "))
            d = float(input("Insira d: "))
            '''
            r = 3
            R = 5
            d = 6

        except ValueError:
            print('Insira valores do tipo "FLOAT"...')

        # CONSTANTS
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
        ax.set_title('hypotrocycloid')

        lines_r3(1, 0, 0, D)
        lines_r3(0, 1, 0, D)
        lines_r3(0, 0, 1, D)

        # PLANE
        x_plane, y_plane = np.linspace(-D, D, 200), np.linspace(-D, D, 200)
        X_plane, Y_plane = np.meshgrid(x_plane, y_plane)

        plt.plot(x_inside_circle(R), y_inside_circle(
            R), color='mediumslateblue')

        ani = animation.FuncAnimation(
            fig, update_hypotrocycloid, fargs=(R, r, d), frames=500, interval=SEVENTY)

        plt.show()
        break
