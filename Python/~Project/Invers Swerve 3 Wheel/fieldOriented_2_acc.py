import tkinter as tk
import math

def calculate():
    try:
        # Ambil nilai input
        gyro = math.radians(float(entry_gyro.get()))
        FWD = float(entry_fwd.get())
        STR = float(entry_str.get())
        RCW = float(entry_rcw.get())
        L = float(entry_l.get())
        W = float(entry_w.get())

        # Field-oriented transform
        temp = FWD * math.cos(gyro) + STR * math.sin(gyro)
        STR = -FWD * math.sin(gyro) + STR * math.cos(gyro)
        FWD = temp

        # Hitung radius R
        R = math.sqrt(L**2 + W**2)

        # Hitung A, B, C, D
        A = STR - RCW * (L / R)
        B = STR + RCW * (L / R)
        C = FWD - RCW * (W / R)
        D = FWD + RCW * (W / R)

        # Hitung wheel speeds
        ws1 = math.sqrt(B**2 + C**2)
        ws2 = math.sqrt(B**2 + D**2)
        ws3 = math.sqrt(A**2 + D**2)
        ws4 = math.sqrt(A**2 + C**2)

        # Hitung wheel angles
        wa1 = math.degrees(math.atan2(B, C))
        wa2 = math.degrees(math.atan2(B, D))
        wa3 = math.degrees(math.atan2(A, D))
        wa4 = math.degrees(math.atan2(A, C))

        # Normalisasi
        max_ws = max(ws1, ws2, ws3, ws4)
        if max_ws > 1:
            ws1 /= max_ws
            ws2 /= max_ws
            ws3 /= max_ws
            ws4 /= max_ws

        # Update teks
        lbl_ws1.config(text=f"WS1: {ws1:.2f}"); lbl_wa1.config(text=f"WA1: {wa1:.1f}°")
        lbl_ws2.config(text=f"WS2: {ws2:.2f}"); lbl_wa2.config(text=f"WA2: {wa2:.1f}°")
        lbl_ws3.config(text=f"WS3: {ws3:.2f}"); lbl_wa3.config(text=f"WA3: {wa3:.1f}°")
        lbl_ws4.config(text=f"WS4: {ws4:.2f}"); lbl_wa4.config(text=f"WA4: {wa4:.1f}°")

        # Gambar ulang visualisasi
        draw_visual(ws1, wa1, ws2, wa2, ws3, wa3, ws4, wa4)

    except ValueError:
        pass


def draw_arrow(x, y, angle_deg, length, color="red"):
    angle_rad = math.radians(angle_deg)
    end_x = x + length * math.sin(angle_rad) * 50
    end_y = y - length * math.cos(angle_rad) * 50
    canvas.create_line(x, y, end_x, end_y, arrow=tk.LAST, fill=color, width=2)


def draw_visual(ws1, wa1, ws2, wa2, ws3, wa3, ws4, wa4):
    canvas.delete("all")

    # Titik posisi roda
    offset = 80
    wheel_positions = [
        (150 - offset, 150 - offset),  # WS1 (kiri depan)
        (150 + offset, 150 - offset),  # WS2 (kanan depan)
        (150 + offset, 150 + offset),  # WS3 (kanan belakang)
        (150 - offset, 150 + offset),  # WS4 (kiri belakang)
    ]

    # Gambar kotak robot
    canvas.create_rectangle(150 - offset, 150 - offset, 150 + offset, 150 + offset, outline="black")

    # Gambar panah tiap roda
    draw_arrow(*wheel_positions[0], wa1, ws1, "blue")
    draw_arrow(*wheel_positions[1], wa2, ws2, "green")
    draw_arrow(*wheel_positions[2], wa3, ws3, "purple")
    draw_arrow(*wheel_positions[3], wa4, ws4, "orange")


# Setup GUI
root = tk.Tk()
root.title("Swerve Drive Calculator + Visual")

# Input fields
tk.Label(root, text="Gyro (°):").grid(row=0, column=0)
entry_gyro = tk.Entry(root); entry_gyro.grid(row=0, column=1); entry_gyro.insert(0, "0")

tk.Label(root, text="FWD:").grid(row=1, column=0)
entry_fwd = tk.Entry(root); entry_fwd.grid(row=1, column=1); entry_fwd.insert(0, "0")

tk.Label(root, text="STR:").grid(row=2, column=0)
entry_str = tk.Entry(root); entry_str.grid(row=2, column=1); entry_str.insert(0, "0")

tk.Label(root, text="RCW:").grid(row=3, column=0)
entry_rcw = tk.Entry(root); entry_rcw.grid(row=3, column=1); entry_rcw.insert(0, "0")

tk.Label(root, text="Wheelbase (L):").grid(row=4, column=0)
entry_l = tk.Entry(root); entry_l.grid(row=4, column=1); entry_l.insert(0, "1")

tk.Label(root, text="Trackwidth (W):").grid(row=5, column=0)
entry_w = tk.Entry(root); entry_w.grid(row=5, column=1); entry_w.insert(0, "1")

btn_calc = tk.Button(root, text="Calculate", command=calculate)
btn_calc.grid(row=6, column=0, columnspan=2)

# Output
lbl_ws1 = tk.Label(root, text="WS1: -"); lbl_ws1.grid(row=7, column=0)
lbl_ws2 = tk.Label(root, text="WS2: -"); lbl_ws2.grid(row=7, column=1)
lbl_ws3 = tk.Label(root, text="WS3: -"); lbl_ws3.grid(row=8, column=0)
lbl_ws4 = tk.Label(root, text="WS4: -"); lbl_ws4.grid(row=8, column=1)

lbl_wa1 = tk.Label(root, text="WA1: -"); lbl_wa1.grid(row=9, column=0)
lbl_wa2 = tk.Label(root, text="WA2: -"); lbl_wa2.grid(row=9, column=1)
lbl_wa3 = tk.Label(root, text="WA3: -"); lbl_wa3.grid(row=10, column=0)
lbl_wa4 = tk.Label(root, text="WA4: -"); lbl_wa4.grid(row=10, column=1)

# Canvas visualisasi
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.grid(row=0, column=2, rowspan=12)

root.mainloop()
