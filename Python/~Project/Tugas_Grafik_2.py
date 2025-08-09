import matplotlib.pyplot as plt

# Data daya terhitung (konstan) dan daya terukur (dari percobaan)
calculated_power = [26.1426, 26.9348,26.9348,26.9348,26.9348,26.9348,26.9348,26.9348]
measured_power = [26.35, 26.70, 26.80, 26.90, 27.00, 27.10, 27.35, 27.65]

# Nomor percobaan
trials = list(range(1, 9))

# Membuat grafik
plt.figure(figsize=(10, 5))
plt.plot(trials, calculated_power, label='Daya Terhitung (W)', marker='o', color='orange')
plt.plot(trials, measured_power, label='Daya Terukur (W)', marker='s', color='orangered')
plt.xlabel('Percobaan ke-')
plt.ylabel('Daya (Watt)')
plt.title('Perbandingan Daya Terhitung dan Daya Terukur')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
