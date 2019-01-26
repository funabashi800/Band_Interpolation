import matplotlib

import numpy as np
import matplotlib.pyplot as plt
import csv
from julia import Julia
julia = Julia()
julia.eval("@eval Main import Base.MainInclude: include")
from julia import Main
Main.include("interpolate.jl")

data = np.loadtxt('input.csv', delimiter=',')
k = np.array(data[:, 0])
energy = np.array(data[:, 1])
knew = np.linspace(k[0], k[-1], num=k.size*100)

energynew = Main.interpolate(k, energy, knew)

print(energynew)
fig = plt.figure()
plt.plot(k, energy, 'o')
plt.plot(knew, energynew, '-')
plt.ylim([min(energy), max(energy)])
plt.legend(['Raw data','3D spline'], loc='best')
plt.savefig("band_structure.png")

new_band_structure = np.array(((k.size*100)+1, 2))
"""
new_band_structure[:, 0] = knew
new_band_structure[:, 1] = energynew
with open("interpolated_band_structure.csv") as mycsv:
    csvwriter = csv.writer(mycsv, delimiter=',')
    csvwriter.writerows(new_band_structure)
"""