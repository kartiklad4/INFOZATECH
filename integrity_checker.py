import hashlib
import os
import json

def get_file_hash(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

# We will monitor a single test file on your phone
target_file = "test.txt"
baseline_db = "baseline.json"

if not os.path.exists(target_file):
    with open(target_file, "w") as f:
        f.write("Initial secure content.")

current_hash = get_file_hash(target_file)

# Menu selector
choice = input("1. Save Baseline Snapshot\n2. Re-scan & Check Integrity\nChoose option (1 or 2): ")

if choice == "1":
    snapshot = {target_file: current_hash}
    with open(baseline_db, "w") as f:
        json.dump(snapshot, f)
    print("Baseline snapshot saved securely!")

elif choice == "2":
    if not os.path.exists(baseline_db):
        print("Error: No baseline found. Run Option 1 first.")
    else:
        with open(baseline_db, "r") as f:
            snapshot = json.load(f)
        
        saved_hash = snapshot.get(target_file)
        if current_hash is None:
            print(f"ALERT: {target_file} has been DELETED!")
        elif saved_hash == current_hash:
            print(f"SUCCESS: {target_file} is safe. No modifications detected.")
        else:
            print(f"ALERT: {target_file} has been MODIFIED or corrupted!")
