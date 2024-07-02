import  plistlib
import json

file_path = 'hackintosh_survey_results.json'
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

#database config quirks
boot_args = '-v debug=0x100 keepsyms=1 alcid=1 npci=0x3000'

#Config boot-args
if IGPU == "UHD 620" or IGPU == "UHD 630" or IGPU == "UHD (620-630)" or IGPU == "UHD (655)" or IGPU == "UHD G1":
    boot_args += ' -igfxblr'
if type == 'Desktop':
    if checkDGPU == 'Yes':
        if checkIGPU == 'Yes' and DGPU != "AMD":
            boot_args += ' -wegnoegpu'
        if checkIGPU == 'Yes' and DGPU == "AMD":
            boot_args += ' -wegnoigpu'
if type == 'Laptop':
    if checkDGPU == 'Yes':
        boot_args += ' -wegnoegpu'
if DGPU == 'AMD':
    boot_args += ' unfairgva=1 -radcodec'
    if AMDGPU == 'Navi(10, 21, 22, 23)':
        boot_args += ' agdpmod=pikera'
    if AMDGPU == 'R7-R9':
        boot_args += ' radpg=15 -raddvi'
    if AMDGPU == 'HD (7x-8x)':
        boot_args += ' radpg=15'

if type == 'Laptop':
    if typetrackpad == 'i2c':
        boot_args += ' -vi2c-force-polling'
    if cpu_generation == 'Kaby Lake':
            boot_args += ' -igfxnotelemetryload'
    if cpu_generation == 'Coffee Lake':
            boot_args += ' -igfxnotelemetryload'
    if cpu_generation == 'Comet Lake':
            boot_args += ' -igfxnotelemetryload'
    if cpu_generation == 'Ice Lake':
            boot_args += ' -igfxcdc -igfxdvmt -igfxnotelemetryload'
if Lanmodel == "I225-V":
        if Macos == 'Big Sur':
            boot_args += ' dk.e1000=0'
        if Macos == 'Monterey'or Macos =='Ventura' or Macos == 'Sonoma14.4' or Macos == 'Sonoma14.0':
            boot_args += ' e1000=0'
if cpu_generation == "Alder Lake" or cpu_generation == 'Raptor Lake':
     boot_args +=' -ctrsmt'

desktop_11_12_13 = {
    "Booter": {
        "Quirks": {
            "DevirtualiseMmio": True,
            "EnableWriteUnprotector": False,
            "ProtectUefiServices": True,
            "RebuildAppleMemoryMap": True,
            "ResizeAppleGpuBars": -1,
            "SyncRuntimePermissions": True,
            "SetupVirtualMap": False
        }
    },
    "Kernel": {
        "Emulate": {
            "Cpuid1Data": bytes.fromhex('55060A00000000000000000000000000'),
            "Cpuid1Mask": bytes.fromhex('FFFFFFFF000000000000000000000000')
        },
        "Quirks": {
            "DisableIoMapper": True,
            "LapicKernelPanic": False,  # Chú ý cho HP
            "PanicNoKextDump": True,
            "PowerTimeoutKernelPanic": True,
            "XhciPortLimit": False,
            "AppleXcpmCfgLock": True,
            "ProvideCurrentCpuInfo": True
        }
    },
    "Misc": {
        "Boot": {
            "HideAuxiliary": True
        },
        "Debug": {
            "AppleDebug": True,
            "ApplePanic": True,
            "DisableWatchDog": True,
            "Target": 67
        },
        "Security": {
            "AllowSetDefault": True,
            "BlacklistAppleUpdate": True,
            "ScanPolicy": 0,
            "SecureBootModel": "Disabled",
            "Vault": "Optional"
        }
    },
    "NVRAM": {
        "Add": {
            "7C436110-AB2A-4BBB-A880-FE41995C9F82": {
                "boot-args": boot_args,
                "prev-lang:kbd": "en-US:0"
            }
        }
    },
    "UEFI": {
        "APFS": {
            "MinDate": -1,
            "MinVersion": -1
        },
        "Output": {
            "ProvideConsoleGop": True
        },
        "Quirks": {
            "UnblockFsConnect": False  # Chú ý cho HP
        }
    }
}


