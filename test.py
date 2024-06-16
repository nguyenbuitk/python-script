import os
import shutil

# Define base directory
base_dir = '/mnt/data/extracted_files/example/'

# Define the new structure
structure = {
    "data_processing": ["load_json.py"],
    "data_processing/pandas": [
        "pandas_series.py",
        "pandas_readcsv.ipynb",
        "pandas_dataframe.ipynb",
        "pandas_readjson.py",
        "data.csv",
        "data.json"
    ],
    "web_scraping": ["download_image.py", "send_request_to_healthchecks.py"],
    "automation": ["zip_function.py", "encode-utf8.py", "logger.py"],
    "utilities": [
        "webbrowser_module.py",
        "working_with_file.py",
        "streamlit.py",
        "syspath.py",
        "try_except.py",
        "classmethod.py",
        "staticmethod.py",
        "thread.py",
        "list_comprehensive.py"
    ],
    "examples": [
        "argparser.py", "argparser_1.py", "argparser_2.py", "readJSON.py",
        "response_example.py", "test.py", "fpdf_multicell.py", "squeeze.ipynb",
        "strip_function.py", "compare_tuple.py", "compare_dict.py", "compare_list.py",
        "check_ssl_expiry_online.py", "ssl_example.py", "match_syntax.py",
        "list_index.py", "sorted_file_names.py", "check_cert_expires.py"
    ],
    "modular": ["bonus14.py"],
    "modular/modular": ["converter.py", "parser.py"],
    "modular/modular/__pycache__": ["parser.cpython-312.pyc", "converter.cpython-312.pyc"],
    "create_api": ["main.py"],
    "create_api/templates": ["home.html"],
    "documents": ["README.md", "questions.json", "todo_list.txt", "pandas/README.md"],
    "images": ["astronomy.jpg"]
}

# Create directories and move files
for folder, files in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(base_dir, file)
        if os.path.exists(file_path):
            shutil.move(file_path, folder_path)

print("Files organized successfully.")

