import plistlib

def update_uefi_drivers_section_inplace(plist_path):
    # Load the original plist file
    with open(plist_path, 'rb') as plist_file:
        plist_data = plistlib.load(plist_file)

    # Access the UEFI section and specifically the 'Drivers' sub-section
    uefi_drivers = plist_data.get('UEFI', {}).get('Drivers', [])

    # Ensure all entries in the 'Drivers' section are enabled
    for entry in uefi_drivers:
        entry['Enabled'] = True

    # Save the modified plist data back to the original file
    with open(plist_path, 'wb') as plist_file:
        plistlib.dump(plist_data, plist_file)

    return "UEFI Drivers section updated successfully in the original file!"

# Specify the path to your original plist file
plist_path = 'extra/X64/EFI/OC/Config.plist'

# Call the function with the path to your Config.plist
def main():
    result = update_uefi_drivers_section_inplace(plist_path)
    print(result)
main()