desktop10 = {
    "Booter": {
        "Quirks": {
            "DevirtualiseMmio": True,
            "EnableWriteUnprotector": False,
            "ProtectUefiServices": True,
            "RebuildAppleMemoryMap": True,
            "ResizeAppleGpuBars": -1,
            "SyncRuntimePermissions": True,
            "SetupVirtualMap": False
        }
    },
    "Kernel": {
        "Quirks": {
            "DisableIoMapper": True,
            "LapicKernelPanic": False,  # Chú ý cho HP
            "PanicNoKextDump": True,
            "PowerTimeoutKernelPanic": True,
            "XhciPortLimit": False,
            "AppleXcpmCfgLock": True
        }
    },
    "Misc": {
        "Boot": {
            "HideAuxiliary": True
        },
        "Debug": {
            "AppleDebug": True,
            "ApplePanic": True,
            "DisableWatchDog": True,
            "Target": 67
        },
        "Security": {
            "AllowSetDefault": True,
            "BlacklistAppleUpdate": True,
            "ScanPolicy": 0,
            "SecureBootModel": "Disabled",
            "Vault": "Optional"
        }
    },
    "NVRAM": {
        "Add": {
            "7C436110-AB2A-4BBB-A880-FE41995C9F82": {
                "boot-args": "boot_args",
                "prev-lang:kbd": "en-US:0"
            }
        }
    },
    "UEFI": {
        "APFS": {
            "MinDate": -1,
            "MinVersion": -1
        },
        "Quirks": {
            "UnblockFsConnect": False  # Chú ý cho HP
        }
    }
}


desktop8_9 = {
    "Booter": {
        "Quirks": {
            "DevirtualiseMmio": True,
            "EnableWriteUnprotector": False,
            "ProtectUefiServices": True,
            "RebuildAppleMemoryMap": True,
            "ResizeAppleGpuBars": -1,
            "SyncRuntimePermissions": True
        }
    },
    "Kernel": {
        "Quirks": {
            "DisableIoMapper": True,
            "LapicKernelPanic": False,  # Chú ý cho HP
            "PanicNoKextDump": True,
            "PowerTimeoutKernelPanic": True,
            "XhciPortLimit": False,
            "AppleXcpmCfgLock": True
        }
    },
    "Misc": {
        "Boot": {
            "HideAuxiliary": True
        },
        "Debug": {
            "AppleDebug": True,
            "ApplePanic": True,
            "DisableWatchDog": True,
            "Target": 67
        },
        "Security": {
            "AllowSetDefault": True,
            "BlacklistAppleUpdate": True,
            "ScanPolicy": 0,
            "SecureBootModel": "Disabled",
            "Vault": "Optional"
        }
    },
    "NVRAM": {
        "Add": {
            "7C436110-AB2A-4BBB-A880-FE41995C9F82": {
                "boot-args": boot_args,
                "prev-lang:kbd": "en-US:0"
            }
        }
    },
    "UEFI": {
        "APFS": {
            "MinDate": -1,
            "MinVersion": -1
        },
        "Quirks": {
            "UnblockFsConnect": False  # Chú ý cho HP
        }
    }
}


desktop7 = {
    "Kernel": {
        "Quirks": {
            "AppleCpuPmCfgLock": False,
            "AppleXcpmCfgLock": True,
            "DisableIoMapper": True,
            "LapicKernelPanic": False,  # Chú ý cho HP
            "PanicNoKextDump": True,
            "PowerTimeoutKernelPanic": True,
            "XhciPortLimit": False
        }
    },
    "Misc": {
        "Boot": {
            "HideAuxiliary": True
        },
        "Debug": {
            "AppleDebug": True,
            "ApplePanic": True,
            "DisableWatchDog": True,
            "Target": 67
        },
        "Security": {
            "AllowSetDefault": True,
            "BlacklistAppleUpdate": True,
            "ScanPolicy": 0,
            "SecureBootModel": "Disabled",
            "Vault": "Optional"
        }
    },
    "NVRAM": {
        "Add": {
            "7C436110-AB2A-4BBB-A880-FE41995C9F82": {
                "boot-args": boot_args,
                "prev-lang:kbd": "en-US:0"
            }
        }
    },
    "UEFI": {
        "APFS": {
            "MinDate": -1,
            "MinVersion": -1
        },
        "Quirks": {
            "UnblockFsConnect": False  # Chú ý cho HP
        }
    }
}


