# 🕹️ custom_teleop (ROS 2 Package)

A simple ROS 2 package that provides **custom keyboard teleoperation** for controlling a robot's movement using the `/cmd_vel` topic. Designed for simulation environments or robots that accept velocity commands.

---

## 🚀 Features

- Control robot using keyboard input (W/A/S/D/Space/Q)
- Publishes `geometry_msgs/msg/Twist` messages to `/cmd_vel`
- Runs in the terminal with no GUI required
- Lightweight and ROS 2 Humble compatible

---

## 📦 Package Contents

- `teleop_node.py` – Python script that reads keypresses and publishes velocity commands
- `setup.py` and `package.xml` – ROS 2 Python package structure

---

## 🎮 Keyboard Controls

| Key     | Action         |
|---------|----------------|
| `W`     | Move forward   |
| `S`     | Move backward  |
| `A`     | Turn left      |
| `D`     | Turn right     |
| `Space` | Stop           |
| `Q`     | Quit program   |

---

## 🛠️ How to Build

```bash
cd ~/custom_ws
colcon build
source install/setup.bash
