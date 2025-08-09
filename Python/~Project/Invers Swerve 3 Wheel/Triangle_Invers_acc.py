import tkinter as tk
from math import sin, cos, sqrt, atan2, radians, degrees
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Jarak dari pusat ke roda
r = 1.0  # meter

# Koordinat roda (segitiga sama sisi)
wheel_pos = [
    (0, r),  # roda 1
    (-sqrt(3)/2 * r, -r/2),  # roda 2
    (sqrt(3)/2 * r, -r/2)    # roda 3
]

def calculate_and_draw():
    try:
        gyro = float(entry_gyro.get())
        Vx = float(entry_vx.get())
        Vy = float(entry_vy.get())
        omega = float(entry_omega.get())
    except ValueError:
        return

    # Rotasi translasi berdasarkan gyro (field-oriented)
    theta = radians(gyro)
    temp = Vx * cos(theta) + Vy * sin(theta)
    Vy = -Vx * sin(theta) + Vy * cos(theta)
    Vx = temp

    speeds = []
    angles = []

    for (Xi, Yi) in wheel_pos:
        Wxi = Vx + omega * Yi
        Wyi = Vy - omega * Xi
        speed = sqrt(Wxi**2 + Wyi**2)
        angle = degrees(atan2(Wxi, Wyi))
        speeds.append(speed)
        angles.append(angle)

    # Normalisasi kecepatan
    max_speed = max(speeds)
    if max_speed > 1:
        speeds = [s / max_speed for s in speeds]

    # Update teks output
    for i in range(3):
        labels[i].config(text=f"Roda {i+1}: {speeds[i]:.2f} m/s, {angles[i]:.1f}°")

    # Gambar robot + roda
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    # Gambar body robot
    robot_x = [p[0] for p in wheel_pos] + [wheel_pos[0][0]]
    robot_y = [p[1] for p in wheel_pos] + [wheel_pos[0][1]]
    ax.plot(robot_x, robot_y, 'k-')

    # Gambar roda
    for (x, y), speed, ang in zip(wheel_pos, speeds, angles):
        ax.plot(x, y, 'ro')
        dx = 0.3 * speed * sin(radians(ang))
        dy = 0.3 * speed * cos(radians(ang))
        ax.arrow(x, y, dx, dy, head_width=0.05, head_length=0.08, fc='b', ec='b')

    canvas.draw()

def increment(entry, delta):
    try:
        value = float(entry.get())
    except ValueError:
        value = 0
    entry.delete(0, tk.END)
    entry.insert(0, str(value + delta))
    calculate_and_draw()

# GUI utama
root = tk.Tk()
root.title("Simulasi 3 Roda Swerve Drive")

# Input + tombol increment
def add_param_row(label, entry_var, row, step):
    tk.Label(root, text=label).grid(row=row, column=0)
    entry = tk.Entry(root)
    entry.insert(0, entry_var)
    entry.grid(row=row, column=1)

    tk.Button(root, text="-", command=lambda: increment(entry, -step)).grid(row=row, column=2)
    tk.Button(root, text="+", command=lambda: increment(entry, step)).grid(row=row, column=3)
    return entry

entry_gyro = add_param_row("Gyro (°):", 0, 0, 5)
entry_vx   = add_param_row("Vx (m/s):", 0, 1, 0.1)
entry_vy   = add_param_row("Vy (m/s):", 0.5, 2, 0.1)
entry_omega= add_param_row("Omega (rad/s):", 0, 3, 0.1)

tk.Button(root, text="Hitung & Gambar", command=calculate_and_draw).grid(row=4, column=0, columnspan=4)

# Output teks
labels = []
for i in range(3):
    lbl = tk.Label(root, text=f"Roda {i+1}: -")
    lbl.grid(row=5+i, column=0, columnspan=4)
    labels.append(lbl)

# Plot matplotlib
fig, ax = plt.subplots(figsize=(4, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=4, rowspan=8)

root.mainloop()
