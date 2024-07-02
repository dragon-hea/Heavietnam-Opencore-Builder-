import plistlib
# Database Device properties GPUs
laptop2igpu = {
    'AAPL,snb-platform-id': bytes.fromhex('00000100'),
    'AAPL00,DualLink': bytes.fromhex('01000000')
}
NUC2igpu = {
    'AAPL,snb-platform-id': bytes.fromhex('10000300'),
    'AAPL00,DualLink': bytes.fromhex('01000000')
}
laptop3igpu_1366x768 = {
    'AAPL,ig-platform-id': bytes.fromhex('03006601')
}
laptop3igpu1600x900 = {
    'AAPL,ig-platform-id': bytes.fromhex('04006601'),
    'framebuffer-patch-enable': 1,
    'framebuffer-memorycount': 2,
    'framebuffer-pipecount': 2,
    'framebuffer-portcount': 4,
    'framebuffer-stolenmem': bytes.fromhex('00000004'),
    'framebuffer-con1-enable': 1,
    'framebuffer-con1-alldata': bytes.fromhex('020500000004000007040000030400000004000081000000040600000004000081000000')
}
laptop3igpuedp = {
    'AAPL,ig-platform-id': bytes.fromhex('09006601')
}
NUC3igpu = {
    'AAPL,ig-platform-id': bytes.fromhex('0B006601')
}
laptop4igpu5000_5200 = {
    'AAPL,ig-platform-id': bytes.fromhex('0500260A'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000'),
    'framebuffer-cursormem': bytes.fromhex('00009000')
}
laptop4igpu4200_4600 = {
    'AAPL,ig-platform-id': bytes.fromhex('0600260A'),
    'device-id': bytes.fromhex('12040000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000'),
    'framebuffer-cursormem': bytes.fromhex('00009000')
}
NUC4igpu = {
    'AAPL,ig-platform-id': bytes.fromhex('0300220D'),
    'device-id': bytes.fromhex('12040000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000'),
    'framebuffer-cursormem': bytes.fromhex('00009000')
}
laptop5igpu = {
    'AAPL,ig-platform-id': bytes.fromhex('06002616'),
    'device-id': bytes.fromhex('26160000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
NUC5igpu = {
    'AAPL,ig-platform-id': bytes.fromhex('02001616'),
    'device-id': bytes.fromhex('26160000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
laptop6igpu515_550 = {
    'AAPL,ig-platform-id': bytes.fromhex('00001619'),
    'device-id': bytes.fromhex('16190000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
laptop6igpu510 = {
    'AAPL,ig-platform-id': bytes.fromhex('00001B19'),
    'device-id': bytes.fromhex('02190000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
NUC6igpu515 = {
    'AAPL,ig-platform-id': bytes.fromhex('00001E19'),
    'device-id': bytes.fromhex('16190000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
NUC6igpu520_530 = {
    'AAPL,ig-platform-id': bytes.fromhex('02001619'),
    'device-id': bytes.fromhex('16190000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
NUC6igpu540_550 = {
    'AAPL,ig-platform-id': bytes.fromhex('02002619'),
    'device-id': bytes.fromhex('16190000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
NUC6igpu580 = {
    'AAPL,ig-platform-id': bytes.fromhex('05003B19'),
    'device-id': bytes.fromhex('16190000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
laptop7igpu615_650 = {
    'AAPL,ig-platform-id': bytes.fromhex('00001B59'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000'),
    'framebuffer-con1-enable': bytes.fromhex('01000000'),
    'framebuffer-con1-alldata': bytes.fromhex('01050A000008000087010000'),
    'framebuffer-con2-enable': bytes.fromhex('01000000'),
    'framebuffer-con2-alldata': bytes.fromhex('02040A000008000087010000')
}
laptop7igpuUHD = {
    'AAPL,ig-platform-id': bytes.fromhex('0000C087'),
    'device-id': bytes.fromhex('16590000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
NUC7igpu615 = {
    'AAPL,ig-platform-id': bytes.fromhex('00001E59'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000'),
    'framebuffer-con1-enable': bytes.fromhex('01000000'),
    'framebuffer-con1-alldata': bytes.fromhex('01050A000008000087010000'),
    'framebuffer-con2-enable': bytes.fromhex('01000000'),
    'framebuffer-con2-alldata': bytes.fromhex('02040A000008000087010000')
}
NUC7igpu630 = {
    'AAPL,ig-platform-id': bytes.fromhex('00001B59'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000'),
    'framebuffer-con1-enable': bytes.fromhex('01000000'),
    'framebuffer-con1-alldata': bytes.fromhex('01050A000008000087010000'),
    'framebuffer-con2-enable': bytes.fromhex('01000000'),
    'framebuffer-con2-alldata': bytes.fromhex('02040A000008000087010000')
}
NUC7igpu640_650 = {
    'AAPL,ig-platform-id': bytes.fromhex('02002659'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000'),
    'framebuffer-con1-enable': bytes.fromhex('01000000'),
    'framebuffer-con1-alldata': bytes.fromhex('01050A000008000087010000'),
    'framebuffer-con2-enable': bytes.fromhex('01000000'),
    'framebuffer-con2-alldata': bytes.fromhex('02040A000008000087010000')
}
NUC7igpuUHD = {
    'AAPL,ig-platform-id': bytes.fromhex('00001659'),
    'device-id': bytes.fromhex('16590000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
Laptop8igpu630 = {
    'AAPL,ig-platform-id': bytes.fromhex('0900A53E'),
    'device-id': bytes.fromhex('9B3E0000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
Laptop8igpu620 = {
    'AAPL,ig-platform-id': bytes.fromhex('00009B3E'),
    'device-id': bytes.fromhex('9B3E0000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
NUC8igpu620_630 = {
    'AAPL,ig-platform-id': bytes.fromhex('07009B3E'),
    'device-id': bytes.fromhex('9B3E0000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
NUC8igpu655 = {
    'AAPL,ig-platform-id': bytes.fromhex('0000A53E'),
    'device-id': bytes.fromhex('9B3E0000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
laptop10igpuG1 = {
    'AAPL,ig-platform-id': bytes.fromhex('01005C8A'),
    'device-id': bytes.fromhex('5C8A0000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}
laptop10igpuG4_G7 = {
    'AAPL,ig-platform-id': bytes.fromhex('0000528A'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}

desktop2 = {
    'AAPL,snb-platform-id': bytes.fromhex('10000300'),
    'device-id': bytes.fromhex('26010000'),
}

desktop3 = {
    'AAPL,ig-platform-id': bytes.fromhex('0A006601'),
}

desktop4 = {
    'AAPL,ig-platform-id': bytes.fromhex('0300220D'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}

desktop4hd4400 = {
    'AAPL,ig-platform-id': bytes.fromhex('0300220D'),
    'device-id': bytes.fromhex('12040000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}

desktop5 = {
    'AAPL,ig-platform-id': bytes.fromhex('07002216'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}

desktop6 = {
    'AAPL,ig-platform-id': bytes.fromhex('00001219'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}

desktop6p350 = {
    'AAPL,ig-platform-id': bytes.fromhex('00001219'),
    'device-id': bytes.fromhex('1B190000'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}

desktop7 = {
    'AAPL,ig-platform-id': bytes.fromhex('00001259'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}

desktop8 = {
    'AAPL,ig-platform-id': bytes.fromhex('07009B3E'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}

desktop9_10 = {
    'AAPL,ig-platform-id': bytes.fromhex('07009B3E'),
    'framebuffer-patch-enable': bytes.fromhex('01000000'),
    'framebuffer-stolenmem': bytes.fromhex('00003001'),
    'framebuffer-fbmem': bytes.fromhex('00009000')
}

def load_plist(filepath):
    with open(filepath, 'rb') as file:
        plist_data = plistlib.load(file)
    return plist_data

def save_plist(data, filepath):
    with open(filepath, 'wb') as file:
        plistlib.dump(data, file)

def add_new_device_property(plist_data, properties):
    # Kiểm tra xem 'DeviceProperties' và 'Add' có tồn tại hay không
    if 'DeviceProperties' in plist_data and 'Add' in plist_data['DeviceProperties']:
        # Đường dẫn thiết bị cần thêm thông tin
        device_path = 'PciRoot(0x0)/Pci(0x2,0x0)'

        # Thêm hoặc cập nhật thông tin mới
        plist_data['DeviceProperties']['Add'].setdefault(device_path, {}).update(properties)
        print(f"Thông tin đã được thêm/cập nhật cho {device_path}.")
    else:
        print("Không tìm thấy 'DeviceProperties' hoặc 'Add'. Vui lòng kiểm tra file plist.")

def main(properties):
    # Đường dẫn đến file plist của bạn
    plist_path = 'extra/X64/EFI/OC/Config.plist'
    # Tải dữ liệu plist
    plist_data = load_plist(plist_path)
    # Thêm thông tin mới vào DeviceProperties sử dụng properties như là một tham số
    add_new_device_property(plist_data, properties)
    # Lưu lại thay đổi
    save_plist(plist_data, plist_path)
