import requests
import os
from testextra import unzip_file

def download_release_files(user, repo, keyword):
    keyword = keyword.lower()
    # Lấy URL của API cho releases
    url = f"https://api.github.com/repos/{user}/{repo}/releases/latest"

    # Gửi yêu cầu GET để nhận thông tin release mới nhất
    response = requests.get(url)
    response.raise_for_status()  # Ném lỗi nếu yêu cầu thất bại
    release_data = response.json()

    # Đảm bảo có ít nhất một asset để tải về
    assets = release_data.get('assets', [])
    if not assets:
        print("Không có assets nào để tải xuống.")
        return

    # Lọc và tải xuống chỉ các assets chứa từ khóa 'releases' trong tên
    filtered_assets = [asset for asset in assets if keyword in asset['name'].lower()]
    if not filtered_assets:
        print(f"Không có assets nào chứa từ khóa '{keyword}'.")
        return

    for asset in filtered_assets:
        asset_url = asset['browser_download_url']
        asset_name = asset['name']
        print(f"Đang tải xuống {asset_name}...")

        # Gửi yêu cầu GET với stream=True để tải xuống tập tin
        with requests.get(asset_url, stream=True) as r:
            r.raise_for_status()
            # Lưu tập tin vào đường dẫn hiện tại
            with open(asset_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # lọc ra keep-alive new chunks
                        f.write(chunk)
        print(f"Đã tải xuống {asset_name}")
        unzip_file(asset_name, 'extra')
if __name__ == "__main__":
    # Thay đổi 'user' và 'repo' với tên người dùng và kho lưu trữ bạn muốn tải xuống
    download_release_files('acidanthera', 'VirtualSMC', 'release')
