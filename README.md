# Network Speed & Battery Monitor 🔌📶

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-3-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

A lightweight Python utility that continuously monitors your network connection speed and battery level, sending desktop alerts when thresholds are breached.

## Table of Contents 📋
- [Features](#features-)
- [Installation](#installation-)
- [Usage](#usage-)
- [Configuration](#configuration-)
- [Requirements](#requirements-)
- [Troubleshooting](#troubleshooting-)
- [License](#license-)

## Features ✨
- *Network Monitoring*:
  - Real-time download/upload speed measurement
  - Automatic speed test every 5 minutes
  - Alert when speed < 1 Mbps
- *Battery Monitoring*:
  - Continuous battery percentage tracking
  - Charging status detection
  - Alert when battery < 30% and not charging
- *Notification System*:
  - Cross-platform desktop notifications
  - Clear alert messages with thresholds
- *Lightweight*:
  - Low system resource usage
  - Runs in background

## Installation ⚙

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

### Alternatively, install dependencies direction
```bash
# terminal
pip install speedtest-cli psutil plyer
```
## Usage 🚀
Run the project
```bash
python wifi_bettery_alert.py
```
