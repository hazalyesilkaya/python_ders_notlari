import numpy as np
import matplotlib.pyplot as plt

# Verilen değerler
Voc = 20.51  # Açık devre gerilimi (V)
Vm = 16.58   # Maksimum güç gerilimi (V)
Im = 3.01    # Maksimum güç akımı (A)
Isc = 3.34   # Kısa devre akımı (A)

# Standart test koşulları (STC)
standard_irradiance = 1000  # W/m²
module_area = 3  # m²

# Maksimum güç hesaplaması
Pmax = Vm * Im

# Güç dönüşüm verimliliği (PCE) hesaplaması
efficiency = (Pmax / (standard_irradiance * module_area)) * 100

# Çeşitli güç yoğunlukları için göreceli verimlilik grafiği
irradiance_values = np.linspace(100, 1000, 100)
efficiency_values = (Vm * Im) / (irradiance_values * module_area) * 100

# Verimlilik grafiğini çiz
plt.plot(irradiance_values, efficiency_values, label='PV Module Efficiency')
plt.scatter([standard_irradiance], [efficiency], color='red')  # Standart test koşullarını işaretle
plt.text(standard_irradiance + 20, efficiency - 1, f'STC\nEfficiency = {efficiency:.2f}%', color='red')

# Eksen etiketleri
plt.xlabel('Irradiance (W/m²)')
plt.ylabel('Efficiency (%)')

# Başlık
plt.title('PV Module Relative Efficiency')

# İlgili çizgileri ve etiketleri göster
plt.legend()

# Grafiği göster
plt.show()
