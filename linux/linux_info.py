import os
import platform
import socket
import datetime
import subprocess

def run_command(command):
    try:
        return subprocess.check_output(command, shell=True, text=True).strip()
    except Exception:
        return "N/A"

print("==================================================")
print("LINUX SYSTEM INFORMATION REPORT")
print("==================================================")
print("Hostname        :", socket.gethostname())
print("Date & Time     :", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("OS              :", platform.system(), platform.release())
print("Architecture    :", platform.machine())
print("Python Version  :", platform.python_version())
print("Current User    :", os.getenv("USER"))
print("==================================================")
print("CPU INFORMATION")
print("==================================================")
print(run_command("lscpu | grep 'Model name'"))
print(run_command("lscpu | grep '^CPU(s):'"))
print("==================================================")
print("MEMORY USAGE")
print("==================================================")
print(run_command("free -h"))
print("==================================================")
print("DISK USAGE")
print("==================================================")
print(run_command("df -h /"))
print("==================================================")
print("LOGGED-IN USERS")
print("==================================================")
print(run_command("who"))
print("==================================================")
print("TOP 5 PROCESSES BY CPU USAGE")
print("==================================================")
print(run_command("ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6"))
print("==================================================")