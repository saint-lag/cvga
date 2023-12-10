import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math as mt



# CONSTANTS
T_NUM_5000 = 5000
T_NUM_4000 = 4000
T_NUM_2000 = 2000
PI_RAD = 180

HUNDRED = 100
TWO_HUNDRED = 200
TWENTY_HUNDRED = 20000

SEVENTY = 70
TWENTY_FIVE = 25
TWENTY = 20
ZERO = 0
ONE = 1
TWO = 2


# FUNCTIONS
def x_lissajous(A, a, phi): return A * np.sin(a * T + phi)
def y_lissajous(B, b): return B * np.sin(b * T)
def z_lissajous(A, B, a, b, ap, bp, cp, dp, phi): return (-ap * x_lissajous(A, a, phi) -bp * y_lissajous(B, b) + dp)/cp

T = np.linspace(ZERO, SEVENTY*np.pi, T_NUM_5000)
A = np.linspace(ZERO, TWO*np.pi, HUNDRED)


# GENERAL FUNCTIONS
def lines_r3(x, y, z, D):
    T = np.linspace(-D, D, T_NUM_4000)
    X = T * x
    Y = T * y
    Z = T * z
    plt.plot(X, Y, Z, color='black', linewidth=0.5)

def update_lissajous(frame, A, B, a, b, ap, bp, cp, dp, phi):
    for plots in [lissajouss, points]:
        if len(plots) > ZERO:
            plots.pop().remove()
    lissajous, = plt.plot(
        x_lissajous(A, a, phi)[:frame+1], 
        y_lissajous(B, b)[:frame+1], 
        z_lissajous(A, B, a, b, ap, bp, cp, dp, phi)[:frame+1], color='firebrick'
    )
    point, = plt.plot(
        x_lissajous(A, a, phi)[frame], y_lissajous(B, b)[frame], z_lissajous(A, B, a, b, ap, bp, cp, dp, phi)[frame], markersize=4
    )
    lissajouss.append(lissajous)
    points.append(point)


if __name__ == '__main__':

    while True:
        # ARRAYS
        lissajouss = []
        points = []


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
            A, a, B, b, phi, ap, bp, cp, dp = 4, 2, 6, 3, np.pi*1/5, 4, 2, 6, 3

        except ValueError:
            print('Insira valores do tipo "FLOAT"...')

        # CONSTANTS
        D = (A+B)*2

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
        ax.set_title('lissajous')
        
        lines_r3(ONE, ZERO, ZERO, D)
        lines_r3(ZERO, ONE, ZERO, D)
        lines_r3(ZERO, ZERO, ONE, D)

        # PLANE
        x_plane, y_plane = np.linspace(-D, D, TWO_HUNDRED), np.linspace(-D, D, TWO_HUNDRED)
        X_plane, Y_plane = np.meshgrid(x_plane, y_plane)
        Z_plane = (-ap * X_plane - bp * Y_plane + dp)/cp

        ax.plot_surface(X_plane, Y_plane, Z_plane, color='cyan', alpha=.25)

        try:
            elev_radians = mt.acos(
                (ap**2 + bp**2) / mt.sqrt((ap**2 + bp**2 + cp**2) * (ap**2 + bp**2)))
            azimuth_radians = mt.acos(ap / mt.sqrt(ap**2 + bp**2))
        except ZeroDivisionError:
            elev_radians, azimuth_radians = 1.5707963267948966, 1.5707963267948966
        elev = (PI_RAD/np.pi) * elev_radians
        azimuth = (PI_RAD/np.pi) * azimuth_radians
        ax.view_init(elev=elev, azim=azimuth)

        

        ani = animation.FuncAnimation(
            fig, update_lissajous, fargs=(A, B, a, b, ap, bp ,cp, dp, phi), frames=TWO_HUNDRED*TWO, interval=TWENTY)

        plt.show()
        break
