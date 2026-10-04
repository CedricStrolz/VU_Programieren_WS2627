import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

'''
Schreiben Sie eine Funktion die als Input einen String bekommt der die Summenformel eines Moleküls darstellen soll (z.B. C6H12O6),
und die Molmasse der Substanz in g/mol zurückgibt. Gehen Sie davon aus, dass die Eingabe immer dem Muster „Element1Index1Element2Index2…“ folgt.
Ein Wassermolekül würde beispielsweise als Eingabe „H2O1“ haben. Verwenden Sie das Dictionary um die Molmassen für die einzelnen Atome zu erhalten. 
Probieren Sie Ihren Code so zu gestalten, dass er Atome mit mehreren Buchstaben wie "Fe" ebenfalls erkennt und auch belibig lange Ziffern wie 123 richtig berechnet.
'''

element_data = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.941,
    "Be": 9.012,
    "B": 10.81,
    "C": 12.01,
    "N": 14.01,
    "O": 16.00,
    "F": 19.00,
    "Ne": 20.18,
    "Na": 22.99,
    "Mg": 24.31,
    "Al": 26.98,
    "Si": 28.09,
    "P": 30.97,
    "S": 32.07,
    "Cl": 35.45,
    "K": 39.10,
    "Ar": 39.95,
    "Ca": 40.08,
    "Sc": 44.96,
    "Ti": 47.87,
    "V": 50.94,
    "Cr": 52.00,
    "Mn": 54.94,
    "Fe": 55.85,
    "Ni": 58.69,
    "Co": 58.93,
    "Cu": 63.55,
    "Zn": 65.38,
    "Ga": 69.72,
    "Ge": 72.63,
    "As": 74.92,
    "Se": 78.97,
    "Br": 79.90,
    "Kr": 83.80,
    "Rb": 85.47,
    "Sr": 87.62,
    "Y": 88.91,
    "Zr": 91.22,
    "Nb": 92.91,
    "Mo": 95.94,
    "Tc": 98.00,
    "Ru": 101.1,
    "Rh": 102.9,
    "Pd": 106.4,
    "Ag": 107.9,
    "Cd": 112.4,
    "In": 114.8,
    "Sn": 118.7,
    "Sb": 121.8,
    "I": 126.9,
    "Te": 127.6,
    "Xe": 131.3,
    "Cs": 132.9,
    "Ba": 137.3,
    "La": 138.9,
    "Ce": 140.1,
    "Pr": 140.9,
    "Nd": 144.2,
    "Pm": 145.0,
    "Sm": 150.4,
    "Eu": 152.0,
    "Gd": 157.3,
    "Tb": 158.9,
    "Dy": 162.5,
    "Ho": 164.9,
    "Er": 167.3,
    "Tm": 168.9,
    "Yb": 173.0,
    "Lu": 175.0,
    "Hf": 178.5,
    "Ta": 180.9,
    "W": 183.8,
    "Re": 186.2,
    "Os": 190.2,
    "Ir": 192.2,
    "Pt": 195.1,
    "Au": 197.0,
    "Hg": 200.6,
    "Tl": 204.4,
    "Pb": 207.2,
    "Bi": 208.9,
    "Th": 232.0,
    "Pa": 231.0,
    "U": 238.0
}

def molarmass(formula):
    M = 0
    i = 0

    while i < len(formula):
        element = formula[i]
        i += 1

        if i < len(formula) and formula[i].islower() == True:
            element += formula[i]
            i += 1

        number = ""

        while i < len(formula) and formula[i].isdigit() == True:
            number += formula[i]
            i += 1

        number = int(number)

        M += element_data[element] * number

    return M

#Test der molarmass Funktion 

print(molarmass("C6H12O6"))
# print(molarmass("H2O1"))
# print(molarmass("Eu1F2"))
# print(molarmass("Na1C2O2H3"))
# print(molarmass("Fe1C10H10"))


'''
Das Sieb des Eratosthenes ist ein Algorithmus, der im antiken Griechenland entwickelt wurde, um alle Primzahlen unterhalb einer vorgegebenen Obergrenze zu ermitteln. 
Man beginnt mit der Zahl 2 und streicht alle Vielfachen von 2. Die erste Zahl, die nicht gestrichen wurde (3), ist dann eine Primzahl. 
Anschließend werden auch alle Vielfachen dieser neuen Zahl aus der Liste gestrichen, und so weiter.

Implementieren Sie das Sieb mit Hilfe von numpy arrays und berechnen Sie all Primzahlen unterhalb von 1000.
'''

