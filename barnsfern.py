# ACM40690: Python Assignment 1
# A program to plot the Barnsley Fern
# Alexey Tarutin, 10300685
from pylab import *

nx = [0.0] # initial x value
ny = [0.0] # initial y value

# coeff*=[a,b,c,d,e,f] if looking at Wikipedia
coeff1=[0, 0, 0, 0.16, 0, 0]
coeff2=[-0.15, 0.28, 0.26, 0.24, 0, 0.44]
coeff3=[0.2, -0.26, 0.23, 0.22, 0, 1.6]
coeff4=[0.85, 0.04, -0.04, 0.85, 0, 1.6]

# NB: These values may be changed to create mutant varieties.
#     For example, a Thelypteridaceae fern is created using
# coeff1=[0,0,0,0.25,0,0]
# coeff2=[-0.04,0.2,0.16,0.04,0.083,0.12]
# coeff3=[0.035,-0.2,0.16,0.04,-0.09,0.02]
# coeff4=[0.95,0.005,-0.005,0.93,-0.002,0.5]
# You may comment out the originals and uncomment these and see what it draws.

# Below are functions to initialise the transformation.
def xtran(co,nx,ny,i):
    fx=co[0]*nx[i-1]+co[1]*ny[i-1]+co[4]
    return fx

def ytran(co,nx,ny,i):
    fy=co[2]*nx[i-1]+co[3]*ny[i-1]+co[5]
    return fy

# NB: The xrange() command is obsolete in Python3, its role now covered by range(). For the sake of the module, I reverted to Python2.7
for i in xrange(1,350000):
    rn=randint(100) # Generate probability
    # Coordinate 1: Proba 0.01, draw stem
    if rn==0:
        x=xtran(coeff1,nx,ny,i)
        y=ytran(coeff1,nx,ny,i)
    # Coordinate 2: Proba 0.07, draw fronds on left
    elif rn < 8 and rn != 0:
        x=xtran(coeff2,nx,ny,i)
        y=ytran(coeff2,nx,ny,i)
    # Coordinate 3: Proba 0.07, draw fronds on right
    elif rn < 15 and rn > 7:
        x=xtran(coeff3,nx,ny,i)
        y=ytran(coeff3,nx,ny,i)
    # Coordinate 4: Proba 0.85, draw complete fern
    else:
        x=xtran(coeff4,nx,ny,i)
        y=ytran(coeff4,nx,ny,i)

    nx.append(x)
    ny.append(y)

# Plot the fern
plot(nx, ny, ls='None', marker='.', ms=1, color='c')
grid(True)
xlim(-3, 3)
ylim(-0.1, 10)
savefig("BFernPlot.png")
show()
