import subprocess

def run_oc_snapshot_automatically():
    snapshot_path = 'extra/OCSnapshot/OCSnapshot.py'
    input_file = 'extra/X64/EFI/OC/Config.plist'
    oc_folder = 'extra/X64/EFI/OC'
    
    command = ['python', snapshot_path, '-i', input_file, '-s', oc_folder, '-v', 'latest']
    
    print("Running command:", ' '.join(command))
    try:
        process = subprocess.run(command, capture_output=True, text=True, check=True)
        print("STDOUT:", process.stdout)
    except subprocess.CalledProcessError as e:
        print("ERROR:", e.stderr)
    except Exception as e:
        print("EXCEPTION:", str(e))
def main():
    run_oc_snapshot_automatically()