numbs = np.arange(2, 1001)

def is_prime(array):
    primes = []
    primenumber_type = np.ones(len(array), dtype=bool)

    for i in range(len(array)):
        n = array[i]

        for j in range(2, n):
            if n % j == 0:
                primenumber_type[i] = False
                break

    for i in range(len(array)):
        if primenumber_type[i] == True:
           primes.append(array[i])

    primes_list = np.array(primes)

    return print(primes_list)

is_prime(numbs)

'''
Generieren Sie 3 arrays mit 100, 1000 und 10000 Werten mittels der Funktion np.random.normal mit den Parametern loc = 15 
und scale = 3. Erstellen Sie mit Hilfe von matplotlib einen für jeden array einen barplots darstellen. Jeder plot soll 
zusätzlich die Normalverteilung zeigen aus der die Werte gezogen wurden. Jeder Plot soll einen Titel mit der Anzahl an Datenpunkten 
haben und Achsen beschriftungen. Wählen Sie die Schriftgrößen so, dass die Beschriftungen auch von weiter entfernt lesbar sind. Erstellen Sie einen Plot 
in dem alle 3 Barplots sichtbar sind sowie die Normalverteilung.
'''
def normalverteilung(x, m, s):
    return np.exp(-0.5 * ((x - m) / s)**2) / (s * np.sqrt(2 * np.pi))

mu, sigma = 15, 3

array_100 = np.random.normal(mu, sigma, 100)
array_1000 = np.random.normal(mu, sigma, 1000)
array_10000 = np.random.normal(mu, sigma, 10000)

data_list = [array_100, array_1000, array_10000]
labels = [f'$N = 100$', f'$N = 1000$', f'$N = 10000$']
colors = ["lightskyblue", "lawngreen", "lightcoral"]

x_plot = np.linspace(5, 25, 500)
y_plot = normalverteilung(x_plot, mu, sigma)

plt.figure(figsize=(10, 7), dpi=300)
plt.hist(array_100, bins=25 , density=True, color=colors[0], alpha=0.5, label="Daten")
plt.plot(x_plot, y_plot, lw = 2, linestyle="--", color= "indigo" , label="Normalverteilung")
plt.ylabel("Wahrscheinlichkeitsdichte", fontsize=15)
plt.xlabel("Werte", fontsize=15)
plt.title("Histogram (N = 100)", fontsize=25)
plt.legend()

plt.tight_layout()
plt.savefig("histogramme_n100.svg", bbox_inches="tight")
plt.close()



plt.figure(figsize=(10, 7), dpi=300)
plt.hist(array_1000, bins=50, density=True, color=colors[1], alpha=0.5, label="Daten")
plt.plot(x_plot, y_plot, lw = 2, linestyle="--", color= "seagreen", label="Normalverteilung")
plt.ylabel("Wahrscheinlichkeitsdichte", fontsize=15)
plt.xlabel("Werte", fontsize=15)
plt.title("Histogram (N = 1000)", fontsize=25)
plt.legend()

plt.tight_layout()
plt.savefig("histogramme_n1000.svg", bbox_inches="tight")
plt.close()



plt.figure(figsize=(10, 7), dpi=300)
plt.hist(array_10000, bins=50, density=True, color=colors[2], alpha=0.5, label="Daten")
plt.plot(x_plot, y_plot, lw = 2, linestyle="--", color= "firebrick", label="Normalverteilung")
plt.ylabel("Warscheinlichkeitsdichte", fontsize=15)
plt.xlabel("Werte", fontsize=15)
plt.title("Histogram (N = 10000)", fontsize=25)
plt.legend()

plt.tight_layout()
plt.savefig("histogramme_n10000.svg", bbox_inches="tight")
plt.close()



plt.figure(figsize=(10, 7), dpi=300)
plt.hist(array_100, bins=30, density=True, color=colors[0], alpha=0.75, label="N=100")
plt.hist(array_1000, bins=30, density=True, color=colors[1], alpha=0.75, label="N=1000")
plt.hist(array_10000, bins=30, density=True, color=colors[2], alpha=0.75, label="N=10000")
plt.plot(x_plot, y_plot, lw = 2, linestyle="--", color= "black", label="Normalverteilung")
plt.ylabel("Warscheinlichkeitsdichte", fontsize=15)
plt.xlabel("Werte", fontsize=15)
plt.tick_params(axis="both", labelsize=15)
plt.title("Histogramme", fontsize=25)
plt.legend()

plt.tight_layout()
plt.savefig("histogramme_gesammt.svg", bbox_inches="tight")
plt.close()