desktop6 = {
    "Kernel": {
        "Quirks": {
            "AppleCpuPmCfgLock": False,
            "AppleXcpmCfgLock": True,
            "DisableIoMapper": True,
            "LapicKernelPanic": False,  # Chú ý cho HP
            "PanicNoKextDump": True,
            "PowerTimeoutKernelPanic": True,
            "XhciPortLimit": False
        }
    },
    "Misc": {
        "Boot": {
            "HideAuxiliary": True
        },
        "Debug": {
            "AppleDebug": True,
            "ApplePanic": True,
            "DisableWatchDog": True,
            "Target": 67
        },
        "Security": {
            "AllowSetDefault": True,
            "BlacklistAppleUpdate": True,
            "ScanPolicy": 0,
            "SecureBootModel": "Disabled",
            "Vault": "Optional"
        }
    },
    "NVRAM": {
        "Add": {
            "7C436110-AB2A-4BBB-A880-FE41995C9F82": {
                "boot-args": boot_args,
                "prev-lang:kbd": "en-US:0"
            }
        }
    },
    "UEFI": {
        "APFS": {
            "MinDate": -1,
            "MinVersion": -1
        },
        "Quirks": {
            "UnblockFsConnect": False  # Chú ý cho HP
        }
    }
}


desktop4_5 = {
    "Kernel": {
        "Quirks": {
            "AppleCpuPmCfgLock": False,
            "AppleXcpmCfgLock": True,
            "DisableIoMapper": True,
            "LapicKernelPanic": False,  # Chú ý cho HP
            "PanicNoKextDump": True,
            "PowerTimeoutKernelPanic": True,
            "XhciPortLimit": False
        }
    },
    "Misc": {
        "Boot": {
            "HideAuxiliary": True
        },
        "Debug": {
            "AppleDebug": True,
            "ApplePanic": True,
            "DisableWatchDog": True,
            "Target": 67
        },
        "Security": {
            "AllowSetDefault": True,
            "BlacklistAppleUpdate": True,
            "ScanPolicy": 0,
            "SecureBootModel": "Disabled",
            "Vault": "Optional"
        }
    },
    "NVRAM": {
        "Add": {
            "7C436110-AB2A-4BBB-A880-FE41995C9F82": {
                "boot-args": boot_args,
                "prev-lang:kbd": "en-US:0"
            }
        }
    },
    "UEFI": {
        "APFS": {
            "MinDate": -1,
            "MinVersion": -1
        },
        "Quirks": {
            "IgnoreInvalidFlexRatio": True,
            "UnblockFsConnect": False  # Chú ý cho HP
        }
    }
}


