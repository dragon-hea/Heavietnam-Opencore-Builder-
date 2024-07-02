import os

def delete_files_in_tools(tools_dir):
    # Duyệt qua thư mục Tools
    for item in os.listdir(tools_dir):
        item_path = os.path.join(tools_dir, item)
        # Kiểm tra nếu là file thì xoá
        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"File đã xoá: {item_path}")
        # Nếu là thư mục con, xoá các file bên trong thư mục đó
        elif os.path.isdir(item_path):
            for sub_item in os.listdir(item_path):
                sub_item_path = os.path.join(item_path, sub_item)
                if os.path.isfile(sub_item_path):
                    os.remove(sub_item_path)
                    print(f"File đã xoá: {sub_item_path}")

# Đường dẫn đến thư mục Tools
tools_dir = 'extra/X64/EFI/OC/Tools'
def main():
    delete_files_in_tools(tools_dir)