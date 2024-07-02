import os
import shutil

def delete_files_and_folders(directory):
    # Duyệt qua thư mục gốc và tất cả thư mục con, sử dụng topdown=False để xóa từ thư mục con trước khi xóa thư mục cha
    for root, dirs, files in os.walk(directory, topdown=False):
        # Xóa các file kết thúc bằng .zip
        for file in files:
            if file.lower().endswith('.zip'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Could not delete {file_path}: {e}")
            
            # Xóa các file có tên cụ thể
            if file in ['alc-verb', 'AsusSMCDaemon', 'com.hieplpvip.AsusSMCDaemon.plist', 'install_daemon.sh']:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Could not delete {file_path}: {e}")

        # Xóa các thư mục kết thúc bằng .dsym
        for dir in dirs:
            if dir.lower().endswith('.dsym'):
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Deleted directory: {dir_path}")
                except Exception as e:
                    print(f"Could not delete {dir_path}: {e}")

def main():
    directory = os.getcwd()  # Lấy đường dẫn thư mục hiện tại
    delete_files_and_folders(directory)
