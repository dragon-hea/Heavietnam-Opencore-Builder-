import plistlib

def remove_warning_keys():
    global plist_path
    plist_path = 'extra/X64/EFI/OC/Config.plist'
    # Load the original PLIST file
    with open(plist_path, 'rb') as file:
        plist_data = plistlib.load(file)
    
    # Find and remove keys that start with "#WARNING"
    keys_to_remove = [key for key in plist_data if key.startswith("#WARNING")]
    for key in keys_to_remove:
        del plist_data[key]
    
    # Save the modified PLIST back to the same file
    with open(plist_path, 'wb') as file:
        plistlib.dump(plist_data, file)

# Example usage

remove_warning_keys()
print(f"PLIST file has been updated and saved to: {plist_path}")
