
# Network Speed & Battery Monitor 🔌📶

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-3-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

A lightweight Python utility that continuously monitors your network connection speed and battery level, sending real-time desktop alerts when thresholds are breached.  
It runs automatically every 5 minutes in the background and helps you stay aware of poor network conditions or low battery levels!

---

## Table of Contents 📋
- [Features](#features-)
- [Installation](#installation-)
- [Usage](#usage-)
- [Requirements](#requirements-)
- [Troubleshooting](#troubleshooting-)
- [License](#license-)

---

## Features ✨

### 📶 Network Monitoring
- Real-time download and upload speed testing using `speedtest-cli`.
- Automatic monitoring every 5 minutes.
- Instant alert if download speed falls below **1 Mbps**.

### 🔋 Battery Monitoring
- Continuous tracking of battery percentage.
- Charging status detection (plugged/unplugged).
- Alert if battery drops below **30%** and not charging.

### 🔔 Desktop Notifications
- Cross-platform alert pop-ups using `plyer`.
- Clear and detailed alert messages.
- Alerts shown even when app runs silently in the background.

### 🛡️ Error Handling
- Gracefully handles errors like missing battery sensor.
- Prints helpful error messages for debugging.

### ⚡ Lightweight & Efficient
- Minimal system resource consumption.
- Ideal for long background operations.
- Simple console logs for monitoring progress.

---

## Installation ⚙️

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Steps
```bash
# Clone the repository
git clone https://github.com/yourusername/network-battery-monitor.git
cd network-battery-monitor

# Install dependencies
pip install -r requirements.txt
```

Or install dependencies manually:
```bash
pip install speedtest-cli psutil plyer
```

---

## Usage 🚀

Run the project:
```bash
python wifi_battery_alert.py
```

- The script will:
  - Check network speed and battery level.
  - Send alerts if thresholds are breached.
  - Repeat monitoring every 5 minutes automatically.

> Make sure notifications are allowed on your device/system.

---

## Requirements 📦
- [speedtest-cli](https://pypi.org/project/speedtest-cli/)
- [psutil](https://pypi.org/project/psutil/)
- [plyer](https://pypi.org/project/plyer/)

Install all with:
```bash
pip install speedtest-cli psutil plyer
```

---

## Troubleshooting 🛠
- **No notifications?**
  - Check if your system allows notification pop-ups for apps/scripts.
- **Battery information not available?**
  - Some desktop PCs may not have a battery sensor.
- **Slow speed test?**
  - Network fluctuations can cause varied results; consider adjusting threshold if needed.

---

## License 📜
This project is licensed under the **MIT License**.  
Feel free to modify and use it for personal or professional purposes!
