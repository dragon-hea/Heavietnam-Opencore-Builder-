import inquirer
import os
import json  # Import the json module

def check():
    def collect_user_input():
        print("Chào mừng bạn đến với khảo sát Hackintosh!")
        survey_results = {
            'CPU Generation': 'None',
            'Device Type': 'None',
            'Laptop Brand': 'None',
            'Has DGPU': 'None',
            'DGPU Brand': 'None',
            'AMD GPU Type': 'None',
            'Has IGPU': 'None',
            'IGPU Model': 'None',
            'Drive Type': 'None',
            'Drive Model': 'None',
            'Has WiFi Card': 'None',
            'WiFi Card Brand': 'None',
            'WiFi Card Model': 'None',
            'macOS Version': 'None',
            'Has Trackpad': 'None',
            'Trackpad Type': 'None',
            'Trackpad Model': 'None',
            'Has LAN Card': 'None',
            'LAN Card Brand': 'None',
            'LAN Card Model': 'None',
            'OpenCore version': 'None'
        }
        
        cpu_generations = [
            "Clarksfield and Arrandale", "Nehalem", "Sandy Bridge", "Ivy Bridge", "Haswell",
            "Broadwell", "Skylake", "Kaby Lake", "Coffee Lake",
            "Comet Lake", "Ice Lake", "Tiger Lake", "Alder Lake", "Raptor Lake", "Rocket Lake"
        ]
        
        questions = [
            inquirer.List('cpu', message="Chọn thế hệ CPU của bạn:", choices=cpu_generations),
        ]
        answers = inquirer.prompt(questions)
        cpu_generation = answers['cpu']
        survey_results['CPU Generation'] = cpu_generation

        device_types = ["NUC", "Laptop", "Desktop"]
        device_type = inquirer.list_input("Thiết bị của bạn là loại nào?", choices=device_types)
        survey_results['Device Type'] = device_type
        
        if device_type == "Laptop":
            laptop_brands = ["Dell", "HP", "Asus", "other"]
            laptop_brand = inquirer.list_input("Thương hiệu laptop của bạn là gì?", choices=laptop_brands)
            survey_results['Laptop Brand'] = laptop_brand

        has_dgpu = inquirer.confirm("Bạn có dGPU không?")
        survey_results['Has DGPU'] = 'Yes' if has_dgpu else 'No'

        # Phần thay đổi bắt đầu từ đây
        dgpu_brand = None  # Định nghĩa biến dgpu_brand với giá trị None

        if has_dgpu and device_type == "Desktop":
            gpu_brands = ["AMD", "NVIDIA"]
            dgpu_brand = inquirer.list_input("GPU của bạn là của AMD hay NVIDIA?", choices=gpu_brands)
            survey_results['DGPU Brand'] = dgpu_brand
            if dgpu_brand == "AMD":
                amd_options = ["Navi(10, 21, 22, 23)", "Vega(20,10)", "Polaris(20,10)", "R7-R9", "HD (7x-8x)", "other"]
                amd_choice = inquirer.list_input("Chọn dòng GPU AMD của bạn:", choices=amd_options)
                survey_results['AMD GPU Type'] = amd_choice
        # Kết thúc phần thay đổi

        has_igpu = False  # Định nghĩa biến has_igpu với giá trị False

        # Phần thay đổi bắt đầu từ đây
        if (device_type == 'Desktop' and (dgpu_brand != 'AMD' or dgpu_brand is None)) or (device_type != 'Desktop'):
            has_igpu = inquirer.confirm("CPU của bạn có IGPU không?")
            survey_results['Has IGPU'] = 'Yes' if has_igpu else 'No'
            if has_igpu:
                igpu_options = {
                    "Ivy Bridge": {"Laptop": ["1366 x 768", "1600 x 900", "EDP"]},
                    "Haswell": {
                        "Laptop": ["HD 5x", "HD 4x"],
                        "Desktop": ["HD 4400", "other"]
                    },
                    "Broadwell": {"Laptop": ["HD 5600", "other"]},
                    "Skylake": {
                        "Laptop": ["HD (515-550), P350", "HD 510"],
                        "NUC": ["HD 515", "HD (520-530)", "HD (540-550)", "HD 580"],
                        "Desktop": ["HD P350", 'other']
                    },
                    "Kaby Lake": {
                        "Laptop": ["HD(615-650)", "UHD 620"],
                        "NUC": ["HD 615", "HD 630", "HD (640-650)", "UHD 620"]
                    },
                    "Coffee Lake": {
                        "Laptop": ["UHD 620", "UHD 630"],
                        "NUC": ["UHD (620-630)", "UHD (655)"]
                    },
                    "Comet Lake": {
                        "Laptop": ["UHD 620", "UHD 630"],
                        "NUC": ["UHD (620-630)", "UHD (655)"]
                    },
                    "Ice Lake": {
                        "Laptop": ["G4, G7", "UHD G1"]
                    }
                }
                igpu_choices = igpu_options.get(cpu_generation, {}).get(device_type, ["Có thể bỏ qua"])
                if igpu_choices:
                    igpu_model = inquirer.list_input("Chọn thông số IGPU của bạn:", choices=igpu_choices)
                    survey_results['IGPU Model'] = igpu_model
        # Kết thúc phần thay đổi

        drive_options = [
            "512 GB GIGABYTE M.2 PCIe SSD (VD GP-GSM2NE8512GNTD)", "ADATA Swordfish 2 TB M.2-2280",
            "SK Hynix HFS001TD9TNG-L5B0B", "SK Hynix P31", "PC601/PC611/PC711/BC501",
            "Samsung PM961/PM981/PM981a/PM991", "Samsung 983ZET", "Micron 2200V MTFDHBA512TCK",
            "Micron 2200S", "Intel 600P/660P/760P", "Kingston A2000", "Asgard AN3+ (STAR1000P)",
            "Netac NVME SSD 480", "Kingmax NVME SSD", "other"
        ]
        drive_model = inquirer.list_input("Chọn mô hình ổ cứng của bạn:", choices=drive_options)
        survey_results['Drive Model'] = drive_model

        drive_types = ["NVMe", "SATA"]
        drive_type = inquirer.list_input("Ổ cứng của bạn là loại nào?", choices=drive_types)
        survey_results['Drive Type'] = drive_type

        has_wifi = inquirer.confirm("Bạn có card WiFi không?")
        survey_results['Has WiFi Card'] = 'Yes' if has_wifi else 'No'
        wifi_card_brand = None  # Định nghĩa biến wifi_card_brand với giá trị None

        if has_wifi:
            wifi_brands = ["Intel", "Broadcom", "Atheros", "other"]
            wifi_card_brand = inquirer.list_input("Hãng card WiFi của bạn là gì?", choices=wifi_brands)
            survey_results['WiFi Card Brand'] = wifi_card_brand
        if wifi_card_brand == "Intel":
            intel_models = ["AxXXX", "other"]
            intel_model = inquirer.list_input("Mô hình card Intel của bạn là gì?", choices=intel_models)
            survey_results['WiFi Card Model'] = intel_model

        has_lan = inquirer.confirm("Bạn có card LAN không?")
        survey_results['Has LAN Card'] = 'Yes' if has_lan else 'No'
        if has_lan:
            lan_brands = ["Intel", "Atheros", "Realtek"]
            lan_brand = inquirer.list_input("Thương hiệu card LAN của bạn là gì?", choices=lan_brands)
            survey_results['LAN Card Brand'] = lan_brand
            if lan_brand == "Intel":
                intel_models = ["I211 NICs", "Intel's 82578, 82579, I217, I218 and I219 NICs", "I225-V", "Intel I350 1Gb NIC"]
                intel_model = inquirer.list_input("Mô hình card LAN Intel của bạn là gì?", choices=intel_models)
                survey_results['LAN Card Model'] = intel_model
            elif lan_brand == "Atheros":
                atheros_models = ["Atheros Killer E2500", "other"]
                atheros_model = inquirer.list_input("Mô hình card LAN Atheros của bạn là gì?", choices=atheros_models)
                survey_results['LAN Card Model'] = atheros_model
            elif lan_brand == "Realtek":
                realtek_models = ["Realtek's 2.5Gb Ethernet", "other"]
                realtek_model = inquirer.list_input("Mô hình card LAN Realtek của bạn là gì?", choices=realtek_models)
                survey_results['LAN Card Model'] = realtek_model
        
        if device_type == 'Laptop' or device_type == 'NUC':
            all_macos_versions = ['Mojave', 'Catalina', 'Big Sur', 'Monterey', 'Ventura', 'Sonoma14.4','Sonoma14.0']
            macos_versions = {
                'Ivy Bridge': ['Mojave', 'Catalina', 'Big Sur', 'Monterey', 'Ventura'],
                'Haswell': ['Mojave', 'Catalina', 'Big Sur', 'Monterey', 'Ventura'],
                'Broadwell': ['Mojave', 'Catalina', 'Big Sur', 'Monterey', 'Ventura'],
                'Skylake': ['Mojave', 'Catalina', 'Big Sur', 'Monterey', 'Ventura'],
                'Kaby Lake': ['Mojave', 'Catalina', 'Big Sur', 'Monterey', 'Ventura'],
                'Sandy Bridge': ['Mojave', 'Catalina'],
                'Coffee Lake': all_macos_versions,
                'Comet Lake': all_macos_versions,
                'Ice Lake': ['Catalina', 'Big Sur', 'Monterey', 'Ventura', 'Sonoma14.4','Sonoma14.0'],
                'Tiger Lake': ['Catalina', 'Big Sur', 'Monterey', 'Ventura', 'Sonoma14.4','Sonoma14.0'],
                'Alder Lake': ['Catalina', 'Big Sur', 'Monterey', 'Ventura', 'Sonoma14.4','Sonoma14.0'],
                'Raptor Lake': ['Catalina', 'Big Sur', 'Monterey', 'Ventura', 'Sonoma14.4','Sonoma14.0'],
                'Clarksfield and Arrandale': [],
                'Nehalem': []
            }
            if macos_versions[cpu_generation]:
                macos_choice = inquirer.list_input('Bạn muốn cài đặt phiên bản macOS nào?', choices=macos_versions[cpu_generation])
                print(f'Bạn đã chọn cài đặt macOS {macos_choice} trên CPU {cpu_generation}.')
            else:
                print(f'Thế hệ CPU {cpu_generation} không tương thích với các phiên bản macOS nào.')
        else:
            macos_versions = ['Mojave', 'Catalina', 'Big Sur', 'Monterey', 'Ventura', 'Sonoma14.4','Sonoma14.0']
            macos_choice = inquirer.list_input('Bạn muốn cài đặt phiên bản macOS nào?', choices=macos_versions)
            print(f'Bạn đã chọn cài đặt macOS {macos_choice} trên CPU {cpu_generation}.')
        
        survey_results['macOS Version'] = macos_choice

        if device_type == 'Laptop' or device_type == 'NUC':
            has_trackpad = inquirer.confirm("Bạn có trackpad không?")
            survey_results['Has Trackpad'] = 'Yes' if has_trackpad else 'No'
            if has_trackpad:
                trackpad_types = ["i2c", "ps2", "other"]
                trackpad_type = inquirer.list_input("Giao thức trackpad của bạn là gì?", choices=trackpad_types)
                survey_results['Trackpad Type'] = trackpad_type
                if trackpad_type == "i2c":
                    i2c_trackpad_types = ["HID", "Synaptics", "FTE", "ELAN", "AtmelMXT", "other"]
                    i2c_trackpad_model = inquirer.list_input("Loại trackpad I2C của bạn là gì?", choices=i2c_trackpad_types)
                    survey_results['Trackpad Model'] = i2c_trackpad_model

        OC_versions = [
            "OpenCore standard", "Opencore NO ACPI" 
        ]
        
        questions = [
            inquirer.List('Opencore', message="Chọn version OpenCore của bạn:", choices=OC_versions),
        ]
        answers = inquirer.prompt(questions)
        OC_version = answers['Opencore']
        survey_results['OpenCore version'] = OC_version


        return survey_results

    def main():
        user_data = collect_user_input()
        if user_data:  # Check if user_data is not empty
            # Save results to a JSON file
            with open('hackintosh_survey_results.json', 'w') as file:
                json.dump(user_data, file, indent=4)  # Dump the data with indentation for better readability

        print("Cảm ơn bạn đã tham gia khảo sát!")

    if __name__ == "__main__":
        main()
        os.system('cls')  # Clears the screen.

check()
