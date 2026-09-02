# psutil is third-party: pip install psutil
import os
import psutil

# CPU information
print("Logical CPUs:", psutil.cpu_count(logical=True))
print("Physical CPUs:", psutil.cpu_count(logical=False))
print("CPU usage:", psutil.cpu_percent(interval=1), "%")
print("Usage per CPU:", psutil.cpu_percent(interval=0.2, percpu=True))
cpu_frequency = psutil.cpu_freq()
if cpu_frequency:
    print("Current CPU frequency:", cpu_frequency.current, "MHz")

# Memory and swap information
memory = psutil.virtual_memory()
print("Total memory:", memory.total)
print("Available memory:", memory.available)
print("Memory usage:", memory.percent, "%")
swap = psutil.swap_memory()
print("Swap usage:", swap.percent, "%")

# Disk information
disk = psutil.disk_usage("/")
print("Disk total:", disk.total)
print("Disk free:", disk.free)
print("Disk usage:", disk.percent, "%")
print("Disk partitions:", len(psutil.disk_partitions()))

# Network counters
network = psutil.net_io_counters()
print("Bytes sent:", network.bytes_sent)
print("Bytes received:", network.bytes_recv)

# Current process information
process = psutil.Process(os.getpid())
print("Process ID:", process.pid)
print("Process name:", process.name())
print("Process status:", process.status())
print("Process memory:", process.memory_info().rss)
print("Process create time:", process.create_time())
