#MMAE 350 Homework #6 Problem #6d
#Michael Gromski 

import matplotlib.pyplot as plt
from scipy import optimize

print("")
print("-"*50)
print("Problem 5: Drag force on an airfoil")

def DragForce(U):
    totalDrag = 0.006*U**2 + (0.95/0.6)*(W/U)**2    #primary function given 
    return totalDrag
Grav_force = []
U_min = []
force_drag = []
for i in range(12000,20001):                        #range depends on weight range
    Grav_force.append(i)                            #This will be our X-axis
    W = i                                           #Set our weight value
    DF = optimize.fminbound(DragForce,300,700)               
    U_min.append(DF)
    force_drag.append(DragForce(DF))

fig, host = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = host.twinx()

p1, = host.plot(Grav_force, force_drag, "b-", label="Drag Force")
p2, = par1.plot(Grav_force, U_min, "r-", label="Associated Velocity")

host.set_xlim(12000, 20000)
host.set_ylim(2250, 4000)
par1.set_ylim(440, 575)

host.set_title("Corresponding Drag and Velocity to Weight")
host.set_xlabel("Weight")
host.set_ylabel("Minimum Drag Force")
par1.set_ylabel("Velocity")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2]

host.legend(lines, [l.get_label() for l in lines])

plt.show()