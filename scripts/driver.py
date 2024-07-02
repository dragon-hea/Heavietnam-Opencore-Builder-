import os

def clean_drivers(directory, keep_files):
    # Duyệt qua các thư mục và file trong thư mục chính
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            if name not in keep_files:
                os.remove(file_path)
                print(f"Removed: {file_path}")
        # Xoá các thư mục trống
        for name in dirs:
            dir_path = os.path.join(root, name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Removed directory: {dir_path}")

# Đường dẫn tới thư mục Drivers
drivers_dir = 'extra/X64/EFI/OC/Drivers'

# Danh sách các file cần giữ
keep_drivers = [
    "ToggleSipEntry.efi", 
    "ResetNvramEntry.efi", 
    "OpenRuntime.efi", 
    "OpenHfsPlus.efi", 
    "OpenCanopy.efi"
]
def main():
    clean_drivers(drivers_dir, keep_drivers)
