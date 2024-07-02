from testdownload import download_release_files
import testmove as move
import removefile as remove 
import driver as driver
import ACPIdownload as ACPI
import GUI as GUI
import json
import testconfig as quirk
import tools as tools
import os
def buildOC():
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
    OC_ver = data["OpenCore version"]

    #Tiến hành tải opencorepkg
    if OC_ver == "OpenCore standard":
        download_release_files('acidanthera', 'OpencorePKG', 'release')
    else:
        download_release_files('wjz304', 'OpenCore_NO_ACPI_Build', 'release')

    #Tải các kext bắt buộc
    download_release_files('acidanthera', 'LILU', 'release')
    download_release_files('acidanthera', 'VirtualSMC', 'release')
    download_release_files('acidanthera', 'WhateverGreen', 'release')
    download_release_files('USBToolBox', 'kext', 'release')
    download_release_files('acidanthera', 'AppleALC', 'release')
    download_release_files('acidanthera', 'HibernationFixup', 'release')
    if type == 'Laptop':
        download_release_files('acidanthera', 'VoodooPS2', 'release')
        move.movekext('VoodooPS2Controller.kext')
    move.movekext('AppleALC.kext')
    move.movekext('Lilu.kext')
    move.movekext('WhateverGreen.kext')
    move.movekext('SMCProcessor.kext')
    move.movekext('SMCSuperIO.kext')
    move.movekext('USBToolBox.kext')
    move.movekext('VirtualSMC.kext')
    move.movekext('HibernationFixup.kext')
    #di chuyển và đổi tên config.plist
    move.main()
    #Xoá các driver dư thừa
    driver.main()
    #Tiến thêm resource
    GUI.main()


    #Tiến hành thêm các ACPI
    ACPI.main(ACPI.gprw)
    if type == 'Laptop' or type == 'NUC':
        if cpu_generation == "Clarksfield and Arrandale":
            ACPI.main(ACPI.laptop1)
        if cpu_generation == "Sandy Bridge" or cpu_generation == "Ivy Bridge":
            ACPI.main(ACPI.laptop2_3)
        if cpu_generation == "Haswell" or cpu_generation == "Broadwell":
            ACPI.main(ACPI.laptop4_5)
        if cpu_generation == "Skylake" or cpu_generation == "Kaby Lake":
            ACPI.main(ACPI.laptop6_7)
        if cpu_generation == "Coffee Lake":
            ACPI.main(ACPI.laptop8)
        if cpu_generation == "Comet Lake":
            ACPI.main(ACPI.laptop9)
        if cpu_generation == "Ice Lake":
            ACPI.main(ACPI.laptop10)
        if laptopmodel == "Dell":
            ACPI.main(ACPI.dell)
        if laptopmodel == "Asus":
            ACPI.main(ACPI.asus)
    if type == 'Desktop':
        if cpu_generation == "Nehalem":
            ACPI.main(ACPI.desktop1)
        if cpu_generation == "Sandy Bridge" or cpu_generation == 'Ivy Bridge':
            ACPI.main(ACPI.desktop2_3)
        if cpu_generation == "Haswell" or cpu_generation == "Broadwell":
            ACPI.main(ACPI.desktop4_5)
        if cpu_generation == "Skylake" or cpu_generation == "Kaby Lake":
            ACPI.main(ACPI.desktop6_7)
        if cpu_generation == "Coffee Lake":
            ACPI.main(ACPI.desktop8_9)
        if cpu_generation == "Comet Lake":
            ACPI.main(ACPI.desktop10)
        if cpu_generation == "Tiger Lake" or cpu_generation == "Alder Lake" or cpu_generation == "Raptor Lake" or cpu_generation == 'Rocket Lake':
            ACPI.main(ACPI.desktop11_12_13)


    #Các plugin virtualSMC
    if type == 'Laptop':
        move.movekext('SMCBatteryManager.kext')
    if laptopmodel == "Dell":
        move.movekext('SMCDellSensors.kext')
    if laptopmodel == "Asus":
        download_release_files('hieplpvip', 'AsusSMC', 'release')
        move.movekext('AsusSMC.kext')    
    #Ethernet
    if Checklan == "Yes":
        if Lan == "Intel":
            if Lanmodel == "Intel's 82578, 82579, I217, I218 and I219 NICs":
                download_release_files('acidanthera', 'IntelMausi', 'release')
                move.movekext('IntelMausi.kext')
            if Lanmodel == "I211 NICs" and Macos == 'Big Sur':
                download_release_files('khronokernel', 'SmallTree-I211-AT-patch', 'smalltreeintel')
                move.movekext('SmallTreeIntel82576.kext')
            if Lanmodel == "I211 NICs":
                if Macos == 'Monterey' or Macos == 'Ventura' or Macos =='Sonoma14.0' or Macos == 'Sonoma14.4':
                    download_release_files('donatengit', 'AppleIGB', 'debug')
                    move.movekext('AppleIGB.kext')
            if Lanmodel == "I225-V":
                ACPI.main(ACPI.I225_v)
                if Macos == 'Ventura' or Macos == 'Sonoma14.0' or Macos == 'Sonoma14.4':
                    download_release_files('HeaDragon', 'AII210E', 'aii210e')
                    move.movekext('AppleIntelI210Ethernet.kext')
            if Lanmodel == "Intel I350 1Gb NIC":
                print('To patch intel I350 1Gb NIC https://heavietnam.gitbook.io/basic-guide/network/fix-ethernet#patch-i225-v')

        if Lan == "Atheros":
            if Lanmodel == "Atheros Killer E2500":
                download_release_files('Mieze', 'RTL8111_driver_for_OS_X', 'realtekrtl8111')
                move.movekext('RealtekRTL8111.kext')
            if Lanmodel == 'other':
                download_release_files('Mieze', 'AtherosE2200Ethernet', 'atherose2200')
                move.movekext('AtherosE2200Ethernet.kext')
        if Lan == "Realtek":
            if Lanmodel == "Realtek's 2.5Gb Ethernet":
                download_release_files('Mieze', 'LucyRTL8125Ethernet', 'LucyRTL8125')
                move.movekext('LucyRTL8125Ethernet.kext')
            if Lanmodel == 'other':
                download_release_files('Mieze', 'RTL8111_driver_for_OS_X', 'RealtekRTL8111')
                move.movekext('RealtekRTL8111.kext')
    if CheckWiFi == 'Yes':
        if WiFi == "Atheros":
            print('To patch Atheros https://heavietnam.gitbook.io/basic-guide/network/fix-wifi-va-bluetooth')
        if WiFi == "Intel":
            if Macos == 'Mojave':
                download_release_files('OpenIntelWireless', 'itlwm', 'mojave')
                move.movekext('AirportItlwm.kext')  
            if Macos == 'Catalina':
                download_release_files('OpenIntelWireless', 'itlwm', 'catalina')
                move.movekext('AirportItlwm.kext')
            if Macos == 'Big Sur':
                download_release_files('OpenIntelWireless', 'itlwm', 'bigSur')
                move.movekext('AirportItlwm.kext')
            if Macos == 'Monterey':
                download_release_files('OpenIntelWireless', 'itlwm', 'monterey')
                move.movekext('AirportItlwm.kext')
            if Macos == 'Ventura':
                download_release_files('OpenIntelWireless', 'itlwm', 'ventura')
                move.movekext('AirportItlwm.kext')
            if Macos == 'Sonoma14.0':
                download_release_files('OpenIntelWireless', 'itlwm','sonoma14.0')
                move.movekext('AirportItlwm.kext')
            if Macos == 'Sonoma14.4':
                download_release_files('OpenIntelWireless', 'itlwm','sonoma14.4')
                move.movekext('AirportItlwm.kext')
            download_release_files('OpenIntelWireless', 'IntelBluetoothFirmware', 'intelbluetooth')
            move.movekext('IntelBluetoothFirmware.kext')
            if Macos == 'Catalina' or Macos == 'Mojave' or Macos == 'Big Sur':
                move.movekext('IntelBluetoothInjector.kext')
            if wifimodel == 'AxXXX':
                move.movekext('IntelBTPatcher.kext')
            if Macos == 'Monterey' or Macos == 'Ventura' or Macos =='Sonoma14.0' or Macos == 'Sonoma14.4':
                download_release_files('acidanthera', 'BrcmPatchRAM', 'release')   
                move.movekext('BlueToolFixup.kext')  
        if WiFi == "Broadcom":
            download_release_files('acidanthera', 'AirportBrcmFixup', 'release')  
            move.movekext('AirportBrcmFixup.kext')
            download_release_files('acidanthera', 'BrcmPatchRAM', 'release')  
            move.movekext('BrcmFirmwareData.kext')
            if Macos == 'Mojave':
                move.movekext('BrcmPatchRAM2.kext')
            else:
                move.movekext('BrcmPatchRAM3.kext') 
            if Macos == 'Big Sur' or Macos == 'Monterey' or Macos == 'Ventura' or Macos =='Sonoma14.0' or Macos == 'Sonoma14.4':
                move.movekext('BlueToolFixup.kext') 
            else:
                move.movekext('BrcmBluetoothInjector.kext')

    if Drive == 'other':
        if Drivetype == 'NVMe':
            download_release_files('acidanthera', 'NVMeFix', 'release')
            move.movekext('NVMeFix.kext')
        if Drivetype == 'SATA':
            if Macos == 'Mojave' or Macos == 'Catalina':
                download_release_files('HeaDragon', 'SATA-unsupported', 'SATA-unsupported')
                move.movekext('SATA-unsupported.kext')
            else:
                download_release_files('HeaDragon', 'CtlnaAHCIPort', 'CtlnaAHCIPort')
                move.movekext('CtlnaAHCIPort.kext')

    if cpu_generation == "Alder Lake" or cpu_generation == 'Raptor Lake':
        download_release_files('b00t0x', 'CpuTopologyRebuild', 'release')
        move.movekext('CpuTopologyRebuild.kext')
    if checktrackpad == 'Yes':
        if typetrackpad == 'i2c':
            download_release_files('VoodooI2C', 'VoodooI2C', 'VoodooI2C')
            move.movekext('VoodooI2C.kext')
            if modeltrackpad == 'Synaptics':
                move.movekext('VoodooI2CSynaptics.kext')
                download_release_files('VoodooSMBus', 'VoodooRMI', 'release')
                move.movekext('VoodooRMI.kext')
            if modeltrackpad == 'HID':
                move.movekext('VoodooI2CHID.kext')
            if modeltrackpad == 'ELAN':
                move.movekext('VoodooI2CELAN.kext')
            if modeltrackpad == 'FTE':
                move.movekext('VoodooI2CFTE.kext')
            if modeltrackpad == 'AtmelMXT':
                move.movekext('VoodooI2CAtmelMXT.kext')
    if type == 'Laptop':
        download_release_files('1Revenger1', 'ECEnabler', 'release')
        move.movekext('ECEnabler.kext')
        if laptopmodel != 'Asus':
            download_release_files('acidanthera', 'BrightnessKeys', 'release')
            move.movekext('BrightnessKeys.kext')

    tools.main()        
    remove.main()
buildOC()