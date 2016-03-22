# ACM40690: Python Assignment 1
# A program to plot the Barnsley Fern
# Alexey Tarutin, 10300685
from pylab import *

N = int(5e5) # Number of points

nx = zeros(N) # initial x value
ny = zeros(N) # initial y value

coeff1 = [0, 0, 0, 0.16, 0, 0]
coeff2 = [-0.15, 0.28, 0.26, 0.24, 0, 0.44]
coeff3 = [0.2, -0.26, 0.23, 0.22, 0, 1.6]
coeff4 = [0.85, 0.04, -0.04, 0.85, 0, 1.6]

def tran(co,nx,ny,i):
    fx = co[0]*nx[i-1]+co[1]*ny[i-1]+co[4]
    fy = co[2]*nx[i-1]+co[3]*ny[i-1]+co[5]
    return (fx, fy)

def simulation():
    for i in range(N):
        rn = randint(100) # Generate probability
        if rn == 0:
            x, y = tran(coeff1, nx, ny, i)
        elif rn < 8 and rn != 0:
            x, y = tran(coeff2, nx, ny, i)
        elif rn < 15 and rn > 7:
            x, y = tran(coeff3, nx, ny, i)
        else:
            x, y = tran(coeff4, nx, ny, i)

        nx[i] = x
        ny[i] = y

    return nx, ny
def plot(nx, ny):
    # Plot the fern
    plot(nx, ny, ls='None', marker='.', ms=1, color='c')
    xlim(-3, 3)
    ylim(-0.1, 10)
    savefig("BFernPlot.png")
    show()

def main():
    nx, ny = simulation()
    plot(nx, ny)
