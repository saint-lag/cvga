import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
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
TEN = 10
FIVE = 5
ZERO = 0
ONE = 1
TWO = 2


# FUNCTIONS
def x_helix(r): return r * np.cos(T)
def y_helix(r): return r * np.sin(T)
def z_helix(amp): return amp * T



T = np.linspace(ZERO, SEVENTY*np.pi, T_NUM_5000)
A = np.linspace(ZERO, TWO*np.pi, HUNDRED)


# GENERAL FUNCTIONS
def lines_r3(x, y, z, D):
    T = np.linspace(-D, D, T_NUM_4000)
    X = T * x
    Y = T * y
    Z = T * z
    plt.plot(X, Y, Z, color='black', linewidth=0.5)


def update_helix(frame, r, amp):
    for plots in [frenet_serret, points, vectors]:
        if len(plots) > ZERO:
            plots.pop().remove()
    
    for line in vectors:
        line.remove()

    vectors.clear()

    current_frenet_serret, = plt.plot(
        x_helix(r)[:frame+1],
        y_helix(r)[:frame+1],
        z_helix(amp)[:frame+1], 
        color='firebrick'
    )
    point, = plt.plot(
        x_helix(r)[frame],
        y_helix(r)[frame],
        z_helix(amp)[frame], 
        markersize=4
    )
    frenet_serret.append(current_frenet_serret)
    points.append(point)

    
    # Calculate vectors
    T_vector = np.array([x_helix(r)[frame], y_helix(r)[frame], z_helix(amp)[frame]])
    N_vector = np.array([-np.sin(T[frame]), np.cos(T[frame]), 0])
    B_vector = np.cross(T_vector, N_vector)

    # Plot vectors
    vector_scale = 0.5
    BLUE = 'blue'
    PINK = 'magenta'
    PURPLE = 'purple'

    tangent_vector, = plt.plot(
        [x_helix(r)[frame], 
        x_helix(r)[frame] + vector_scale * T_vector[0]], 
        [y_helix(r)[frame], y_helix(r)[frame] + vector_scale * T_vector[1]], 
        [z_helix(amp)[frame], z_helix(amp)[frame] + vector_scale * T_vector[2]], 
        color=BLUE
        )

    normal_vector, = plt.plot([x_helix(r)[frame], x_helix(r)[frame] + vector_scale * N_vector[0]],
                            [y_helix(r)[frame], y_helix(r)[frame] + vector_scale * N_vector[1]],
                            [z_helix(amp)[frame], z_helix(amp)[frame] + vector_scale * N_vector[2]],
                            color=PINK)

    binormal_vector, = plt.plot([x_helix(r)[frame], x_helix(r)[frame] + vector_scale * B_vector[0]],
                                [y_helix(r)[frame], y_helix(r)[frame] + vector_scale * B_vector[1]],
                                [z_helix(amp)[frame], z_helix(amp)[frame] + vector_scale * B_vector[2]],
                                color=PURPLE)

    vectors.extend([tangent_vector, normal_vector, binormal_vector])

    '''# View
    azimuth = (PI_RAD/np.pi) * np.arctan2(y_helix(r)[frame], x_helix(r)[frame])
    elev = np.arctan2(z_helix(amp)[frame], np.sqrt(x_helix(r)[frame]**2 + y_helix(r)[frame]**2))
    ax.view_init(elev=elev, azim=azimuth)'''

if __name__ == '__main__':

    while True:
        # ARRAYS
        frenet_serret = []
        points = []
        vectors = []


        try:
            '''
            # TROCAR STRINGS DE INPUT
            r = float(input("Insira o raio da esfera: "))
            a = float(input("Insira a: "))
            b = float(input("Insira b: "))
            c = float(input("Insira c: "))
            d = float(input("Insira d: "))
            '''

        except ValueError:
            print('Insira valores do tipo "FLOAT"...')

        # CONSTANTS
        a, b, c, d = 2, 2, 2, 2
        A, B = 2, 2

        r = 5
        amp = 1/3
    

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
        
        try:
            elev_radians = mt.acos(
                (a**2 + b**2) / mt.sqrt((a**2 + b**2 + c**2) * (a**2 + b**2)))
            azimuth_radians = mt.acos(a / mt.sqrt(a**2 + b**2))
        except ZeroDivisionError:
            elev_radians, azimuth_radians = 1.5707963267948966, 1.5707963267948966


        ax.set_box_aspect([np.ptp(c) for c in [ax.get_xlim(), ax.get_ylim(), ax.get_zlim()]])
        ax.set_title('helix')
        
        
        lines_r3(ONE, ZERO, ZERO, D)
        lines_r3(ZERO, ONE, ZERO, D)
        lines_r3(ZERO, ZERO, ONE, D)

        ani = animation.FuncAnimation(
            fig, update_helix, fargs=(r, amp), frames=TWO_HUNDRED, interval=FIVE)

        plt.show()
        break
