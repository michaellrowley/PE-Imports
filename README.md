# PE-Imports ![Language Shields tag](https://img.shields.io/badge/language-Python-blue)

## Usage
*This script requires that the [pefile](https://github.com/erocarrera/pefile) library is installed.*

``python3 imports.py [-h] [-i IMPORTS] [-o OUTPUT] [-d DELIM] [-s STRINGS] basepath``

The arguments that are passed into this script should be done so in the following order:

- ``imports``: The path to a newline-separated file of strings that represent imports to be flagged.
- ``output``: The path to a file where a complete log of all imports should be written.
- ``delim``: The path to a file whose contents are the delimiter for the file referenced by the ``strings`` argument.
- ``strings``: The path to a ``delim``-separated file of bytes that should be flagged if located.
- ``basepath``: The path to a file or directory which should be recursively scanned.

# Example Output

> [This](https://gchq.github.io/CyberChef/#recipe=Comment('Be%20sure%20to%20add%20a%20%5C'Find%20/%20Replace%5C'%20*between*%20regexes')Regular_expression('User%20defined','%5E%5B%5C%5C/%5C%5Cw%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*%5C%5Cs%2Bntoskrnl%5C%5C.exe!IoCreateDevice(/null)?%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*',true,true,false,false,false,false,'List%20matches')Find_/_Replace(%7B'option':'Regex','string':'%5C%5Cn%5C%5Cn'%7D,'%5C%5Cn',true,false,true,false)Regular_expression('User%20defined','%5E%5B%5C%5C/%5C%5Cw%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*%5C%5Cs%2Bntoskrnl%5C%5C.exe!ZwMapViewOfSection(/null)?%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*',true,true,false,false,false,false,'List%20matches')Find_/_Replace(%7B'option':'Regex','string':'%5C%5Cn%5C%5Cn'%7D,'%5C%5Cn',true,false,true,false)Regular_expression('User%20defined','%5E%5B%5C%5C/%5C%5Cw%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*%5C%5Cs%2Bntoskrnl%5C%5C.exe!IoCreateSymbolicLink(/null)?%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*',true,true,false,false,false,false,'List%20matches')Find_/_Replace(%7B'option':'Regex','string':'%5C%5Cn%5C%5Cn'%7D,'%5C%5Cn',true,false,true,false)Regular_expression('User%20defined','%5E%5B%5C%5C/%5C%5Cw%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*%5C%5Cs%2Bntoskrnl%5C%5C.exe!IofCompleteRequest(/null)?%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*',true,true,false,false,false,false,'List%20matches')&ienc=65001) CyberChef query is compatible with the output format of what ``imports.py`` prints to the console or what it logs to the ``-o`` output location. By default, it lists drivers which import ``IoCreateDevice``, ``IoCreateSymbolicLink``, ``ZwMapViewOfSection``, and ``IofCompleteRequest`` to demonstrate the matching patterns' non-mutually exclusive nature. This pattern is good for retrospective processing (using the large ``-o`` file) or narrowing down a search field from listings in stdout.

```
drivers/SgrmAgent.sys:
        ntoskrnl.exe!MmMapLockedPagesSpecifyCache/null
        ntoskrnl.exe!ZwQueryInformationFile/null
        ntoskrnl.exe!ZwMapViewOfSection/null
        ntoskrnl.exe!MmMapIoSpaceEx/null
        ntoskrnl.exe!ZwOpenFile/null
        ntoskrnl.exe!ZwQueryVirtualMemory/null
        ntoskrnl.exe!IoCreateDevice/null
drivers/storport.sys:
        ntoskrnl.exe!ZwMapViewOfSection/null
        ntoskrnl.exe!MmMapLockedPagesSpecifyCache/null
        ntoskrnl.exe!IoCreateDevice/null
        ntoskrnl.exe!MmMapIoSpaceEx/null
        ntoskrnl.exe!MmMapIoSpace/null
drivers/vhdmp.sys:
        ntoskrnl.exe!MmMapLockedPagesSpecifyCache/null
        ntoskrnl.exe!MmMapLockedPagesWithReservedMapping/null
        ntoskrnl.exe!ZwSetInformationFile/null
        ntoskrnl.exe!ZwReadFile/null
        ntoskrnl.exe!ZwMapViewOfSection/null
        ntoskrnl.exe!IoCreateDevice/null
        ntoskrnl.exe!ZwOpenFile/null
...
```

## Tips
- Running this on Linux (or WSL) makes it much easier to do a wider-range of scanning across drivers as the root ``/mnt/`` path can be used to have the program enumerate imports from all drives (allowing for a more generic scanning process) but the tool is compatible with all operating-systems that support PEFile and Python 3.

- The ``output`` argument/file is used to store every import that the tool comes across so that searching the same file again with a different 'Key imports' list/parameter doesn't require a full re-analysis and so that the user can just manually look through the output file for their new criteria without spending time re-scanning entire files.

- This script currently only searches files with suffixes of ``'.sys'`` (as they must match the glob query ``*.sys``) - this is because my initial use for this script was for searching drivers for interesting imports. The required extension query can be changed by modifying the script to fit your search criteria (e.g '``*.dll``', '``*.exe``', or just remove the check completely)
