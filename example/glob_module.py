import glob

python_files = glob.glob("*.py")

for file_path in python_files:
    print(file_path)