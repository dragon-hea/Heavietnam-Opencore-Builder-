import shutil
import os

def copy_files(source_folder, destination_folder, files_to_copy):
    """
    Sao chép một nhóm file từ thư mục nguồn đến thư mục đích.

    Args:
    source_folder (str): Đường dẫn đến thư mục nguồn chứa các file.
    destination_folder (str): Đường dẫn đến thư mục đích nơi file sẽ được sao chép đến.
    files_to_copy (list): Danh sách tên các file cần sao chép.
    """
    # Đảm bảo thư mục đích tồn tại
    os.makedirs(destination_folder, exist_ok=True)
    
    # Lặp qua từng file trong danh sách và sao chép
    for file_name in files_to_copy:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        
        # Kiểm tra file tồn tại trước khi sao chép
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Đã sao chép {file_name} từ {source_folder} đến {destination_folder}.")
        else:
            print(f"Không tìm thấy {file_name} trong {source_folder}.")

# Ví dụ về cách sử dụng hàm:
source_folder = 'extra/ACPI'
destination_folder = 'extra/X64/EFI/OC/ACPI'
I225_v = [
    'SSDT-I225V.aml'
]
desktop1 = [
    'SSDT-EC-DESKTOP.aml'
    ]  
desktop2_3 = [
    'SSDT-EC-DESKTOP.aml'
]
desktop4_5 =[
    'SSDT-PLUG-DRTNIA.aml',
    'SSDT-EC-DESKTOP.aml'
]
desktop6_7 =[
    'SSDT-PLUG-DRTNIA.aml',
    'SSDT-EC-USBX-DESKTOP.aml'
]
desktop8_9 =[
    'SSDT-PLUG-DRTNIA.aml',
    'SSDT-EC-USBX-DESKTOP.aml',
    'SSDT-AWAC.aml',
    'SSDT-PMC.aml'  
]
desktop10 =[
    'SSDT-PLUG-DRTNIA.aml',
    'SSDT-EC-USBX-DESKTOP.aml', 
    'SSDT-AWAC.aml',
    'SSDT-RHUB.aml'  
]
desktop11_12_13 =[
    'SSDT-PLUG-ALT.aml',
    'SSDT-EC-USBX-DESKTOP.aml',  
    'SSDT-AWAC.aml',
    'SSDT-RHUB.aml',  
    'SSDT-MCHC.aml',
    'SSDT-SMBUS.aml'
]
laptop1 =[
    'SSDT-EC-LAPTOP.aml',
    'SSDT-PNLF.aml'
]
laptop2_3 =[
    'SSDT-EC-LAPTOP.aml',
    'SSDT-PNLF.aml',
    'SSDT-IMEI.aml'  
]
laptop4_5 = [
    'SSDT-EC-LAPTOP.aml',
    'SSDT-PNLF.aml',
    'SSDT-PLUG-DRTNIA.aml', 
    'SSDT-XOSI.aml' 
]
laptop6_7 = [
    'SSDT-EC-USBX-LAPTOP.aml',
    'SSDT-PNLF.aml',
    'SSDT-PLUG-DRTNIA.aml',
    'SSDT-XOSI.aml' 
]
laptop8 = [
    'SSDT-EC-USBX-LAPTOP.aml',
    'SSDT-PNLF.aml',
    'SSDT-PLUG-DRTNIA.aml',
    'SSDT-XOSI.aml', 
    'SSDT-AWAC.aml'
    ]
laptop9 = [
    'SSDT-EC-USBX-LAPTOP.aml',
    'SSDT-PNLF.aml',
    'SSDT-PLUG-DRTNIA.aml',
    'SSDT-XOSI.aml', 
    'SSDT-AWAC.aml',
    'SSDT-PMC.aml'  
]
laptop10 =[
    'SSDT-EC-USBX-LAPTOP.aml',
    'SSDT-PNLF.aml',
    'SSDT-PLUG-DRTNIA.aml',
    'SSDT-XOSI.aml', 
    'SSDT-AWAC.aml',
    'SSDT-RHUB.aml'    
]
dell =[
    'SSDT-BKeyBRT6-dell.aml',
    'SSDT-OCWork-dell.aml'
]
asus = [
    'SSDT-OCWork-asus.aml'
    ]
gprw = [
    'SSDT-GPRW.aml'
]
# Cập nhật danh sách file theo yêu cầu
def main(fileACPI):
    copy_files(source_folder, destination_folder, fileACPI)
