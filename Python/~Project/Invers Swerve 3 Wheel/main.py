import math

# ----------------------------
# Konfigurasi posisi roda (m)
# Segitiga sama sisi, sisi s meter
s = 0.6  # panjang sisi segitiga
R = s / math.sqrt(3)  # circumradius

# Koordinat (x, y) tiap roda relatif pusat robot
wheels = [
    (0.0, R),  # Roda 1 (depan)
    (R * math.cos(math.radians(210)), R * math.sin(math.radians(210))),  # Roda 2 (kiri-bawah)
    (R * math.cos(math.radians(330)), R * math.sin(math.radians(330)))   # Roda 3 (kanan-bawah)
]

# ----------------------------
# Input perintah gerak robot
Vx = 1.0   # m/s, maju (+x)
Vy = 0.5   # m/s, ke kiri (+y)
omega = 1.0  # rad/s, rotasi CCW positif
Vmax = 1.2   # batas kecepatan motor (m/s)

# ----------------------------
# Perhitungan untuk tiap roda
results = []
for (x, y) in wheels:
    Vx_i = Vx - omega * y
    Vy_i = Vy + omega * x
    speed = math.sqrt(Vx_i**2 + Vy_i**2)
    angle_deg = math.degrees(math.atan2(Vy_i, Vx_i))  # -180 .. +180
    angle_deg_360 = (angle_deg + 360) % 360           # 0 .. 360
    results.append({
        "Vx_i": Vx_i,
        "Vy_i": Vy_i,
        "speed": speed,
        "angle_deg": angle_deg,
        "angle_deg_360": angle_deg_360
    })

# ----------------------------
# Normalisasi kecepatan
max_speed = max(r["speed"] for r in results)
scale = Vmax / max_speed if max_speed > Vmax else 1.0
for r in results:
    r["speed_scaled"] = r["speed"] * scale

# ----------------------------
# Tampilkan hasil
for idx, r in enumerate(results, start=1):
    print(f"Roda {idx}:")
    print(f"  Vx_i = {r['Vx_i']:.3f} m/s, Vy_i = {r['Vy_i']:.3f} m/s")
    print(f"  Sudut = {r['angle_deg']:.2f}°  ({r['angle_deg_360']:.2f}° 0..360)")
    print(f"  Speed = {r['speed']:.3f} m/s  (scaled: {r['speed_scaled']:.3f} m/s)")
    print()