desktop3 = {
     
    'ACPI': {
        # Bổ sung các cấu hình ACPI Delete nếu cần
        'Delete': [
            {
                'All': True,
                'Enabled': True,  # Cập nhật theo yêu cầu
                'Comment': 'Delete CpuPm',
                'OemTableId': b'CpuPm\x00\x00\x00',
                'TableLength': 0,
                'TableSignature': b'SSDT'
            },
            {
                'All': True,
                'Enabled': True,  # Cập nhật theo yêu cầu
                'Comment': 'Delete Cpu0Ist',
                'OemTableId': b'Cpu0Ist\x00',
                'TableLength': 0,
                'TableSignature': b'SSDT'
            }
        ]
    },

    "Kernel": {
        "Quirks": {
            "AppleCpuPmCfgLock": True,
            "DisableIoMapper": True,
            "LapicKernelPanic": False,  # Chú ý cho HP
            "PanicNoKextDump": True,
            "PowerTimeoutKernelPanic": True,
            "XhciPortLimit": False
        }
    },
    "Misc": {
        "Boot": {
            "HideAuxiliary": True
        },
        "Debug": {
            "AppleDebug": True,
            "ApplePanic": True,
            "DisableWatchDog": True,
            "Target": 67
        },
        "Security": {
            "AllowSetDefault": True,
            "BlacklistAppleUpdate": True,
            "ScanPolicy": 0,
            "SecureBootModel": "Disabled",
            "Vault": "Optional"
        }
    },
    "NVRAM": {
        "Add": {
            "7C436110-AB2A-4BBB-A880-FE41995C9F82": {
                "boot-args": boot_args,
                "prev-lang:kbd": "en-US:0"
            }
        }
    },
    "UEFI": {
        "APFS": {
            "MinDate": -1,
            "MinVersion": -1
        },
        "Quirks": {
            "IgnoreInvalidFlexRatio": True,
            "UnblockFsConnect": False  # Chú ý cho HP
        }
    }
}


desktop2 = {
    'ACPI': {
        # Bổ sung các cấu hình ACPI Delete nếu cần
        'Delete': [
            {
                'All': True,
                'Enabled': True,  # Cập nhật theo yêu cầu
                'Comment': 'Delete CpuPm',
                'OemTableId': b'CpuPm\x00\x00\x00',
                'TableLength': 0,
                'TableSignature': b'SSDT'
            },
            {
                'All': True,
                'Enabled': True,  # Cập nhật theo yêu cầu
                'Comment': 'Delete Cpu0Ist',
                'OemTableId': b'Cpu0Ist\x00',
                'TableLength': 0,
                'TableSignature': b'SSDT'
            }
        ]
    },
    
    "Kernel": {
        "Quirks": {
            "AppleCpuPmCfgLock": True,
            "DisableIoMapper": True,
            "LapicKernelPanic": False,
            "PanicNoKextDump": True,
            "PowerTimeoutKernelPanic": True,
            "XhciPortLimit": False
        }
    },
    "Misc": {
        "Boot": {
            "HideAuxiliary": True
        },
        "Debug": {
            "AppleDebug": True,
            "ApplePanic": True,
            "DisableWatchDog": True,
            "Target": 67
        },
        "Security": {
            "AllowSetDefault": True,
            "BlacklistAppleUpdate": True,
            "ScanPolicy": 0,
            "SecureBootModel": "Disabled",
            "Vault": "Optional"
        }
    },
    "NVRAM": {
        "Add": {
            "7C436110-AB2A-4BBB-A880-FE41995C9F82": {
                "boot-args": boot_args,
                "prev-lang:kbd": "en-US:0"
            }
        }
    },
    "UEFI": {
        "APFS": {
            "MinDate": -1,
            "MinVersion": -1
        },
        "Quirks": {
            "IgnoreInvalidFlexRatio": True,
            "UnblockFsConnect": False
        }
    }
}


GUIquirk = {
    'Misc': {
        'Boot': {
            'PickerMode': 'External',
            'PickerAttributes': 1,  # Thay đổi giá trị này thành 17 nếu muốn sử dụng chuột
            'PickerVariant': 'Acidanthera\GoldenGate'  # Hoặc chọn một trong các giá trị khác như Syrah, GoldenGate, hoặc Chardonnay
        }
    }
}

HPquirk = {
    'Kernel': {
        'Quirks': {
            'LapicKernelPanic': True
        }
    },
    'UEFI': {
        'Quirks': {
            'UnblockFsConnect': True
        }
    }
}

Dellquirk = {
    'Kernel': {
        'Quirks': {
            'CustomSMBIOSGuid': True
        }
    },
    'PlatformInfo': {
        'UpdateSMBIOSMode': 'Custom'
    }
}

