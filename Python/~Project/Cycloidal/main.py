import numpy as np
import matplotlib.pyplot as plt

# === Parameter cycloidal drive ===
r1 = 27        # Radius ring gear (radius besar)
r2 = 2.76      # Radius pin tetap (fixed ring pin radius)
N = 17         # Jumlah pin tetap (gear teeth count)
E = 1          # Eksentrisitas
n_out = 6      # Jumlah lubang output
R_o = 15       # Jarak radial lubang output dari pusat disc
r_o = 2        # Radius lubang output
theta_vals = np.linspace(0, 2 * np.pi, 1000)  # Parameter θ

# === Hitung profil cakram sikloid ===
phi_vals = np.arctan2(
    np.sin((1 - N) * theta_vals),
    (r1 / (E * N)) - np.cos((1 - N) * theta_vals)
)

X_d = r1 * np.cos(theta_vals) - r2 * np.cos(theta_vals + phi_vals) - E * np.cos(N * theta_vals)
Y_d = r1 * np.sin(theta_vals) - r2 * np.sin(theta_vals + phi_vals) - E * np.sin(N * theta_vals)

# === Posisi pin tetap pada ring gear ===
ring_pin_x = [r1 * np.cos(2 * np.pi * k / N) for k in range(N)]
ring_pin_y = [r1 * np.sin(2 * np.pi * k / N) for k in range(N)]

# === Lubang output: posisi saat teta = 0 ===
theta_drive = 0  # posisi statis disc
X_c = -E * np.cos(theta_drive)
Y_c = -E * np.sin(theta_drive)

output_x = [X_c + R_o * np.cos(2 * np.pi * k / n_out + N * theta_drive) for k in range(n_out)]
output_y = [Y_c + R_o * np.sin(2 * np.pi * k / n_out + N * theta_drive) for k in range(n_out)]

# === Plot ===
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(X_d, Y_d, 'k-', label="Cycloidal Disc Profile")
ax.scatter(ring_pin_x, ring_pin_y, color='blue', label="Fixed Ring Pins")
ax.scatter(output_x, output_y, color='green', label="Output Holes")

# Lingkaran visual untuk pin tetap
for x, y in zip(ring_pin_x, ring_pin_y):
    circle = plt.Circle((x, y), r2, color='blue', fill=False, linestyle='--')
    ax.add_patch(circle)

# Lingkaran visual untuk lubang output
for x, y in zip(output_x, output_y):
    circle = plt.Circle((x, y), r_o, color='green', fill=False, linestyle='--')
    ax.add_patch(circle)

# Lubang bearing input
input_circle = plt.Circle((X_c, Y_c), r2 * N / np.pi, color='red', fill=False, linestyle='--', label='Input Bearing')
ax.add_patch(input_circle)

# Finalisasi tampilan
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title("Cycloidal Drive with Output Holes")
plt.show()
