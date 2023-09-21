file_size_gb = float(input("Enter: "))
internet_speed_bps = float(input("Enter internet speed in bits per second: "))

print("Choose operation number:")
print("1. In hours")
print("2. In minutes")
print("3. In seconds")
choice = int(input("Enter operation number (1/2/3): "))

if choice == 1:
    time_hours = (file_size_gb * 8 * 1024) / (internet_speed_bps * 3600)
    print(f"The file will be downloaded in {time_hours} hours")
elif choice == 2:
    time_minutes = (file_size_gb * 8 * 1024) / (internet_speed_bps * 60)
    print(f"The file will be downloaded in {time_minutes} minutes")
elif choice == 3:
    time_seconds = (file_size_gb * 8 * 1024) / internet_speed_bps
    print(f"The file will be downloaded in {time_seconds} seconds")
else:
    print("Unknown operation number")