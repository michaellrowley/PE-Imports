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
- ``extension``: The extension (excluding leading dot) of files to be searched (default: 'sys').

# Example Output

```
A:/Windows/System32/sioctl.sys
	ntoskrnl.exe!RtlInitUnicodeString/null @ 0x00402000
	ntoskrnl.exe!ProbeForRead/null @ 0x00402004
	ntoskrnl.exe!MmProbeAndLockPages/null @ 0x00402008
	ntoskrnl.exe!MmUnlockPages/null @ 0x0040200C
	ntoskrnl.exe!MmMapLockedPagesSpecifyCache/null @ 0x00402010
	ntoskrnl.exe!IoAllocateMdl/null @ 0x00402014
	ntoskrnl.exe!IofCompleteRequest/null @ 0x00402018
	ntoskrnl.exe!IoCreateDevice/null @ 0x0040201C
	ntoskrnl.exe!IoCreateSymbolicLink/null @ 0x00402020
	ntoskrnl.exe!IoDeleteDevice/null @ 0x00402024
	ntoskrnl.exe!IoDeleteSymbolicLink/null @ 0x00402028
	ntoskrnl.exe!IoFreeMdl/null @ 0x0040202C
	ntoskrnl.exe!memcpy/null @ 0x00402030
	ntoskrnl.exe!RtlUnwind/null @ 0x00402034
B:/Windows/System32/netio.sys
	ntoskrnl.exe!ExRegisterCallback/null @ 0x0005E000
	ntoskrnl.exe!ObfDereferenceObject/null @ 0x0005E008
	ntoskrnl.exe!ExCreateCallback/null @ 0x0005E010
	ntoskrnl.exe!RtlStringFromGUID/null @ 0x0005E018
	ntoskrnl.exe!ZwQueryValueKey/null @ 0x0005E020
	ntoskrnl.exe!ZwClose/null @ 0x0005E028
	ntoskrnl.exe!ZwOpenKey/null @ 0x0005E030
	ntoskrnl.exe!MmUnmapLockedPages/null @ 0x0005E038
	ntoskrnl.exe!MmAllocatePagesForMdlEx/null @ 0x0005E040
	... *snip* ...
	msrpc.sys!NdrMesTypeDecode3/null @ 0x0005E608
	msrpc.sys!MesHandleFree/null @ 0x0005E610
	msrpc.sys!MesDecodeBufferHandleCreate/null @ 0x0005E618
	msrpc.sys!RpcExceptionFilter/null @ 0x0005E620
C:/Windows/System32/WinAccel.sys
	ntoskrnl.exe!KeInitializeDpc/null @ 0x1C000B018
	ntoskrnl.exe!ZwDeviceIoControlFile/null @ 0x1C000B020
	ntoskrnl.exe!ZwCreateFile/null @ 0x1C000B028
	ntoskrnl.exe!IoGetRelatedDeviceObject/null @ 0x1C000B030
	ntoskrnl.exe!ObfDereferenceObject/null @ 0x1C000B038
	ntoskrnl.exe!RtlFreeUnicodeString/null @ 0x1C000B040
	ntoskrnl.exe!RtlInitUnicodeString/null @ 0x1C000B048
	ntoskrnl.exe!ExQueueWorkItem/null @ 0x1C000B050
	ntoskrnl.exe!ExWaitForRundownProtectionRelease/null @ 0x1C000B058
...
```

> Feel free to use [this](https://gchq.github.io/CyberChef/#recipe=Comment('Be%20sure%20to%20add%20a%20%5C'Find%20/%20Replace%5C'%20*between*%20regexes')Regular_expression('User%20defined','%5E%5B%5C%5C/%5C%5Cw%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*%5C%5Cs%2Bntoskrnl%5C%5C.exe!IoCreateDevice%5B%5C%5C/%5C%5C@%5C%5Cs%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*',true,true,false,false,false,false,'List%20matches')Regular_expression('User%20defined','%5E%5B%5C%5C/%5C%5Cw%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*%5C%5Cs%2Bntoskrnl%5C%5C.exe!IoCreateSymbolicLink%5B%5C%5C/%5C%5C@%5C%5Cs%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*',true,true,false,false,false,false,'List%20matches')Regular_expression('User%20defined','%5E%5B%5C%5C/%5C%5Cw%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*%5C%5Cs%2Bntoskrnl%5C%5C.exe!IofCompleteRequest%5B%5C%5C/%5C%5C@%5C%5Cs%5D%5B%5E%5C%5Cn%5D%2B%5C%5Cn(%5C%5Cs%2B%5B%5E%5C%5Cn%5D%2B%5C%5Cn)*',true,true,false,false,false,false,'List%20matches')) CyberChef query to list drivers which import ``IoCreateDevice``, ``IoCreateSymbolicLink``, ``ZwMapViewOfSection``, and ``IofCompleteRequest`` via postprocessing (using an output/``-o`` file).

> Additionally, ``^[\/\w][^\n]+\n(\s+[^\n]+\n){0,5}(?=[^\s])`` may be used as a regular expression to identify  drivers with less than a five imports, common signal of obfuscation/packing.

## Tips
- Running this on Linux (or WSL) makes it much easier to do a wider-range of scanning across drivers as the root ``/mnt/`` path can be used to have the program enumerate imports from all drives (allowing for a more generic scanning process) but the tool is compatible with all operating-systems that support PEFile and Python 3.

- Following the above point, a well-[configured](https://github.com/qilingframework/qiling/blob/master/examples/scripts/dllscollector.bat) Qiling [rootfs](https://github.com/qilingframework/rootfs) can be an adequate starting point for becoming accustomed to the tool.

- The ``output`` argument/file is used to store every import that the tool comes across so that searching the same file again with a different 'Key imports' list/parameter doesn't require a full re-analysis and so that the user can just manually look through the output file for their new criteria without spending time re-scanning entire files.
