import numpy as np
import matplotlib.pyplot as plt
import pvlib

# Verilen bilgiler
Voc = 20.51  # Açık devre gerilimi (V)
Vm = 16.58   # Maksimum güç noktasındaki voltaj (V)
Im = 3.01    # Maksimum güç noktasındaki akım (A)
Isc = 3.34   # Kısa devre akımı (A)

# Güneş koşulları
effective_irradiance = 1000  # W/m^2
temperature_cell = 25  # °C

# Başlangıç değerleri
Rs_guess = 0.64
Rsh_guess = 89.42

# Panel parametreleri
IL, I0, Rs, Rsh, nNsVth = pvlib.pvsystem.calcparams_desoto(
    effective_irradiance=effective_irradiance,
    temp_cell=temperature_cell,
    alpha_sc=0.004539,
    a_ref=2.6373,
    I_L_ref=3.34,
    I_o_ref=8.196e-10,
    R_sh_ref=Rsh_guess,
    R_s=Rs_guess,
    EgRef=1.121,
    dEgdT=-0.0002677
)

# IV eğrisini hesapla
voltage = np.linspace(0, Voc, 100)
current = pvlib.pvsystem.singlediode(
    photocurrent=IL,
    saturation_current=I0,
    resistance_series=Rs,
    resistance_shunt=Rsh,
    nNsVth=nNsVth,
    ivcurve_pnts=len(voltage),
    method='lambertw'
)['i']

# MPP noktasını belirle
mpp_idx = np.argmax(current * voltage)
Vm_sim = voltage[mpp_idx]
Im_sim = current[mpp_idx]

# Voltaj-Akım (V-I) Grafiği
plt.figure(figsize=(10, 5))
plt.plot(voltage, current, label='IV Characteristic')
plt.scatter([Voc, Vm_sim], [0, Im_sim], color='red')  # Açık devre gerilimi ve simülasyon MPP noktasını belirt
plt.xlabel('Voltaj (V)')
plt.ylabel('Akım (A)')
plt.title('Voltaj-Akım (V-I) Grafiği')
plt.legend()
plt.grid(True)
plt.show()

print("Simülasyon MPP Noktası -", Vm_sim*Im_sim)
print("Gerçek MPP Noktası -", Vm*Im,)

