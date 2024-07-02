import testconfig as quirk
import devicepp as device
import configimei as imei
import ACPIconfig as aciconfig
import smbios as smbios
from removewarming import remove_warning_keys
import snapshot as snapshot
import json
import enableACPI as enableACPI
import enabledrivers as enabledrivers
import enable_kexts as enable_kext
import enable_trackpad_kexts as enable_trackpad_kext
import usbconfig as usbconfig
import os
def buildconfig():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'hackintosh_survey_results.json')
    # Mở file và đọc dữ liệu
    with open(file_path, 'r') as file:
        data = json.load(file)

    cpu_generation = data["CPU Generation"]
    type = data["Device Type"]
    checkDGPU = data["Has DGPU"]
    checkIGPU = data["Has IGPU"]
    DGPU = data ["DGPU Brand"]
    AMDGPU = data["AMD GPU Type"]
    IGPU = data["IGPU Model"]
    Drivetype = data["Drive Type"]
    Drive = data["Drive Model"]
    CheckWiFi = data["Has WiFi Card"]
    WiFi = data ["WiFi Card Brand"]
    wifimodel = data["WiFi Card Model"]
    Macos = data ["macOS Version"]
    checktrackpad = data["Has Trackpad"]
    typetrackpad = data ["Trackpad Type"]
    modeltrackpad = data["Trackpad Model"]
    Checklan = data["Has LAN Card"]
    Lan = data["LAN Card Brand"]
    Lanmodel = data["LAN Card Model"]
    laptopmodel = data["Laptop Brand"]

    #Tiến hành snapshot
    snapshot.main()

    #Tiến hành remove warming key
    remove_warning_keys()

    #Tiến hành enable enable
    enableACPI.main()

    #Tiến hành enable drivers
    enabledrivers.main()

    #Tiến hành enable kext
    enable_kext.main()
    if checktrackpad == "Yes":
        #Tiến hành enable trackpad
        enable_trackpad_kext.main(typetrackpad)
    #Tiến hành thêm UTBMap.kext
    usbconfig.main()
    #Tiến hành config gui
    quirk.main(quirk.GUIquirk)

    #Thêm patch ACPI
    aciconfig.main(aciconfig.GPRWtoXPRW)
    if type == "Laptop":
        if cpu_generation == "Haswell" or cpu_generation == 'Broadwell' or cpu_generation == 'Skylake' or cpu_generation == 'Kaby Lake' or cpu_generation == 'Coffee Lake' or cpu_generation == 'Comet Lake' or cpu_generation == 'Ice Lake':
            aciconfig.main(aciconfig.OSItoXOSI)
        if laptopmodel == "Dell":
            aciconfig.main(aciconfig.BRT6toXBRT6)
            aciconfig.main(aciconfig.OSIDtoXSID)
        if laptopmodel == "Asus":
            aciconfig.main(aciconfig.PNLFtoXNLF)
    if type == 'Desktop':
        if cpu_generation == 'Rocket Lake' or cpu_generation == 'Tiger Lake' or cpu_generation == 'Alder Lake' or cpu_generation == 'Raptor Lake':
            aciconfig.main(aciconfig.ADBGtoXDBG)

    #Thêm patch imei
    if type == 'Laptop' or type == 'NUC':
        if cpu_generation == 'Ivy Bridge':
            imei.main(imei.laptopimeiivy)
        if cpu_generation == 'Sandy Bridge':
            imei.main(imei.laptopimeisandy)
    if type == 'Desktop':
        if cpu_generation == 'Sandy Bridge':
            imei.main(imei.desktopimeisandy)
        if cpu_generation == 'Ivy Bridge':
            imei.main(imei.desktopimeiivy)

    #Enable GUI
    quirk.main(quirk.GUIquirk)
    quirk.main(quirk.Dellquirk)
    #Config quirk 
    if type == 'Laptop' or type == 'NUC':
        if cpu_generation == "Clarksfield and Arrandale":
            quirk.main(quirk.laptop1)
        if cpu_generation == 'Ivy Bridge':
            quirk.main(quirk.laptop3)
        if cpu_generation == 'Sandy Bridge':
            quirk.main(quirk.laptop2)
        if cpu_generation == 'Haswell':
            quirk.main(quirk.laptop4)
        if cpu_generation == 'Broadwell':
            quirk.main(quirk.laptop5)
        if cpu_generation == 'Skylake':
            quirk.main(quirk.laptop6)
        if cpu_generation == 'Kaby Lake':
            quirk.main(quirk.laptop7)
        if cpu_generation == 'Coffee Lake':
            quirk.main(quirk.laptop8)
        if cpu_generation == 'Comet Lake':
            quirk.main(quirk.laptop9)
        if cpu_generation == 'Ice Lake':
            quirk.main(quirk.laptop10)
    if laptopmodel == "HP":
        quirk.main(quirk.HPquirk)
    if type == 'Desktop':
        if cpu_generation == 'Sandy Bridge':
            quirk.main(quirk.desktop2)
        if cpu_generation == 'Ivy Bridge':
            quirk.main(quirk.desktop3)
        if cpu_generation == 'Haswell' or cpu_generation == 'Broadwell':
            quirk.main(quirk.desktop4_5)
        if cpu_generation == 'Skylake':
            quirk.main(quirk.desktop6)
        if cpu_generation == 'Kaby Lake':
            quirk.main(quirk.desktop7)
        if cpu_generation == 'Coffee Lake':
            quirk.main(quirk.desktop8_9)
        if cpu_generation == 'Comet Lake' or cpu_generation == 'Ice Lake':
            quirk.main(quirk.desktop10)
        if cpu_generation == 'Rocket Lake' or cpu_generation == 'Tiger Lake' or cpu_generation == 'Alder Lake' or cpu_generation == 'Raptor Lake':
            quirk.main(quirk.desktop_11_12_13)
        
    #DevicePP
    if type == 'Laptop':
        if IGPU == '1366 x 768':
            device.main(device.laptop3igpu_1366x768)
        if IGPU == '1600 x 900':
            device.main(device.laptop3igpu1600x900)
        if IGPU == 'EDP':
            device.main(device.laptop3igpuedp)
        if IGPU == 'HD 4x':
            device.main(device.laptop4igpu4200_4600)
        if IGPU == 'HD 5x':
            device.main(device.laptop4igpu5000_5200)
        if IGPU == 'HD 5600' or IGPU == 'other':
            device.main(device.laptop5igpu)
        if IGPU == 'HD (515-550)' or IGPU == 'P350':
            device.main(device.laptop6igpu515_550)
        if IGPU == 'HD 510':
            device.main(device.laptop6igpu510)
        if IGPU == 'HD(615-650)':
            device.main(device.laptop7igpu615_650)
        if cpu_generation == 'Kaby Lake' and IGPU == 'UHD 620':
            device.main(device.laptop7igpuUHD)
        if (cpu_generation == 'Coffee Lake' or cpu_generation == 'Comet Lake') and IGPU == 'UHD 620':
            device.main(device.Laptop8igpu620)
        if (cpu_generation == 'Coffee Lake' or cpu_generation == 'Comet Lake') and IGPU == 'UHD 630':
            device.main(device.Laptop8igpu630)
        if IGPU == 'UHD G1':
            device.main(device.laptop10igpuG1)
        if IGPU == 'G4, G7':
            device.main(device.laptop10igpuG4_G7)
    if type == 'NUC':
        if cpu_generation == 'Sandy Bridge':
            device.main(device.NUC2igpu)
        if cpu_generation == 'Ivy Bridge':
            device.main(device.NUC3igpu)
        if cpu_generation == 'Haswell':
            device.main(device.NUC4igpu)
        if cpu_generation == 'Broadwell':
            device.main(device.NUC5igpu)
        if cpu_generation == 'Skylake':
            if IGPU == 'HD 515':
                device.main(device.NUC6igpu515)
            if IGPU == "HD (520-530)":
                device.main(device.NUC6igpu520_530)
            if IGPU == "HD (540-550)":
                device.main(device.NUC6igpu540_550)
            if IGPU == "HD 580":
                device.main(device.NUC6igpu580)
        if cpu_generation == 'Kaby Lake':
            if IGPU == "HD 615":
                device.main(device.NUC7igpu615)
            if IGPU == "HD 630":
                device.main(device.NUC7igpu630)
            if IGPU == "HD (640-650)":
                device.main(device.NUC7igpu640_650)
            if IGPU == "UHD 620":
                device.main(device.NUC7igpuUHD)
        if cpu_generation == 'Coffee Lake':
            if IGPU == 'UHD (620-630)':
                device.main(device.NUC8igpu620_630)
            if IGPU == 'UHD (655)':
                device.main(device.NUC8igpu655)
    if type == 'Desktop':
        if cpu_generation == 'Sandy Bridge':
            device.main(device.desktop2)
        if cpu_generation == 'Ivy Bridge':
            device.main(device.desktop3)
        if cpu_generation == 'Haswell':
            if IGPU == "HD 4400":
                device.main(device.desktop4hd4400)
            if IGPU == 'other':
                device.main(device.desktop4)
        if cpu_generation == 'Broadwell':
            device.main(device.desktop5)
        if cpu_generation == 'Skylake':
            if IGPU == 'other':
                device.main(device.desktop6)
            if IGPU == "HD P350":
                device.main(device.desktop6p350)
        if cpu_generation == 'Kaby Lake':
            device.main(device.desktop7)
        if cpu_generation == 'Coffee Lake':
            device.main(device.desktop8)
        if cpu_generation == 'Comet Lake' or cpu_generation == 'Ice Lake':
            device.main(device.desktop10)



    #Smbios
    if type == 'Laptop':
        if cpu_generation =='Clarksfield and Arrandale':
            smbios.main('MacBookPro6,1')
        if cpu_generation == 'Sandy Bridge':
            smbios.main('MacBookPro8,1')
        if cpu_generation == 'Ivy Bridge':
            if Macos == 'Catalina' or Macos == 'Mojave':
                smbios.main('MacBookPro10,2')
            if Macos == 'Big Sur':
                smbios.main('MacBookPro11,5')
            if Macos == 'Monterey':
                smbios.main('MacBookPro11,5')
            if Macos == 'Ventura':
                smbios.main('MacBookPro14,1')
        if cpu_generation == 'Haswell':
            if Macos == 'Catalina' or Macos == 'Mojave' or Macos == 'Big Sur':
                smbios.main('MacBookPro11,4')
            if Macos == 'Monterey':
                smbios.main('MacBookPro11,5')
            if Macos == 'Ventura':
                smbios.main('MacBookPro14,1')
        if cpu_generation == 'Broadwell':
            if Macos == 'Catalina' or Macos == 'Mojave' or Macos == 'Big Sur' or Macos == 'Monterey':
                smbios.main('MacBookPro11,5')
            if Macos == 'Ventura':
                smbios.main('MacBookPro14,1')
        if cpu_generation == 'Skylake':
            if Macos == 'Catalina' or Macos == 'Mojave' or Macos == 'Big Sur' or Macos == 'Monterey':
                smbios.main('MacBookPro13,3')
            if Macos == 'Ventura':
                smbios.main('MacBookPro14,1')     
        if cpu_generation == 'Kaby Lake':
            smbios.main('MacBookPro14,2')
        if cpu_generation == 'Coffee Lake':
            smbios.main('MacBookPro15,4')
        if cpu_generation == 'Comet Lake':
            smbios.main('MacBookPro16,4')
        if cpu_generation == 'Ice Lake':
            smbios.main('MacBookPro16,2')
    if type == 'NUC':
        if cpu_generation == 'Sandy Bridge':
            smbios.main('Macmini5,3')
        if cpu_generation == 'Ivy Bridge':
            smbios.main('Macmini6,2')
        if cpu_generation == 'Haswell':
            smbios.main('Macmini7,1')
        if cpu_generation == 'Broadwell':
            smbios.main('iMac16,1')
        if cpu_generation == 'Skylake':
            smbios.main('iMac17,1')
        if cpu_generation == 'Kaby Lake':
            smbios.main('iMac18,1')
        if cpu_generation == 'Coffee Lake':
            smbios.main('Macmini8,1')
        if cpu_generation == 'Comet Lake':
            smbios.main('Macmini8,1')
        if cpu_generation == 'Ice Lake':
            print('update later.....')
    if type == 'Desktop':
        if cpu_generation == "Clarksfield and Arrandale":
            smbios.main('MacPro6,1')
        if cpu_generation == "Sandy Bridge":
            smbios.main('MacPro6,1')
        if cpu_generation == "Ivy Bridge":
            if Macos == 'Mojave' or Macos == 'Catalina':
                smbios.main('iMac13,1')
            if Macos == 'Big Sur':
                smbios.main('iMac14,4')
            if Macos == 'Monterey':
                smbios.main('MacPro6,1')
        if cpu_generation == "Haswell":
            if checkDGPU == 'Yes':
                if DGPU == 'AMD':
                    if Macos == 'Mojave' or Macos =='Catalina' or Macos == 'Big Sur':
                        smbios.main('iMac15,1')
                    if Macos == 'Monterey':
                        smbios.main('iMac17,1')
                    if Macos == 'Ventura':
                        smbios.main('iMac18,1')
                if DGPU == 'NVIDIA':
                    if Macos == 'Mojave' or Macos =='Catalina' or Macos == 'Big Sur':
                        smbios.main('iMac14,4')
                    if Macos == 'Monterey':
                        smbios.main('iMac16,2')
                    if Macos == 'Ventura':
                        smbios.main('iMac18,1')
            if checkDGPU == 'No':
                if Macos == 'Mojave' or Macos =='Catalina' or Macos == 'Big Sur':
                    smbios.main('iMac14,4')
                if Macos == 'Monterey':
                    smbios.main('iMac16,2')
                if Macos == 'Ventura':
                    smbios.main('iMac18,1')
        if cpu_generation == "Broadwell":
            if checkDGPU == 'Yes':
                if DGPU == 'AMD':
                    if Macos == 'Mojave' or Macos =='Catalina' or Macos == 'Big Sur':
                        smbios.main('iMac16,2')
                    if Macos == 'Monterey':
                        smbios.main('iMac17,1')
                    if Macos == 'Ventura':
                        smbios.main('iMac18,1')
                if DGPU == 'NVIDIA':
                    if Macos == 'Mojave' or Macos =='Catalina' or Macos == 'Big Sur':
                        smbios.main('iMac16,2')
                    if Macos == 'Monterey':
                        smbios.main('iMac16,2')
                    if Macos == 'Ventura':
                        smbios.main('iMac18,1')
            if checkDGPU == 'No':
                if Macos == 'Mojave' or Macos =='Catalina' or Macos == 'Big Sur':
                    smbios.main('iMac16,2')
                if Macos == 'Monterey':
                    smbios.main('iMac16,2')
                if Macos == 'Ventura':
                    smbios.main('iMac18,1') 
        if cpu_generation == "Skylake":
            if Macos == 'Ventura' or Macos =='Sonoma14.0' or Macos == 'Sonoma14.4':
                smbios.main('iMac18,1')
            else:
                smbios.main('iMac17,1')
        if cpu_generation == 'Kaby Lake':
            smbios.main('iMac18,1')
        if cpu_generation == 'Coffee Lake':
            smbios.main('iMac19,1')
        if cpu_generation == 'Comet Lake':
            smbios.main('iMac20,1')
        if cpu_generation == 'Alder Lake' or cpu_generation == 'Raptor Lake' or cpu_generation == 'Tiger Lake' or cpu_generation == 'Rocket Lake':
            smbios.main('iMacPro1,1')

buildconfig()

