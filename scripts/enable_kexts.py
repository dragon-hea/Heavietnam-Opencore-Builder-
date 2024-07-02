import plistlib

def enable_all_kexts(plist_path):
    with open(plist_path, 'rb') as plist_file:
        plist_data = plistlib.load(plist_file)

    kexts = plist_data.get('Kernel', {}).get('Add', [])
    
    for kext in kexts:
        kext['Enabled'] = True  # Enable all kexts by default

    with open(plist_path, 'wb') as plist_file:
        plistlib.dump(plist_data, plist_file)

    return "All kexts in Kernel -> Add have been enabled!"

def main():
    plist_path = 'extra/X64/EFI/OC/Config.plist'  # Đảm bảo cập nhật đúng đường dẫn tới Config.plist
    result = enable_all_kexts(plist_path)
    print(result)
