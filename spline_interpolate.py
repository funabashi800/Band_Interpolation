from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
import csv

def main():

    data = np.loadtxt('input.csv', delimiter=',')
    k = data[:, 0].tolist()
    energy = data[:, 1].tolist()
    knew = np.linspace(k[0], k[-1], num=len(k)*500)

    # liner interpolation
    liner = interpolate.interp1d(k, energy)

    # 3d spline interpolation
    cubic = interpolate.interp1d(k, energy, kind="cubic")

    # 0d spline interpolation
    zero = interpolate.interp1d(k, energy, kind="zero")

    # 秋間法
    akima = interpolate.Akima1DInterpolator(k, energy)

    plt.plot(k, energy, "o")
    plt.plot(knew, liner(knew), "b", label="Liner interpolation")
    plt.plot(knew, cubic(knew), "r", label="3d Spline interpolation")
    plt.plot(knew, akima(knew), "g", label="Akima interpolation")
    plt.plot(knew, zero(knew), "m", label="0d Spline interpolation")
    plt.xlim([0.99, 1.00])
    plt.ylim([0.40,0.55])
    plt.legend()
    plt.savefig("bandstructure.png")

    # difference 
    dx = (k[-1] - k[0])/len(k)*500
    dot_np = np.gradient(cubic(knew), dx)
    plt.figure()
    plt.plot(knew, dot_np)
    plt.xlim([0.99, 1.00])
    plt.savefig("gradient_1.png")

    dot2_np = np.gradient(dot_np, dx)
    plt.figure()
    plt.plot(knew, dot2_np)
    plt.xlim([0.99, 1.00])
    plt.savefig("gradient_2.png")

    new_band_structure = np.zeros(((len(knew)), 2))
    
    print(len(new_band_structure[:, 0]))
    print(len(knew))
    new_band_structure[:, 0] = knew
    new_band_structure[:, 1] = cubic(knew)
    with open("interpolated_band_structure.csv", "w") as mycsv:
        csvwriter = csv.writer(mycsv, delimiter=',')
        csvwriter.writerows(new_band_structure)
    


if __name__ == "__main__":
    main()