import shutil
import os

def move_and_replace(source_dir, target_dir):
    # Kiểm tra và xóa thư mục đích nếu nó đã tồn tại
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    # Di chuyển thư mục nguồn tới đích
    shutil.copytree(source_dir, target_dir)

# Ví dụ về việc di chuyển và thay thế thư mục
def main():
    source = 'extra/Resources'
    target = 'extra/X64/EFI/OC/Resources'
    move_and_replace(source, target)