laptop1 = {
        'Booter': {
            'Quirks': {
                'AvoidRuntimeDefrag': True,
                'EnableSafeModeSlide': True,
                'EnableWriteUnprotector': True,
                'ProvideCustomSlide': True,
                'RebuildAppleMemoryMap': True,
                'SetupVirtualMap': True
            }
        },
        'Kernel': {
            'Quirks': {
                'DisableIoMapper': True,
                'LapicKernelPanic': True,
                'PanicNoKextDump': True,
                'PowerTimeoutKernelPanic': True,
                'XhciPortLimit': True,
                'AppleCpuPmCfgLock': True
            }
        },
        'Misc': {
            'Boot': {
                'HideAuxiliary': True
            },
            'Debug': {
                'AppleDebug': True,
                'ApplePanic': True,
                'DisableWatchDog': True,
                'Target': 67
            },
            'Security': {
                'AllowSetDefault': True,
                'BlacklistAppleUpdate': True,
                'ScanPolicy': 0,
                'SecureBootModel': 'Disabled',
                'Vault': 'Optional'
            }
        },
        'NVRAM': {
            'Add': {
                '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                    'boot-args': boot_args,
                    'prev-lang:kbd': 'en-US:0'
                }
            },
            'WriteFlash': True
        },
        'UEFI': {
            'APFS': {
                'MinDate': -1,
                'MinVersion': -1
            },
            'Quirks': {
                'IgnoreInvalidFlexRatio': True,
                'UnblockFsConnect': True,
                'ReleaseUsbOwnership': True
            }
        }
    }
