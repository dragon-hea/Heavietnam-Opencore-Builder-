import subprocess
import uuid
import plistlib
import os

def update_plist(plist_path, model, serial_number, smuuid,mlb):
    if not os.path.exists(plist_path):
        print(f"File {plist_path} không tồn tại.")
        return False

    with open(plist_path, 'rb') as fp:
        plist_data = plistlib.load(fp)

    # Đảm bảo các nhóm cha và con tồn tại trước khi cập nhật
    if 'PlatformInfo' not in plist_data:
        plist_data['PlatformInfo'] = {}
    if 'Generic' not in plist_data['PlatformInfo']:
        plist_data['PlatformInfo']['Generic'] = {}

    # Cập nhật các giá trị theo đường dẫn mới
    plist_data['PlatformInfo']['Generic']['SystemProductName'] = model
    plist_data['PlatformInfo']['Generic']['SystemSerialNumber'] = serial_number
    plist_data['PlatformInfo']['Generic']['SystemUUID'] = smuuid
    plist_data['PlatformInfo']['Generic']['MLB'] = mlb

    # Ghi lại file plist với thông tin đã cập nhật
    with open(plist_path, 'wb') as fp:
        plistlib.dump(plist_data, fp)

    print(f"Đã cập nhật file {plist_path} thành công.")
    return True

def generate_serial_mlb_smuuid(model):
    macserial_path = r"extra\Utilities\macserial\macserial.exe"
    command = f'"{macserial_path}" -m {model}'
    print("Running command:", command)

    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    if result.returncode == 0:
        output = result.stdout.strip().split()
        serial_number = output[0] if len(output) > 0 else "Serial Not Found"
        mlb = output[2] if len(output) > 1 else "MLB Not Found"
        smuuid = str(uuid.uuid4()).upper()
        return serial_number, mlb, smuuid
    else:
        print("Lỗi khi generate Serial và MLB:", result.stderr)
        return None, None, None

# Đường dẫn tới file plist
def main(model):
    plist_path = 'extra/X64/EFI/OC/Config.plist'
    serial_number, mlb, smuuid = generate_serial_mlb_smuuid(model)

    if serial_number and mlb and smuuid:
        updated = update_plist(plist_path, model, serial_number, smuuid,mlb)

main('MacBookPro11,2')