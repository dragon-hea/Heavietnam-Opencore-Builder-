import plistlib

# Define the path to your plist file
plist_file_path = 'extra/X64/EFI/OC/Config.plist'

OSItoXOSI = {
    'Comment': 'Change _OSI to XOSI',
    'Enabled': True,
    'Count': 0,
    'Limit': 0,
    'Find': bytes.fromhex('5f4f5349'),
    'Replace': bytes.fromhex('584f5349')
}
ADBGtoXDBG = {
        'Comment': 'ADBG to XDBG',
        'Enabled': True,
        'Count': 1,
        'Limit': 0,
        'Find': bytes.fromhex('4303141941444247'),
        'Replace': bytes.fromhex('4303141958444247'),
        'OemTableId': bytes.fromhex('475357417070'),
        'TableSignature': bytes.fromhex('53534454'),
        'TableLength': 0,
        'Skip': 0
    }
BRT6toXBRT6 = {
    'Comment': 'Change BRT6 to XBRT6',
    'Enabled': True,
    'Find': bytes.fromhex('4252543602A00B93'),
    'Replace': bytes.fromhex('5852543602A00B93')
}
OSIDtoXSID = {
    'Comment': 'Change OSID to XSID',
    'Enabled': True,
    'Find': bytes.fromhex('4F534944'),
    'Replace': bytes.fromhex('58534944')
}
PNLFtoXNLF = {
    'Comment': 'Change PNLF to XNLF',
    'Enabled': True,
    'Find': bytes.fromhex('504E4C46'),
    'Replace': bytes.fromhex('584E4C46')
}

GPRWtoXPRW = {
    'Base':'',
    'BaseSkip':0,
    'Comment': 'Change GPRW to XPRW',
    'Count': 0,
    'Enabled': True,
    'Find': bytes.fromhex('4750525702'),  # Hexadecimal representation for "GPRW"
    'Limit': 0,
    'Mask': bytes(),
    'OemTableId': bytes(),
    'Replace': bytes.fromhex('5850525702'),  # Hexadecimal representation for "XPRW"
    'ReplaceMask': bytes(),
    'Skip': 0,
    'TableLength': 0,
    'TableSignature': bytes()
}
# Function to load the existing plist data
def load_existing_plist(filepath):
    with open(filepath, 'rb') as file:
        plist_data = plistlib.load(file)
    return plist_data

# Function to save updates to the plist file
def save_updated_plist(data, filepath):
    with open(filepath, 'wb') as file:
        plistlib.dump(data, file)

# Function to add an ACPI patch in the plist, under the correct section
def add_acpi_patch_properly(plist_data, patch):
    if 'ACPI' not in plist_data:
        plist_data['ACPI'] = {'Patch': []}
    if 'Patch' not in plist_data['ACPI']:
        plist_data['ACPI']['Patch'] = []
        
    plist_data['ACPI']['Patch'].append(patch)
    print("ACPI patch has been properly added.")

def main(ACPIpatch):
    # Load the existing plist data
    plist_data = load_existing_plist(plist_file_path)
    # Adding the new ACPI patch to the existing plist data
    add_acpi_patch_properly(plist_data, ACPIpatch)
    # Save the updated plist data back to the file
    save_updated_plist(plist_data, plist_file_path)
