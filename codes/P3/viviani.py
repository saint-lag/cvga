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
ZERO = 0
ONE = 1
TWO = 2


# FUNCTIONS
'''def x_sphere(r, phi): return r * np.cos(T) * np.cos(phi)
def y_sphere(r, phi): return r * np.sin(T) * np.sin(phi)
def z_sphere(r): return r * np.cos(T)'''

def x_viviani(r): return (np.cos(T)**2) * r
def y_viviani(r): return np.cos(T) * np.sin(T) * r
def z_viviani(r): return np.sin(T) * r

T = np.linspace(ZERO, SEVENTY*np.pi, T_NUM_5000)
A = np.linspace(ZERO, TWO*np.pi, HUNDRED)


# GENERAL FUNCTIONS
def lines_r3(x, y, z, D):
    T = np.linspace(-D, D, T_NUM_4000)
    X = T * x
    Y = T * y
    Z = T * z
    plt.plot(X, Y, Z, color='black', linewidth=0.5)


def update_viviani(frame, r):
    for plots in [frenet_serret, points, vectors]:
        if len(plots) > ZERO:
            plots.pop().remove()
    
    for line in vectors:
        line.remove()

    vectors.clear()

    current_frenet_serret, = plt.plot(
        x_viviani(r)[:frame+1],
        y_viviani(r)[:frame+1],
        z_viviani(r)[:frame+1], 
        color='firebrick'
    )
    point, = plt.plot(
        x_viviani(r)[frame],
        y_viviani(r)[frame],
        z_viviani(r)[frame], 
        markersize=4
    )
    frenet_serret.append(current_frenet_serret)
    points.append(point)

    
    # Calculate vectors
    T_vector = np.array([x_viviani(r)[frame], y_viviani(r)[frame], z_viviani(r)[frame]])
    N_vector = np.array([-np.sin(T[frame]), np.cos(T[frame]), 0])
    B_vector = np.cross(T_vector, N_vector)

    # Plot vectors
    vector_scale = 0.5
    BLUE = 'blue'
    PINK = 'PINK'
    PURPLE = 'purple'

    tangent_vector, = plt.plot(
        [x_viviani(r)[frame], 
        x_viviani(r)[frame] + vector_scale * T_vector[0]], 
        [y_viviani(r)[frame], y_viviani(r)[frame] + vector_scale * T_vector[1]], 
        [z_viviani(r)[frame], z_viviani(r)[frame] + vector_scale * T_vector[2]], 
        color=BLUE
        )

    normal_vector, = plt.plot([x_viviani(r)[frame], x_viviani(r)[frame] + vector_scale * N_vector[0]],
                            [y_viviani(r)[frame], y_viviani(r)[frame] + vector_scale * N_vector[1]],
                            [z_viviani(r)[frame], z_viviani(r)[frame] + vector_scale * N_vector[2]],
                            color=PINK)

    binormal_vector, = plt.plot([x_viviani(r)[frame], x_viviani(r)[frame] + vector_scale * B_vector[0]],
                                [y_viviani(r)[frame], y_viviani(r)[frame] + vector_scale * B_vector[1]],
                                [z_viviani(r)[frame], z_viviani(r)[frame] + vector_scale * B_vector[2]],
                                color=PURPLE)

    vectors.extend([tangent_vector, normal_vector, binormal_vector])

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
        r = 4

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


        # SPHERE
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
        x = r*np.cos(u)*np.sin(v)
        y = r*np.sin(u)*np.sin(v)
        z = r*np.cos(v)
        
        ax.plot_surface(x, y, z, color="green", alpha=0.3)
        
        try:
            elev_radians = mt.acos(
                (a**2 + b**2) / mt.sqrt((a**2 + b**2 + c**2) * (a**2 + b**2)))
            azimuth_radians = mt.acos(a / mt.sqrt(a**2 + b**2))
        except ZeroDivisionError:
            elev_radians, azimuth_radians = 1.5707963267948966, 1.5707963267948966
        elev = (PI_RAD/np.pi) * elev_radians
        azimuth = (PI_RAD/np.pi) * azimuth_radians
        ax.view_init(elev=elev, azim=azimuth)

        ax.set_box_aspect([np.ptp(c) for c in [ax.get_xlim(), ax.get_ylim(), ax.get_zlim()]])
        ax.set_title('viviani')
        
        
        lines_r3(ONE, ZERO, ZERO, D)
        lines_r3(ZERO, ONE, ZERO, D)
        lines_r3(ZERO, ZERO, ONE, D)

        ani = animation.FuncAnimation(
            fig, update_viviani, fargs=(r,), frames=T_NUM_5000, interval=TWENTY)

        plt.show()
        break
