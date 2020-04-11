#MMAE 350 Homework #6
#Michael Gromski

import matplotlib.pyplot as plt
import scipy
from scipy import optimize



print("")
print("-"*50)
print("Problem 5: Drag force on an airfoil")

def Weight(W):
    Wei = W
    return Wei
def DragForce(U):
    totalDrag = 0.006*U**2 + (0.95/0.6)*(Weight(W)/U)**2
    return totalDrag
Grav_force = []
U_min = []
force_drag = []
for i in range(12000,20001):
    Grav_force.append(i) # This will be our X-axis
    W = i
    wtf = optimize.root(DragForce,1)
    U_min.append(wtf.x)
    force_drag.append(DragForce(wtf.x))

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


fig, host = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

par2.spines["right"].set_position(("axes", 1.2))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)
# Second, show the right spine.
par2.spines["right"].set_visible(False)

p1, = host.plot(Grav_force, force_drag, "b-", label="Fd")
p2, = par1.plot(Grav_force, U_min, "r-", label="U_min")


host.set_xlim(12000, 20000)
host.set_ylim(2250, 4000)
par1.set_ylim(440, 575)

host.set_xlabel("Weight")
host.set_ylabel("Fd")
par1.set_ylabel("U_min")


host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2]

host.legend(lines, [l.get_label() for l in lines])

plt.show()