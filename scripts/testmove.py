import shutil
import os

def move_specific_file(src_folder, dest_folder, file_name):
    # Kiểm tra và di chuyển file cụ thể từ src_folder sang dest_folder
    file_path = os.path.join(src_folder, file_name)
    if os.path.isfile(file_path):
        shutil.move(file_path, os.path.join(dest_folder, file_name))
        print(f"Moved: {file_path} to {dest_folder}")
    else:
        print(f"No such file: {file_path}")

def move_folders_with_name(src_folder, dest_folder, folder_name):
    # Duyệt qua tất cả các thư mục và thư mục con, di chuyển tất cả các thư mục có tên cụ thể
    for root, dirs, files in os.walk(src_folder, topdown=False):
        if 'debug' in os.path.relpath(root, src_folder).lower().split(os.sep):
            continue
        for dir in dirs:
            if dir == folder_name:
                dir_path = os.path.join(root, dir)
                dest_path = os.path.join(dest_folder, dir)
                try:
                    shutil.move(dir_path, dest_path)
                    print(f"Moved directory: {dir_path} to {dest_path}")
                except Exception as e:
                    print(f"Could not move {dir_path}: {e}")

def rename():
    old_name_relative = "extra/X64/EFI/OC/Sample.plist"
    new_name_relative = "extra/X64/EFI/OC/Config.plist"
    os.rename(old_name_relative, new_name_relative)

def main():
    folder_a = 'extra/docs'
    folder_b = 'extra/X64/EFI/OC'
    specific_file = 'Sample.plist'  # Đặt tên file cụ thể bạn muốn di chuyển
    move_specific_file(folder_a, folder_b, specific_file)
    rename()
def movekext(file_name):
        folder_c = 'extra'
        destination_folder = 'extra/X64/EFI/OC/Kexts'
        move_folders_with_name(folder_c, destination_folder, file_name)

