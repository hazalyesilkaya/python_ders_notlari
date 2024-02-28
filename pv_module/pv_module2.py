import numpy as np
import matplotlib.pyplot as plt


def de_soto_model(V, Voc, Isc, Vmp, Imp, Rs, Rsh, n, T):
    q = 1.602e-19  # Elementar yük (Coulomb)
    k = 1.381e-23  # Boltzmann sabiti (J/K)

    Iph = Isc
    I0 = (Isc - Imp) / (np.exp((Vmp + Imp * Rs) / (n * k * T)) - 1)

    I = Iph - I0 * (np.exp((V + Imp * Rs) / (n * k * T)) - 1) - (V + Imp * Rs) / Rsh
    return I


# Panel parametreleri
Voc = 20.51  # Açık devre gerilimi (Open circuit voltage)
Isc = 3.32  # Kısa devre akımı (Short circuit current)
Vmp = 16.58  # Maksimum güç noktası gerilimi (Voltage at maximum power point)
Imp = 3.01  # Maksimum güç noktası akımı (Current at maximum power point)
Rs = (Voc - Vmp) / Imp  # Seriyel direnç
Rsh = (Vmp / Imp) - Rs  # Paralel direnç
n = 1.2  # Termal voltaj ve ideallik faktörü
T = 298  # Panel sıcaklığı (Kelvin)

# Voltaj aralığını belirle
V_range = np.linspace(0, Voc, 100)

# De Soto modelini kullanarak akım değerlerini hesapla
I_values = de_soto_model(V_range, Voc, Isc, Vmp, Imp, Rs, Rsh, n, T)

# IV eğrisini çiz
plt.figure(figsize=(8, 6))
plt.plot(V_range, I_values, label='IV Curve')
plt.scatter([Voc, Vmp], [0, 0], color='red', marker='o', label='Critical Points')
plt.title('Solar Panel IV Curve (De Soto Model)')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.legend()
plt.grid(True)
plt.show()
