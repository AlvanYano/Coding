"""
Simulasi Swerve 3-Roda (Segitiga) - Field-Centric GUI
- Python 3.x
- Tkinter GUI
Features:
- Input sliders: Vx_field (m/s), Vy_field (m/s), omega (rad/s)
- Toggle Field-Centric (on/off)
- Gyro (yaw) slider and option to have gyro auto-update by integrating omega (simulate IMU)
- Visual robot on canvas: triangle, wheels, velocity arrows
- Display wheel speeds (m/s) and angles (deg)
- Normalization of wheel speeds to Vmax
- Pause / Reset buttons
Author: ChatGPT (example)
"""

import tkinter as tk
from tkinter import ttk
import math
import time

# ----- CONFIG -----
UPDATE_MS = 40               # GUI update interval in ms (~25 Hz)
PIXELS_PER_M = 150.0         # visual scale: pixels per meter
ROBOT_CENTER = (400, 300)    # canvas center in px
ROBOT_SIDE_M = 0.6           # side length of equilateral triangle (meters)
WHEEL_DRAW_R = 8             # radius of wheel marker in px
ARROW_SCALE = 60.0           # visual scale for speed -> px

# ----- geometry (segitiga sama sisi) -----
s = ROBOT_SIDE_M
R = s / math.sqrt(3)   # circumradius (meters)
# coordinates in robot frame (x forward, y left) : front at +y in earlier examples,
# but we'll use x forward, y left (consistent with earlier mathematics: Vx is forward)
# We'll place wheel1 at front (x = +R, y = 0), and other two at 120° and 240°.
# To match previous examples (front on +Y), swap axes accordingly; here we choose:
# wheel positions as (x, y) in meters relative to robot center:
wheels = [
    (0.0,  R),                          # wheel 1 (front)
    (R * math.cos(math.radians(210)), R * math.sin(math.radians(210))),  # wheel 2 (left-bottom)
    (R * math.cos(math.radians(330)), R * math.sin(math.radians(330)))   # wheel 3 (right-bottom)
]

# ----- helper functions -----
def field_to_robot(Vx_field, Vy_field, yaw_rad):
    """
    Transform velocities from field frame to robot frame using yaw (psi).
    Vx_field: forward on field
    Vy_field: left on field
    yaw_rad: robot heading relative to field, positive CCW
    Returns Vx_robot, Vy_robot (robot-centric, forward & left)
    """
    cos_p = math.cos(yaw_rad)
    sin_p = math.sin(yaw_rad)
    Vx_r = cos_p * Vx_field + sin_p * Vy_field
    Vy_r = -sin_p * Vx_field + cos_p * Vy_field
    return Vx_r, Vy_r

def swerve3_inverse(Vx, Vy, omega, Vmax):
    """
    Inverse kinematics for 3-wheel swerve.
    Vx, Vy: robot-frame velocities (m/s)
    omega: yaw rate (rad/s), CCW positive
    Returns list of (speed, angle_rad) for each wheel, angles in (-pi, pi]
    Speeds are normalized so max <= Vmax (if Vmax > 0)
    """
    results = []
    for (x, y) in wheels:
        Vx_i = Vx - omega * y
        Vy_i = Vy + omega * x
        speed = math.hypot(Vx_i, Vy_i)
        angle = math.atan2(Vy_i, Vx_i)
        results.append([speed, angle, Vx_i, Vy_i])
    # normalize speeds if necessary (preserve directions)
    if Vmax > 0:
        max_speed = max(r[0] for r in results)
        if max_speed > Vmax and max_speed > 1e-9:
            scale = Vmax / max_speed
            for r in results:
                r[0] *= scale
    return results

