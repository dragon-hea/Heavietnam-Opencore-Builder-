import plistlib

def update_acpi_add_section_inplace(plist_path):
    # Load the original plist file
    with open(plist_path, 'rb') as plist_file:
        plist_data = plistlib.load(plist_file)

    # Access the ACPI section and specifically the 'Add' sub-section
    acpi_add = plist_data.get('ACPI', {}).get('Add', [])

    # Ensure all entries in the 'Add' section are enabled
    for entry in acpi_add:
        entry['Enabled'] = True

    # Save the modified plist data back to the original file
    with open(plist_path, 'wb') as plist_file:
        plistlib.dump(plist_data, plist_file)

    return "ACPI Add section updated successfully in the original file!"

# Specify the path to your original plist file
plist_path = 'extra/X64/EFI/OC/Config.plist'

# Call the function with the path to your Config.plist
def main():
    result = update_acpi_add_section_inplace(plist_path)
    print(result)
main()