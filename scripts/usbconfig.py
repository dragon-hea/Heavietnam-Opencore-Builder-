import plistlib

# Định nghĩa đường dẫn tới file plist
plist_file_path = 'extra/X64/EFI/OC/Config.plist'

# Định nghĩa kext UTBMap.kext
UTBMap_kext = {
    'Arch': 'x86_64',
    'BundlePath': 'UTBMap.kext',
    'Comment': 'UTBMap kext',
    'Enabled': True,
    'ExecutablePath': '',
    'MaxKernel': '',
    'MinKernel': '',
    'PlistPath': 'Contents/Info.plist'
}

# Hàm tải dữ liệu plist hiện tại
def load_existing_plist(filepath):
    with open(filepath, 'rb') as file:
        plist_data = plistlib.load(file)
    return plist_data

# Hàm lưu dữ liệu plist đã cập nhật
def save_updated_plist(data, filepath):
    with open(filepath, 'wb') as file:
        plistlib.dump(data, file)

# Hàm thêm kext vào plist
def add_kext(plist_data, kext):
    if 'Kernel' not in plist_data:
        plist_data['Kernel'] = {'Add': []}
    if 'Add' not in plist_data['Kernel']:
        plist_data['Kernel']['Add'] = []
        
    plist_data['Kernel']['Add'].append(kext)
    print("Kext đã được thêm thành công.")

def main():
    # Tải dữ liệu plist hiện tại
    plist_data = load_existing_plist(plist_file_path)
    # Thêm kext mới vào dữ liệu plist
    add_kext(plist_data, UTBMap_kext)
    # Lưu dữ liệu plist đã cập nhật lại vào file
    save_updated_plist(plist_data, plist_file_path)