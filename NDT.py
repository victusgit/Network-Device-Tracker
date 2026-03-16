# Network Device Tracker

# Device class definition
class Device:

    def __init__(self, name, ip_address, device_type):
        self.name = name
        self.ip_address = ip_address
        self.device_type = device_type

    def display_device(self):
        print(self.name, "-", self.ip_address, "-", self.device_type)

# List to store devices
devices = []

print("Network Device Tracker")

while True:

    print("\nMenu:")
    print("1. Add Device")
    print("2. View Devices")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter device name: ")
        ip = input("Enter IP address: ")
        device_type = input("Enter device type (computer, router, server, etc.): ")

        # Create device object
        new_device = Device(name, ip, device_type)

        # Add device to list
        devices.append(new_device)

        print("Device added successfully!")

    elif choice == "2":

        if len(devices) == 0:
            print("No devices have been added yet.")
        else:
            print("\nTracked Devices:")
            for device in devices:
                device.display_device()

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please try again.")
