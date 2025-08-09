import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Rectangle

class InteractiveRobotSimulator:
    def __init__(self):
        # Setup lapangan
        self.field_width = 8
        self.field_length = 15
        
        # Inisialisasi variabel
        self.robot_x = 4.0  # Posisi default di tengah
        self.robot_y = 7.5
        self.theta = 0
        self.laser_front = 0
        self.laser_back = 0
        self.laser_left = 0
        self.laser_right = 0
        
        # Setup plot
        self.fig, self.ax = plt.subplots(figsize=(12, 9))
        self.fig.canvas.manager.set_window_title('Simulator Robot Interaktif')
        self.ax.set_xlim(-1, self.field_width + 1)
        self.ax.set_ylim(-1, self.field_length + 1)
        self.ax.set_aspect('equal')
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.set_title('Klik posisi robot di lapangan')
        self.ax.set_xlabel('Lebar Lapangan (X) - meter')
        self.ax.set_ylabel('Panjang Lapangan (Y) - meter')
        
        # Gambar lapangan
        self.field = Rectangle((0, 0), self.field_width, self.field_length, 
                              linewidth=2, edgecolor='black', facecolor='#e6f7e6')
        self.ax.add_patch(self.field)
        
        # Informasi teks
        self.angle_text = self.ax.text(0.5, -0.5, "Sudut: 0°", fontsize=12, 
                                      bbox=dict(facecolor='white', alpha=0.8))
        
        # Koneksi event
        self.cid_click = self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        
        # Robot marker
        self.robot_marker, = self.ax.plot([], [], 'ro', markersize=12, zorder=10)
        self.robot_arrow = None
        
        # Laser lines
        self.laser_lines = []
        laser_colors = ['red', 'blue', 'green', 'purple']
        for color in laser_colors:
            line, = self.ax.plot([], [], '--', linewidth=2, color=color, alpha=0.8)
            self.laser_lines.append(line)
            
        self.laser_texts = []
        for i in range(4):
            text = self.ax.text(0, 0, "", fontsize=10, ha='center', va='center', 
                               backgroundcolor='white', zorder=10)
            self.laser_texts.append(text)
        
        self.result_text = self.ax.text(self.field_width/2, -0.8, "", 
                                       fontsize=12, ha='center', va='center',
                                       bbox=dict(facecolor='yellow', alpha=0.7))
        
        # Instruksi
        self.instruction = self.ax.text(self.field_width/2, 16.2, 
                                       "Klik di lapangan untuk menentukan posisi robot, lalu masukkan sudut di terminal",
                                       fontsize=12, ha='center', va='center')
        
        # Status
        self.status_text = self.ax.text(self.field_width/2, -1.5, 
                                      "Status: Menunggu input posisi...",
                                      fontsize=11, ha='center', va='center',
                                      bbox=dict(facecolor='lightgray', alpha=0.8))
        
        # Update plot awal
        self.update_plot()
    
    def on_click(self, event):
        # Pastikan klik di dalam lapangan
        if event.inaxes != self.ax or event.xdata < 0 or event.xdata > self.field_width or \
           event.ydata < 0 or event.ydata > self.field_length:
            return
        
        # Update posisi robot
        self.robot_x = event.xdata
        self.robot_y = event.ydata
        
        # Update plot sementara
        self.update_plot()
        
        # Minta input sudut di terminal
        self.get_angle_from_terminal()
    
    def get_angle_from_terminal(self):
        # Update status
        self.status_text.set_text("Status: Masukkan sudut di terminal...")
        self.fig.canvas.draw_idle()
        
        # Dapatkan input sudut
        try:
            self.theta = float(input("\nMasukkan sudut gyroscope (derajat): "))
            self.calculate_lasers()
            self.update_plot()
            self.status_text.set_text("Status: Siap. Klik untuk memindahkan robot")
        except ValueError:
            self.status_text.set_text("Status: Input tidak valid! Masukkan angka.")
        
        # Fokus kembali ke plot
        plt.show(block=False)
        self.fig.canvas.draw()
    
    def calculate_lasers(self):
        """Menghitung jarak ke dinding untuk keempat laser"""
        if self.robot_x is None or self.robot_y is None:
            return
        
        theta_rad = math.radians(self.theta)
        
        # Hitung jarak ke dinding dengan mempertimbangkan orientasi
        # Laser depan
        if math.cos(theta_rad) >= 0:
            self.laser_front = (self.field_length - self.robot_y) / max(0.001, math.cos(theta_rad))
        else:
            self.laser_front = self.robot_y / max(0.001, -math.cos(theta_rad))
        
        # Laser belakang
        if math.cos(theta_rad) >= 0:
            self.laser_back = self.robot_y / max(0.001, math.cos(theta_rad))
        else:
            self.laser_back = (self.field_length - self.robot_y) / max(0.001, -math.cos(theta_rad))
        
        # Laser kiri
        self.laser_left = self.robot_x / max(0.001, abs(math.sin(theta_rad)))
        
        # Laser kanan
        self.laser_right = (self.field_width - self.robot_x) / max(0.001, abs(math.sin(theta_rad)))
    
    def update_plot(self):
        """Update visualisasi plot"""
        # Update posisi robot
        self.robot_marker.set_data([self.robot_x], [self.robot_y])
        
        # Update panah arah robot
        if self.robot_arrow:
            self.robot_arrow.remove()
            
        theta_rad = math.radians(self.theta)
        arrow_length = 1.0
        dx = arrow_length * math.sin(theta_rad)
        dy = arrow_length * math.cos(theta_rad)
        
        self.robot_arrow = self.ax.arrow(
            self.robot_x, self.robot_y, dx, dy,
            head_width=0.4, head_length=0.5, fc='darkred', ec='darkred', zorder=9
        )
        
        # Update laser jika sudut sudah diinput
        if self.theta != 0 or self.laser_front > 0:
            # Hitung titik ujung laser
            front_end = (self.robot_x + self.laser_front * math.sin(theta_rad), 
                         self.robot_y + self.laser_front * math.cos(theta_rad))
            back_end = (self.robot_x - self.laser_back * math.sin(theta_rad), 
                        self.robot_y - self.laser_back * math.cos(theta_rad))
            left_end = (self.robot_x - self.laser_left * math.cos(theta_rad), 
                        self.robot_y + self.laser_left * math.sin(theta_rad))
            right_end = (self.robot_x + self.laser_right * math.cos(theta_rad), 
                         self.robot_y - self.laser_right * math.sin(theta_rad))
            
            # Update garis laser
            lasers = [
                ([self.robot_x, front_end[0]], [self.robot_y, front_end[1]]),
                ([self.robot_x, back_end[0]], [self.robot_y, back_end[1]]),
                ([self.robot_x, left_end[0]], [self.robot_y, left_end[1]]),
                ([self.robot_x, right_end[0]], [self.robot_y, right_end[1]])
            ]
            
            for i, (x_data, y_data) in enumerate(lasers):
                self.laser_lines[i].set_data(x_data, y_data)
            
            # Update teks laser
            laser_labels = [
                f"Depan: {self.laser_front:.2f}m",
                f"Belakang: {self.laser_back:.2f}m",
                f"Kiri: {self.laser_left:.2f}m",
                f"Kanan: {self.laser_right:.2f}m"
            ]
            
            positions = [
                ((self.robot_x + front_end[0])/2, (self.robot_y + front_end[1])/2),
                ((self.robot_x + back_end[0])/2, (self.robot_y + back_end[1])/2),
                ((self.robot_x + left_end[0])/2, (self.robot_y + left_end[1])/2),
                ((self.robot_x + right_end[0])/2, (self.robot_y + right_end[1])/2)
            ]
            
            for i, label in enumerate(laser_labels):
                self.laser_texts[i].set_text(label)
                self.laser_texts[i].set_position(positions[i])
            
            # Update teks sudut dan hasil
            self.angle_text.set_text(f"Sudut: {self.theta}°")
            self.result_text.set_text(f"Posisi: X={self.robot_x:.2f}m, Y={self.robot_y:.2f}m")
        
        # Refresh plot
        self.fig.canvas.draw_idle()

# Jalankan simulator
print("="*70)
print("SIMULATOR ROBOT INTERAKTIF")
print("Instruksi:")
print("1. Klik di mana saja pada lapangan hijau untuk menentukan posisi robot")
print("2. Masukkan sudut gyroscope di terminal saat diminta")
print("3. Program akan menghitung dan menampilkan jarak laser secara otomatis")
print("4. Ulangi proses dengan mengklik posisi baru kapan saja")
print("="*70)

simulator = InteractiveRobotSimulator()
plt.tight_layout()
plt.show()