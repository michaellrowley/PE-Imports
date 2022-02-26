# PE-Imports ![Language Shields tag](https://img.shields.io/badge/language-Python-blue)

## Usage
*This script requires [pefile](https://github.com/erocarrera/pefile) to be installed.*

``python3 imports.py /mnt/z/drivers /mnt/z/files/key-imports.txt /mnt/d/drivers/drv-output.txt``

The arguments that are passed into this script should be done so in the following order:

1. Path: A path to a directory or file that should be scanned.
2. Key Imports: A path to a file containing newline-terminated, glob-formatted strings that will be compared to import names in order to 'flag' them as interesting, for example; '``*DbgPrint*``' would match the commonly used functions '``DbgPrint``', '``DbgPrintEx``', '``vDbgPrintEx``', and '``vDbgPrintExWithPrefix``'.
3. Output file: The location where **all** imports will be logged.
4. Max recursion *(optional)*: The maximum 'depth' that the tool will enumerate files to/from.

## Notes
- Running this on Linux (or WSL) makes it much easier to do a wider-range of scanning across drivers as the root ``/mnt/`` path can be used to have the program enumerate imports from all drives but the tool is compatible with all operating-systems that pefile, Python, and the imports that were used are compatible with.

- The third argument ('output file') is used to store every import that the tool comes across so that searching the same file again with a different 'Key imports' list/parameter doesn't require a full re-analysis and the user can just manually look through the output file for their new criteria.

- This script currently only searches files with suffixes of ``'.sys'`` (as they must match the glob query ``*.sys``) - this is because my initial use for this script was for searching drivers for interesting imports. This can be changed by modifying [this](https://github.com/michaellrowley/PE-Imports/blob/ff33951d76c0ca0526b47d86cf331dcee41095c9/imports.py#L70) line to fit your search criteria (e.g '``*.dll``', '``*.exe``', or just remove the check completely)
