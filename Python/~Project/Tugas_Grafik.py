import matplotlib.pyplot as plt

# Data percobaan
percobaan = list(range(1, 9))
arus_analog = [34.2, 34.1, 34.4, 34.3, 34.2, 34.2, 34.2, 34.2]  # dalam mA
arus_digital = [32.2] * 8  # dalam mA
arus_teoritis = [31.9] * 8  # dalam mA

# Membuat grafik
plt.figure(figsize=(10, 5))
plt.plot(percobaan, arus_analog, marker='o', label='Arus Analog (mA)', color='blue')
plt.plot(percobaan, arus_digital, marker='s', label='Arus Digital (mA)', color='green')
plt.plot(percobaan, arus_teoritis, marker='^', linestyle='--', label='Arus Perhitungan (mA)', color='red')

# Kustomisasi grafik
plt.title('Grafik Pengukuran Arus DC')
plt.xlabel('Percobaan ke-')
plt.ylabel('Arus (mA)')
plt.xticks(percobaan)
plt.ylim(31, 35)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Tampilkan grafik
plt.show()

