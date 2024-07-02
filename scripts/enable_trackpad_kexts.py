import plistlib

def enable_trackpad_kexts(plist_path, trackpad_type):
    with open(plist_path, 'rb') as plist_file:
        plist_data = plistlib.load(plist_file)

    kexts = plist_data.get('Kernel', {}).get('Add', [])

    for kext in kexts:
        bundle_path = kext.get('BundlePath', '')

        if trackpad_type == "i2c":
            if "VoodooI2C" in bundle_path:
                kext['Enabled'] = True
            elif any(plugin in bundle_path for plugin in ["VoodooPS2Mouse", "VoodooPS2Trackpad", "VoodooInput"]):
                if "VoodooPS2Keyboard" not in bundle_path:
                    kext['Enabled'] = False
                if "VoodooInput" in bundle_path and "VoodooI2C" in bundle_path:
                    kext['Enabled'] = True  # Keep VoodooInput for VoodooI2C enabled
            elif "VoodooPS2Keyboard" in bundle_path:
                kext['Enabled'] = True
        elif trackpad_type == "ps2":
            if "VoodooPS2" in bundle_path:
                kext['Enabled'] = True

    with open(plist_path, 'wb') as plist_file:
        plistlib.dump(plist_data, plist_file)

    return "Trackpad kexts updated successfully!"

def main(trackpad_type):
    plist_path = 'extra/X64/EFI/OC/Config.plist'  # Đảm bảo cập nhật đúng đường dẫn tới Config.plist
    result = enable_trackpad_kexts(plist_path, trackpad_type)
    print(result)

if __name__ == "__main__":
    main()
