import pefile
import sys
import os
import fnmatch
import glob

def catchStr(data):
    # 'data' is expected to be a string.
    if data is None:
        return 'null'
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode()
    else:
        # if isinstance(data, int)):
        return str(data)

try:
    target_path = sys.argv[1]
    key_imports = open(sys.argv[2], 'r').read().split('\n')
    output_file = open(sys.argv[3], 'w')
except:
    print('imports.py binary_dir/ key-imports.txt output-log.txt')
    exit()

def log_imports(path):
    try:
        target_file = pefile.PE(path)
        path_imports = target_file.DIRECTORY_ENTRY_IMPORT
    except:
        return
    output_file.write(path + '\n')
    printed_path = False
    for import_module in target_file.DIRECTORY_ENTRY_IMPORT:
        module_name = import_module.dll.decode()
        for function_import in import_module.imports:
            to_log = '\t' + module_name + '!' \
                + catchStr(function_import.name) + '/' \
                + catchStr(function_import.ordinal)
            output_file.write(to_log + '\n')
            if function_import.name is not None:
                for key_import in key_imports:
                    if not printed_path:
                        print(path)
                        printed_path = True
                    if fnmatch.fnmatch(function_import.name.decode(),
                            key_import):
                        print(to_log)

for file in glob.glob(target_path + "/**/*.sys", recursive=True):
    log_imports(file)