# ----- GUI application -----
class SwerveSimApp:
    def __init__(self, root):
        self.root = root
        root.title("Swerve 3-Roda Field-Centric Simulator")

        # Canvas for drawing field & robot
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.grid(row=0, column=0, rowspan=12, padx=8, pady=8)

        # Controls frame
        frm = ttk.Frame(root)
        frm.grid(row=0, column=1, sticky="nw")

        # Vx slider (field frame): forward (positive)
        ttk.Label(frm, text="Vx_field (m/s) forward").grid(row=0, column=0, sticky="w")
        self.vx_var = tk.DoubleVar(value=0.8)
        self.vx_s = ttk.Scale(frm, from_=-2.0, to=2.0, variable=self.vx_var, orient="horizontal")
        self.vx_s.grid(row=1, column=0, sticky="we", pady=2)

        # Vy slider (field frame): left (positive)
        ttk.Label(frm, text="Vy_field (m/s) left").grid(row=2, column=0, sticky="w")
        self.vy_var = tk.DoubleVar(value=0.2)
        self.vy_s = ttk.Scale(frm, from_=-2.0, to=2.0, variable=self.vy_var, orient="horizontal")
        self.vy_s.grid(row=3, column=0, sticky="we", pady=2)

        # Omega slider (rad/s), positive CCW
        ttk.Label(frm, text="omega (rad/s) CCW").grid(row=4, column=0, sticky="w")
        self.omega_var = tk.DoubleVar(value=0.4)
        self.omega_s = ttk.Scale(frm, from_=-3.0, to=3.0, variable=self.omega_var, orient="horizontal")
        self.omega_s.grid(row=5, column=0, sticky="we", pady=2)

        # Vmax slider (m/s)
        ttk.Label(frm, text="Vmax (m/s) - normalization").grid(row=6, column=0, sticky="w")
        self.vmax_var = tk.DoubleVar(value=1.2)
        self.vmax_s = ttk.Scale(frm, from_=0.1, to=3.0, variable=self.vmax_var, orient="horizontal")
        self.vmax_s.grid(row=7, column=0, sticky="we", pady=2)

        # Field-centric toggle
        self.fieldcentric_var = tk.BooleanVar(value=True)
        self.fc_check = ttk.Checkbutton(frm, text="Field-Centric ON", variable=self.fieldcentric_var)
        self.fc_check.grid(row=8, column=0, sticky="w", pady=6)

        # Gyro controls
        ttk.Label(frm, text="Gyro yaw (deg)").grid(row=9, column=0, sticky="w")
        self.yaw_var = tk.DoubleVar(value=0.0)
        self.yaw_s = ttk.Scale(frm, from_=-180.0, to=180.0, variable=self.yaw_var, orient="horizontal")
        self.yaw_s.grid(row=10, column=0, sticky="we", pady=2)

        self.gyro_follow_var = tk.BooleanVar(value=True)
        self.gyro_follow_cb = ttk.Checkbutton(frm, text="Gyro auto-update by ω", variable=self.gyro_follow_var)
        self.gyro_follow_cb.grid(row=11, column=0, sticky="w", pady=4)

        # Buttons
        btn_frame = ttk.Frame(frm)
        btn_frame.grid(row=12, column=0, pady=8)
        self.btn_pause = ttk.Button(btn_frame, text="Pause", command=self.toggle_pause)
        self.btn_pause.grid(row=0, column=0, padx=4)
        self.btn_reset = ttk.Button(btn_frame, text="Reset Pose", command=self.reset_pose)
        self.btn_reset.grid(row=0, column=1, padx=4)

        # Info text
        self.info_label = ttk.Label(frm, text="Wheel outputs will show on canvas.", wraplength=220)
        self.info_label.grid(row=13, column=0, pady=6)

        # Simulation state
        self.paused = False
        self.last_time = time.time()
        # robot pose on field (x forward, y left), meters
        self.pose_x = 0.0
        self.pose_y = 0.0
        self.pose_yaw = 0.0  # rad, should match gyro ideally

        # Start loop
        self.root.after(UPDATE_MS, self.update)

    def toggle_pause(self):
        self.paused = not self.paused
        self.btn_pause.config(text="Resume" if self.paused else "Pause")
        self.last_time = time.time()

    def reset_pose(self):
        self.pose_x = 0.0
        self.pose_y = 0.0
        self.pose_yaw = 0.0
        self.yaw_var.set(0.0)

    def update(self):
        # time delta
        now = time.time()
        dt = now - self.last_time if not self.paused else 0.0
        self.last_time = now

        # read inputs
        Vx_field = float(self.vx_var.get())
        Vy_field = float(self.vy_var.get())
        omega_cmd = float(self.omega_var.get())
        Vmax = float(self.vmax_var.get())
        yaw_deg = float(self.yaw_var.get())
        # Convert yaw slider deg -> rad for transform (but we also simulate gyro integration)
        yaw_rad = math.radians(yaw_deg)

        # If gyro follows omega, integrate pose_yaw from omega (simulate IMU read)
        if self.gyro_follow_var.get() and not self.paused:
            # integrate yaw by omega in robot frame: omega is yaw rate (CCW positive)
            self.pose_yaw += omega_cmd * dt
            # wrap
            self.pose_yaw = (self.pose_yaw + math.pi) % (2*math.pi) - math.pi
            yaw_rad = self.pose_yaw
            # also integrate robot position in field frame by transforming commanded field velocities
            # Note: commanded Vx_field, Vy_field are in field frame; robot actual velocity in field frame
            # we will integrate actual robot-frame velocities transformed to field frame for movement
            # First compute Vx_robot, Vy_robot used by kinematics (field->robot transform)
            if self.fieldcentric_var.get():
                Vx_robot, Vy_robot = field_to_robot(Vx_field, Vy_field, yaw_rad)
            else:
                Vx_robot, Vy_robot = Vx_field, Vy_field

            # Convert robot velocities back to field frame for integrating pose (V_field = R(yaw)*V_robot)
            cos_p = math.cos(yaw_rad)
            sin_p = math.sin(yaw_rad)
            Vx_field_actual = cos_p * Vx_robot - sin_p * Vy_robot
            Vy_field_actual = sin_p * Vx_robot + cos_p * Vy_robot

            # integrate pose (forward is +x, left is +y)
            self.pose_x += Vx_field_actual * dt
            self.pose_y += Vy_field_actual * dt
        else:
            # use yaw from slider
            yaw_rad = math.radians(self.yaw_var.get())
            self.pose_yaw = yaw_rad
            # optionally integrate position if not paused and not using gyro-follow
            if not self.paused:
                if self.fieldcentric_var.get():
                    Vx_robot, Vy_robot = field_to_robot(Vx_field, Vy_field, yaw_rad)
                else:
                    Vx_robot, Vy_robot = Vx_field, Vy_field
                cos_p = math.cos(yaw_rad)
                sin_p = math.sin(yaw_rad)
                Vx_field_actual = cos_p * Vx_robot - sin_p * Vy_robot
                Vy_field_actual = sin_p * Vx_robot + cos_p * Vy_robot
                self.pose_x += Vx_field_actual * dt
                self.pose_y += Vy_field_actual * dt

        # transform commanded field velocities to robot frame if field-centric ON
        if self.fieldcentric_var.get():
            Vx_robot, Vy_robot = field_to_robot(Vx_field, Vy_field, yaw_rad)
        else:
            Vx_robot, Vy_robot = Vx_field, Vy_field

        # compute wheel outputs (speeds, angles)
        wheel_cmds = swerve3_inverse(Vx_robot, Vy_robot, omega_cmd, Vmax)

        # draw scene
        self.draw_scene(wheel_cmds, yaw_rad)

        # schedule next update
        self.root.after(UPDATE_MS, self.update)

    def draw_scene(self, wheel_cmds, yaw_rad):
        self.canvas.delete("all")
        cx, cy = ROBOT_CENTER
        # Draw axes / grid for field reference
        # axis lines
        self.canvas.create_line(0, cy, 800, cy, fill="#ddd")
        self.canvas.create_line(cx, 0, cx, 600, fill="#ddd")
        # draw robot pose center (field to canvas mapping)
        # map robot pose (meters) to canvas
        robot_cx = cx + self.pose_x * PIXELS_PER_M
        robot_cy = cy - self.pose_y * PIXELS_PER_M   # field left is +y, canvas down is +y so subtract
        # draw a small cross for center
        self.canvas.create_oval(robot_cx-4, robot_cy-4, robot_cx+4, robot_cy+4, fill="black")

        # draw robot triangle in robot frame, rotated by pose yaw and translated to canvas
        # compute wheel canvas coordinates and draw
        pts = []
        for (x,y) in wheels:
            # rotate wheel position by yaw_rad to get in field coords
            xr =  x * math.cos(yaw_rad) - y * math.sin(yaw_rad)
            yr =  x * math.sin(yaw_rad) + y * math.cos(yaw_rad)
            px = robot_cx + xr * PIXELS_PER_M
            py = robot_cy - yr * PIXELS_PER_M
            pts.append((px, py))
        # draw triangle outline
        flat = [coord for p in pts for coord in p]
        self.canvas.create_polygon(flat, outline="black", fill="", width=2)

        # draw heading arrow at robot center
        head_len = 30
        hx = robot_cx + head_len * math.cos(yaw_rad)
        hy = robot_cy - head_len * math.sin(yaw_rad)
        self.canvas.create_line(robot_cx, robot_cy, hx, hy, arrow=tk.LAST, width=3, fill="green")
        # heading text
        deg = math.degrees(yaw_rad)
        self.canvas.create_text(robot_cx + 40, robot_cy - 10, text=f"yaw {deg:.1f}°", fill="green", font=("Arial",10,"bold"))

        # draw each wheel and its velocity vector + label
        for i, ((x,y), (speed, angle, Vx_i, Vy_i)) in enumerate(zip(wheels, wheel_cmds), start=1):
            # wheel pos in field coords
            xr =  x * math.cos(yaw_rad) - y * math.sin(yaw_rad)
            yr =  x * math.sin(yaw_rad) + y * math.cos(yaw_rad)
            wx = robot_cx + xr * PIXELS_PER_M
            wy = robot_cy - yr * PIXELS_PER_M
            # draw wheel marker
            self.canvas.create_oval(wx-WHEEL_DRAW_R, wy-WHEEL_DRAW_R, wx+WHEEL_DRAW_R, wy+WHEEL_DRAW_R, fill="#d9534f", outline="black")
            # velocity arrow (use the wheel's commanded speed & angle in robot frame; rotate to field)
            # angle is wheel direction in robot frame; convert to field angle by adding yaw
            field_angle = angle + yaw_rad
            ax = wx + (speed * ARROW_SCALE) * math.cos(field_angle)
            ay = wy - (speed * ARROW_SCALE) * math.sin(field_angle)
            self.canvas.create_line(wx, wy, ax, ay, arrow=tk.LAST, width=2, fill="blue")
            # label speed and angle near wheel
            ang_deg = math.degrees(angle)
            self.canvas.create_text(wx, wy - 16, text=f"W{i}: {speed:.2f} m/s", font=("Arial", 10, "bold"))
            self.canvas.create_text(wx, wy + 16, text=f"{ang_deg:+.0f}°", font=("Arial", 9))

        # draw pose text
        self.canvas.create_text(100, 20, text=f"Pose X: {self.pose_x:.2f} m   Y: {self.pose_y:.2f} m", anchor="w", font=("Arial",10))
        self.canvas.create_text(100, 40, text=f"Vx_field: {self.vx_var.get():.2f} m/s  Vy_field: {self.vy_var.get():.2f} m/s  ω: {self.omega_var.get():.2f} rad/s", anchor="w", font=("Arial",10))
        self.canvas.create_text(100, 60, text=f"Field-Centric: {'ON' if self.fieldcentric_var.get() else 'OFF'}    Vmax: {self.vmax_var.get():.2f} m/s", anchor="w", font=("Arial",10))


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = SwerveSimApp(root)
    root.mainloop()
