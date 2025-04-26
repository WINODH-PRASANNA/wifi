
# WiFi and Battery Alert System 🔋📶

This is a **Python backend application** that monitors your device's **battery level**, **WiFi connection**, and **internet speed**. It sends real-time **notifications** every 1 minute if any issue is detected.

## Features ✨
- Alerts when **battery level** drops below 30%.
- Alerts if **internet connection** is lost or WiFi is disconnected.
- Alerts if **download speed** falls below 2 Mbps while connected to WiFi.
- Runs automatically **every 1 minute**.
- Lightweight and runs in the background.

## Requirements ⚙️
- Python 3.x
- Install required packages:
  ```bash
  pip install psutil plyer speedtest-cli
  ```

## How to Run 🚀
1. Clone the repository or download the script.
2. Navigate to the project folder in your terminal.
3. Run the script:
   ```bash
   python wifi_battery_alert.py
   ```

## Project Type 📚
- **Backend application**
- No frontend interface (runs silently in the background).

## Libraries Used 📦
- [`psutil`](https://pypi.org/project/psutil/) – for battery status and network information.
- [`plyer`](https://pypi.org/project/plyer/) – for sending notifications.
- [`speedtest-cli`](https://pypi.org/project/speedtest-cli/) – for checking internet speed.

## License 📝
This project is open-source and free to use.
