import tkinter as tk
import math

# Konfigurasi segitiga
s = 200  # panjang sisi segitiga (px)
R = s / math.sqrt(3)  # circumradius (px)

# Posisi roda relatif pusat robot (px)
wheels = [
    (0, -R),  # Roda 1 (atas)
    (-s/2, R/2),  # Roda 2 (kiri bawah)
    (s/2, R/2)    # Roda 3 (kanan bawah)
]

# Kecepatan awal
Vx, Vy, omega = 0, 0, 0

def hitung_kinematics():
    results = []
    for (x, y) in wheels:
        # Skala 100 px = 1 m
        Vx_i = Vx - omega * (y / 100)
        Vy_i = Vy + omega * (x / 100)
        speed = math.sqrt(Vx_i**2 + Vy_i**2)
        angle = math.atan2(Vy_i, Vx_i)
        results.append((x, y, speed, angle))
    return results

def draw():
    canvas.delete("all")
    cx, cy = 300, 300  # pusat robot di tengah canvas

    # Gambar robot (segitiga)
    points = [(cx + x, cy + y) for (x, y) in wheels]
    canvas.create_polygon(points, outline="black", fill="", width=2)

    # Gambar roda & vektor kecepatan
    for i, (x, y, speed, angle) in enumerate(hitung_kinematics(), start=1):
        wx, wy = cx + x, cy + y
        # Roda
        canvas.create_oval(wx-10, wy-10, wx+10, wy+10, fill="red")
        # Panah kecepatan
        vx = wx + speed * 50 * math.cos(angle)  # skala visual
        vy = wy + speed * 50 * math.sin(angle)
        canvas.create_line(wx, wy, vx, vy, arrow=tk.LAST, width=2, fill="blue")
        # Teks kecepatan
        canvas.create_text(wx, wy - 20, text=f"{speed:.2f} m/s", fill="black", font=("Arial", 10, "bold"))

def update_vars(*args):
    global Vx, Vy, omega
    try:
        Vx = float(entry_vx.get())
        Vy = float(entry_vy.get())
        omega = float(entry_omega.get())
    except ValueError:
        return
    draw()

# GUI
root = tk.Tk()
root.title("Simulasi Swerve 3 Roda (Segitiga)")

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.grid(row=0, column=0, columnspan=3)

tk.Label(root, text="Vx (m/s):").grid(row=1, column=0)
entry_vx = tk.Entry(root)
entry_vx.grid(row=1, column=1)
entry_vx.insert(0, "1")

tk.Label(root, text="Vy (m/s):").grid(row=2, column=0)
entry_vy = tk.Entry(root)
entry_vy.grid(row=2, column=1)
entry_vy.insert(0, "0.5")

tk.Label(root, text="ω (rad/s):").grid(row=3, column=0)
entry_omega = tk.Entry(root)
entry_omega.grid(row=3, column=1)
entry_omega.insert(0, "0.5")

btn_update = tk.Button(root, text="Update", command=update_vars)
btn_update.grid(row=4, column=1)

update_vars()
root.mainloop()