laptop2 = {
    'Kernel': {
        'Quirks': {
            'DisableIoMapper': True,
            'LapicKernelPanic': False,  # Chú ý với HP
            'PanicNoKextDump': True,
            'PowerTimeoutKernelPanic': True,
            'XhciPortLimit': False,
            'AppleCpuPmCfgLock': True
        }
    },
    'Misc': {
        'Boot': {
            'HideAuxiliary': True
        },
        'Debug': {
            'AppleDebug': True,
            'ApplePanic': True,
            'DisableWatchDog': True,
            'Target': 67
        },
        'Security': {
            'AllowSetDefault': True,
            'BlacklistAppleUpdate': True,
            'ScanPolicy': 0,
            'SecureBootModel': 'Disabled',
            'Vault': 'Optional'
        }
    },
    'NVRAM': {
        'Add': {
            '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                'boot-args': boot_args,
                'prev-lang:kbd': 'en-US:0'
            }
        },
        'WriteFlash': True
    },
    'UEFI': {
        'APFS': {
            'MinDate': -1,
            'MinVersion': -1
        },
        'Quirks': {
            'IgnoreInvalidFlexRatio': True,
            'UnblockFsConnect': False,  # Chú ý cho HP
            'ReleaseUsbOwnership': True
        }
    }
}
laptop3 = {
    'ACPI': {
        # Bổ sung các cấu hình ACPI Delete nếu cần
        'Delete': [
            {
                'All': True,
                'Enabled': True,  # Cập nhật theo yêu cầu
                'Comment': 'Delete CpuPm',
                'OemTableId': b'CpuPm\x00\x00\x00',
                'TableLength': 0,
                'TableSignature': b'SSDT'
            },
            {
                'All': True,
                'Enabled': True,  # Cập nhật theo yêu cầu
                'Comment': 'Delete Cpu0Ist',
                'OemTableId': b'Cpu0Ist\x00',
                'TableLength': 0,
                'TableSignature': b'SSDT'
            }
        ]
    },
    'Kernel': {
        'Quirks': {
            'DisableIoMapper': True,
            'LapicKernelPanic': False,  # Chú ý với HP
            'PanicNoKextDump': False,
            'PowerTimeoutKernelPanic': True,
            'XhciPortLimit': False,
            'AppleCpuPmCfgLock': True
        }
    },
    'Misc': {
        'Boot': {
            'HideAuxiliary': True
        },
        'Debug': {
            'AppleDebug': True,
            'ApplePanic': True,
            'DisableWatchDog': True,
            'Target': 67
        },
        'Security': {
            'AllowSetDefault': True,
            'BlacklistAppleUpdate': True,
            'ScanPolicy': 0,
            'SecureBootModel': 'Disabled',
            'Vault': 'Optional'
        }
    },
    'NVRAM': {
        'Add': {
            '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                'boot-args': boot_args,
                'prev-lang:kbd': 'en-US:0'
            }
        },
        'WriteFlash': True
    },
    'UEFI': {
        'APFS': {
            'MinDate': -1,
            'MinVersion': -1
        },
        'Quirks': {
            'IgnoreInvalidFlexRatio': True,
            'UnblockFsConnect': True,  # Chú ý cho HP
            'ReleaseUsbOwnership': True
        }
    }
}
laptop4 = {
    'Kernel': {
        'Quirks': {
            'DisableIoMapper': True,
            'LapicKernelPanic': False,  # Chú ý cho HP
            'PanicNoKextDump': True,
            'PowerTimeoutKernelPanic': True,
            'XhciPortLimit': False,
            'AppleCpuPmCfgLock': False,
            'AppleXcpmCfgLock': True
        }
    },
    'Misc': {
        'Boot': {
            'HideAuxiliary': True
        },
        'Debug': {
            'AppleDebug': True,
            'ApplePanic': True,
            'DisableWatchDog': True,
            'Target': 67
        },
        'Security': {
            'AllowSetDefault': True,
            'BlacklistAppleUpdate': True,
            'ScanPolicy': 0,
            'SecureBootModel': 'Disabled',
            'Vault': 'Optional'
        }
    },
    'NVRAM': {
        'Add': {
            '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                'boot-args': boot_args,
                'prev-lang:kbd': 'en-US:0'
            }
        },
        'WriteFlash': True
    },
    'UEFI': {
        'APFS': {
            'MinDate': -1,
            'MinVersion': -1
        },
        'Quirks': {
            'IgnoreInvalidFlexRatio': True,
            'UnblockFsConnect': False,  # Chú ý cho HP
            'ReleaseUsbOwnership': True
        }
    }
}
laptop5 = {
    'Kernel': {
        'Quirks': {
            'DisableIoMapper': True,
            'LapicKernelPanic': False,  # Chú ý cho HP
            'PanicNoKextDump': True,
            'PowerTimeoutKernelPanic': True,
            'XhciPortLimit': False,
            'AppleCpuPmCfgLock': False,
            'AppleXcpmCfgLock': True
        }
    },
    'Misc': {
        'Boot': {
            'HideAuxiliary': True
        },
        'Debug': {
            'AppleDebug': True,
            'ApplePanic': True,
            'DisableWatchDog': True,
            'Target': 67
        },
        'Security': {
            'AllowSetDefault': True,
            'BlacklistAppleUpdate': True,
            'ScanPolicy': 0,
            'SecureBootModel': 'Disabled',
            'Vault': 'Optional'
        }
    },
    'NVRAM': {
        'Add': {
            '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                'boot-args': boot_args,
                'prev-lang:kbd': 'en-US:0'
            }
        },
        'WriteFlash': True
    },
    'UEFI': {
        'APFS': {
            'MinDate': -1,
            'MinVersion': -1
        },
        'Quirks': {
            'IgnoreInvalidFlexRatio': True,
            'UnblockFsConnect': False,  # Chú ý cho HP
            'ReleaseUsbOwnership': True
        }
    }
}
laptop6 = {
    'Kernel': {
        'Quirks': {
            'DisableIoMapper': True,
            'LapicKernelPanic': False,  # Chú ý cho HP
            'PanicNoKextDump': True,
            'PowerTimeoutKernelPanic': True,
            'XhciPortLimit': False,
            'AppleCpuPmCfgLock': False,
            'AppleXcpmCfgLock': True
        }
    },
    'Misc': {
        'Boot': {
            'HideAuxiliary': True
        },
        'Debug': {
            'AppleDebug': True,
            'ApplePanic': True,
            'DisableWatchDog': True,
            'Target': 67
        },
        'Security': {
            'AllowSetDefault': True,
            'BlacklistAppleUpdate': True,
            'ScanPolicy': 0,
            'SecureBootModel': 'Disabled',
            'Vault': 'Optional'
        }
    },
    'NVRAM': {
        'Add': {
            '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                'boot-args': boot_args,
                'prev-lang:kbd': 'en-US:0'
            }
        },
        'WriteFlash': True
    },
    'UEFI': {
        'APFS': {
            'MinDate': -1,
            'MinVersion': -1
        },
        'Quirks': {
            'UnblockFsConnect': False,  # Chú ý cho HP
            'ReleaseUsbOwnership': True
        }
    }
}
laptop7 = {
    'Kernel': {
        'Quirks': {
            'DisableIoMapper': True,
            'LapicKernelPanic': False,  # Chú ý cho HP
            'PanicNoKextDump': True,
            'PowerTimeoutKernelPanic': True,
            'XhciPortLimit': False,
            'AppleCpuPmCfgLock': False,
            'AppleXcpmCfgLock': True
        }
    },
    'Misc': {
        'Boot': {
            'HideAuxiliary': True
        },
        'Debug': {
            'AppleDebug': True,
            'ApplePanic': True,
            'DisableWatchDog': True,
            'Target': 67
        },
        'Security': {
            'AllowSetDefault': True,
            'BlacklistAppleUpdate': True,
            'ScanPolicy': 0,
            'SecureBootModel': 'Disabled',
            'Vault': 'Optional'
        }
    },
    'NVRAM': {
        'Add': {
            '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                'boot-args': boot_args,
                'prev-lang:kbd': 'en-US:0'
            }
        },
        'WriteFlash': True
    },
    'UEFI': {
        'APFS': {
            'MinDate': -1,
            'MinVersion': -1
        },
        'Quirks': {
            'UnblockFsConnect': False,  # Chú ý cho HP
            'ReleaseUsbOwnership': True
        }
    }
}
laptop8 = {
    'Booter': {
        'Quirks': {
            'EnableWriteUnprotector': False,
            'ProtectMemoryRegions': True,
            'RebuildAppleMemoryMap': True,
            'SyncRuntimePermissions': True
        }
    },
    'Kernel': {
        'Quirks': {
            'DisableIoMapper': True,
            'LapicKernelPanic': False,  # Chú ý cho HP
            'PanicNoKextDump': True,
            'PowerTimeoutKernelPanic': True,
            'XhciPortLimit': False,
            'AppleCpuPmCfgLock': False,
            'AppleXcpmCfgLock': True
        }
    },
    'Misc': {
        'Boot': {
            'HideAuxiliary': True
        },
        'Debug': {
            'AppleDebug': True,
            'ApplePanic': True,
            'DisableWatchDog': True,
            'Target': 67
        },
        'Security': {
            'AllowSetDefault': True,
            'BlacklistAppleUpdate': True,
            'ScanPolicy': 0,
            'SecureBootModel': 'Disabled',
            'Vault': 'Optional'
        }
    },
    'NVRAM': {
        'Add': {
            '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                'boot-args': boot_args,
                'prev-lang:kbd': 'en-US:0'
            }
        },
        'WriteFlash': True
    },
    'UEFI': {
        'APFS': {
            'MinDate': -1,
            'MinVersion': -1
        },
        'Quirks': {
            'UnblockFsConnect': False,  # Cần cho HP
            'ReleaseUsbOwnership': True
        }
    }
}
laptop9 = {
    'Booter': {
        'Quirks': {
            'EnableWriteUnprotector': False,
            'ProtectMemoryRegions': True,
            'RebuildAppleMemoryMap': True,
            'SyncRuntimePermissions': True,
            'DevirtualiseMmio': True,
            'ProtectUefiServices': True
        }
    },
    'Kernel': {
        'Quirks': {
            'DisableIoMapper': True,
            'LapicKernelPanic': False,  # Chú ý cho HP
            'PanicNoKextDump': True,
            'PowerTimeoutKernelPanic': True,
            'XhciPortLimit': False,
            'AppleCpuPmCfgLock': False,
            'AppleXcpmCfgLock': True
        }
    },
    'Misc': {
        'Boot': {
            'HideAuxiliary': True
        },
        'Debug': {
            'AppleDebug': True,
            'ApplePanic': True,
            'DisableWatchDog': True,
            'Target': 67
        },
        'Security': {
            'AllowSetDefault': True,
            'BlacklistAppleUpdate': True,
            'ScanPolicy': 0,
            'SecureBootModel': 'Disabled',
            'Vault': 'Optional'
        }
    },
    'NVRAM': {
        'Add': {
            '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                'boot-args': boot_args,
                'prev-lang:kbd': 'en-US:0'
            }
        },
        'WriteFlash': True
    },
    'UEFI': {
        'APFS': {
            'MinDate': -1,
            'MinVersion': -1
        },
        'Quirks': {
            'UnblockFsConnect': False,  # Cần cho HP
            'ReleaseUsbOwnership': True
        }
    }
}
laptop10 = {
    'Booter': {
        'Quirks': {
            'EnableWriteUnprotector': False,
            'ProtectMemoryRegions': True,
            'RebuildAppleMemoryMap': True,
            'SyncRuntimePermissions': True,
            'DevirtualiseMmio': True,
            'ProtectUefiServices': True,
            'SetupVirtualMap': False
        }
    },
    'Kernel': {
        'Quirks': {
            'DisableIoMapper': True,
            'LapicKernelPanic': False,  # Chú ý cho HP
            'PanicNoKextDump': True,
            'PowerTimeoutKernelPanic': True,
            'XhciPortLimit': False,
            'AppleCpuPmCfgLock': False,
            'AppleXcpmCfgLock': True
        }
    },
    'Misc': {
        'Boot': {
            'HideAuxiliary': True
        },
        'Debug': {
            'AppleDebug': True,
            'ApplePanic': True,
            'DisableWatchDog': True,
            'Target': 67
        },
        'Security': {
            'AllowSetDefault': True,
            'BlacklistAppleUpdate': True,
            'ScanPolicy': 0,
            'SecureBootModel': 'Disabled',
            'Vault': 'Optional'
        }
    },
    'NVRAM': {
        'Add': {
            '7C436110-AB2A-4BBB-A880-FE41995C9F82': {
                'boot-args': boot_args,
                'prev-lang:kbd': 'en-US:0'
            }
        },
        'WriteFlash': True
    },
    'UEFI': {
        'APFS': {
            'MinDate': -1,
            'MinVersion': -1
        },
        'Quirks': {
            'UnblockFsConnect': False,  # Chú ý cho HP
            'ReleaseUsbOwnership': True
        }
    }
}
#hàm thực thi

