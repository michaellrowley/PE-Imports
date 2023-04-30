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

## Notes
- Running this on Linux (or WSL) makes it much easier to do a wider-range of scanning across drivers as the root ``/mnt/`` path can be used to have the program enumerate imports from all drives (allowing for a more generic scanning process) but the tool is compatible with all operating-systems that support PEFile and Python 3.

- The ``output`` argument/file is used to store every import that the tool comes across so that searching the same file again with a different 'Key imports' list/parameter doesn't require a full re-analysis and so that the user can just manually look through the output file for their new criteria without spending time re-scanning entire files.

- This script currently only searches files with suffixes of ``'.sys'`` (as they must match the glob query ``*.sys``) - this is because my initial use for this script was for searching drivers for interesting imports. The required extension query can be changed by modifying the script to fit your search criteria (e.g '``*.dll``', '``*.exe``', or just remove the check completely)
