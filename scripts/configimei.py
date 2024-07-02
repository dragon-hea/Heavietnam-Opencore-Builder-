import plistlib

# Define the new device property
new_device_key = "PciRoot(0x0)/Pci(0x16,0x0)"
laptopimeisandy = {
    'device-id': bytes.fromhex('3A1C0000')
}
laptopimeiivy = {
    'device-id': bytes.fromhex('3A1E0000')
}
desktopimeisandy = {
    'device-id': bytes.fromhex('3A1C0000')
}
desktopimeiivy = {
    'device-id': bytes.fromhex('3A1E0000')
}

# Path to the plist file
plist_file_path = 'extra/X64/EFI/OC/Config.plist'

# Function to load the existing plist data
def load_existing_plist(filepath):
    with open(filepath, 'rb') as file:
        plist_data = plistlib.load(file)
    return plist_data

# Function to save updates to the plist file
def save_updated_plist(data, filepath):
    with open(filepath, 'wb') as file:
        plistlib.dump(data, file)

# Function to add or update device properties in the plist
def add_custom_device_property(plist_data, device_path, properties):
    if 'DeviceProperties' in plist_data and 'Add' in plist_data['DeviceProperties']:
        plist_data['DeviceProperties']['Add'].setdefault(device_path, {}).update(properties)
        print(f"Device properties for {device_path} have been added or updated.")
    else:
        print("DeviceProperties or Add not found in plist. Please check the plist file.")

def main(imeiconfig):
    # Load the existing plist data
    plist_data = load_existing_plist(plist_file_path)

    # Adding the new device property to the existing plist data
    add_custom_device_property(plist_data, new_device_key, imeiconfig)

    # Save the updated plist data back to the file
    save_updated_plist(plist_data, plist_file_path)
