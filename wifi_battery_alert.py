import speedtest
import psutil
import requests
import time
from plyer import notification

def check_network_speed():
    """Check download and upload speed in Mbps"""
    st = speedtest.Speedtest()
    st.download()  # Perform download test
    st.upload()    # Perform upload test
    results = st.results.dict()
    download_speed = results['download'] / 1_000_000  # Convert to Mbps
    upload_speed = results['upload'] / 1_000_000      # Convert to Mbps
    return download_speed, upload_speed

def check_battery_level():
    """Check current battery percentage"""
    battery = psutil.sensors_battery()
    if battery is None:
        raise Exception("Battery information not available")
    return battery.percent, battery.power_plugged

def send_alert(message):
    """Send alert via desktop notification"""
    notification.notify(
        title="System Alert",
        message=message,
        timeout=10
    )
    print(f"Alert sent: {message}")

def monitor_system():
    """Main monitoring function"""
    try:
        # Check network speed
        download_speed, upload_speed = check_network_speed()
        print(f"Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")
        
        # Check battery
        battery_percent, is_charging = check_battery_level()
        print(f"Battery: {battery_percent}%", "Charging" if is_charging else "Discharging")
        
        # Check conditions and send alerts
        if download_speed < 1:
            send_alert(f"Low network speed: {download_speed:.2f} Mbps (below 1 Mbps)")
        
        if battery_percent < 30 and not is_charging:
            send_alert(f"Low battery: {battery_percent}% (below 30%)")
            
    except Exception as e:
        print(f"Error occurred: {e}")

if _name_ == "_main_":
    # Run monitoring every 5 minutes (300 seconds)
    while True:
        monitor_system()
        time.sleep(300)  # Wait for 5 minutes before checking again
