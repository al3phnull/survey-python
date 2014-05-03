# ACM40690: Python Assignment 2
# Solve Laplace's equation on a grid shaped
# like the the first letter of your name.
# Alexey Tarutin, 10300685

from pylab import *
from matplotlib import cm

Nx = 20
Ny = 20
N = int(1e3)

u = zeros((Nx,Ny))

u[0][:] = Ny-1
u[Ny-1][:] = 0

for i in range(Nx):
    u[i][0]=Nx-1-i
    u[i][Nx-1]=Nx-1-i

def letter(u):
    for i in range((Nx/2)-Nx/10,(Nx/2)+Nx/10+1):
        for j in range((Ny/2)-Nx/10,(Ny/2)+Nx/10+1):
            u[i][(Ny/2)-Nx/10] = Ny/2
            u[i][(Ny/2)+Nx/10] = Ny/2
            u[(Ny/2)-Nx/10][j] = Ny/2
            u[Ny/2][j] = Ny/2
    return u

u = letter(u)

for p in range(N):
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            u[i][j] = 0.25*(u[i+1][j]+u[i-1][j]+u[i][j+1]+u[i][j-1])
    u = letter(u)

v = arange(Ny) + 0.5

contour(u, v, colors='k')
colorbar(imshow(u, cmap = cm.Accent))
savefig("SolutionPlot.png")
show()
