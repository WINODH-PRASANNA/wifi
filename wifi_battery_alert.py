import psutil
import socket
import time
import speedtest
from plyer import notification

def is_connected_to_wifi():
    wifi_info = psutil.net_if_addrs()
    # Check for WiFi interface and whether it's connected
    for interface, addrs in wifi_info.items():
        if 'Wi-Fi' in interface:  # You might need to change 'Wi-Fi' depending on your system
            for addr in addrs:
                if addr.family == 2:  # IPv4 address
                    return True
    return False

def get_network_speed():
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000  # Convert bits to Megabits (Mbps)
        return round(download_speed, 2)
    except Exception:
        return 0

def check_and_notify():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        wifi_connected = is_connected_to_wifi()
        speed = get_network_speed()

        if wifi_connected:
            if percent < 30:
                notification.notify(
                    title="⚡ Low Battery + WiFi Connected",
                    message=f"Battery is {percent}%. Please charge your device!",
                    timeout=10
                )
            if speed < 2:  # Example: consider less than 2 Mbps as slow
                notification.notify(
                    title="🐢 Slow Internet Alert",
                    message=f"Download Speed is {speed} Mbps. Check your WiFi connection!",
                    timeout=10
                )
        else:
            notification.notify(
                title="❌ No WiFi Connection",
                message="WiFi is not connected. Please check your network!",
                timeout=10
            )

if __name__ == "__main__":
    while True:
        check_and_notify()
        time.sleep(60)  # Wait 1 minute
