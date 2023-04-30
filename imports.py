import pefile
import sys
import os
import fnmatch
import glob
import argparse

argument_parser = argparse.ArgumentParser(prog="PE-Imports", description="logs all of the imports of a given executable")

argument_parser.add_argument("basepath")
argument_parser.add_argument("-i", "--imports")
argument_parser.add_argument("-o", "--output")
argument_parser.add_argument("-d", "--delim")
argument_parser.add_argument("-s", "--strings")

arguments = argument_parser.parse_args()

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

key_imports = []
if arguments.imports is not None:
    with open(arguments.imports, 'r') as imports_file:
        key_imports = imports_file.read().replace("\r\n", '\n').split('\n')

output_file = None if arguments.output is None else open(arguments.output, 'w')

key_strings = []
if arguments.delim is not None and arguments.strings is not None:
    with open(arguments.delim, "rb") as delim_file:
        with open(arguments.strings, "rb") as strings_file:
            key_strings = strings_file.read().split(delim_file.read())

def log_imports(path):
    try:
        target_file = pefile.PE(path)
        path_imports = target_file.DIRECTORY_ENTRY_IMPORT
    except:
        return
    if output_file is not None:
        output_file.write(path + '\n')

    printed_path = False
    if len(key_imports) > 0:
        for import_module in path_imports:
            module_name = import_module.dll.decode()
            for function_import in import_module.imports:
                
                to_log = '\t' + module_name + '!' \
                    + catchStr(function_import.name) + '/' \
                    + catchStr(function_import.ordinal)

                if output_file is not None:
                    output_file.write(to_log + '\n')

                if function_import.name is not None:
                    for key_import in key_imports:
                        if fnmatch.fnmatch(function_import.name.decode(), key_import):
                            if not printed_path:
                                print("\n" + path + " (Imports):")
                                printed_path = True
                            print(to_log)

    if len(key_strings) > 0:
        had_printed_path = printed_path
        printed_path = False
        with open(path, "rb") as opened_path:
            raw_data = opened_path.read()
            for key_string in key_strings:
                if key_string in raw_data:
                    if not printed_path:
                        print(("" if had_printed_path else "\n") + path + " (Bytes):")
                        printed_path = True
                    print("\t" + key_string.hex())

for file in glob.glob(arguments.basepath + "/**/*.sys", recursive=True):
    log_imports(file)

print('\n')