def load_plist(filepath):
    try:
        with open(filepath, 'rb') as file:
            plist_data = plistlib.load(file)
        return plist_data
    except Exception as e:
        print(f"Error loading plist: {e}")
        return None

def update_plist_recursive(plist_data, changes, path=""):
    if isinstance(plist_data, dict):
        for key, subchanges in changes.items():
            if key in plist_data:
                if isinstance(subchanges, dict):
                    update_plist_recursive(plist_data[key], subchanges, path + key + " > ")
                else:
                    plist_data[key] = subchanges
                    print(f"Updated {key} at {path}")
            else:
                print(f"Key {key} not found at {path}. Ignoring.")
    elif isinstance(plist_data, list):
        for index, item in enumerate(plist_data):
            if isinstance(item, dict):
                update_plist_recursive(item, changes, path + f"Item {index} > ")

def save_plist(plist_data, filepath):
    try:
        with open(filepath, 'wb') as file:
            plistlib.dump(plist_data, file)
        print("Plist file saved successfully.")
    except Exception as e:
        print(f"Error saving plist: {e}")

def main(changes):
    plist_path = 'extra/X64/EFI/OC/Config.plist'  # Cập nhật đường dẫn này nếu cần
    # Định nghĩa các thay đổi ở đây
    plist_data = load_plist(plist_path)
    if plist_data:
        update_plist_recursive(plist_data, changes)
        save_plist(plist_data, plist_path)
    else:
        print("Không tải được tệp plist.")

        
