# diskspace
Making it possible to use Linux df &amp; du command on Windows/Linux.

# Requirements
Python 3.6 or up

# Install
```
pip install diskspace
```

# Usage
```
$ ds|diskspace --help
usage:  [--help] [-v] [-e EXCLUDE [EXCLUDE ...]] [-o ONLY [ONLY ...]] [-h]
        [-nf] [-ns]

Making it possible to use Linux df & du command on Windows

optional arguments:
  --help                Show this help message and exit.
  -v, --version         Show the version number and exit
  -e EXCLUDE [EXCLUDE ...], --exclude EXCLUDE [EXCLUDE ...]
                        Exclude name or file extensions matching arguments
  -o ONLY [ONLY ...], --only ONLY [ONLY ...]
                        Only include name or file extensions matching
                        arguments
  -h, --human           Convert bytes in to readable format
  -nf, --nofolders      Ingore folders
  -ns, --nostats        Don't display disk space at top
```

# Usage in code example
```py
>>> import diskspace
>>> show_dir = diskspace.ShowPath("./Desktop")
>>> print(show_dir.all_files)
# [<FileInfo name=Adios.png bytes=267391 human=261.1KiB folder=False created=1571303626.1382277>, <FileInfo name=Baby yoda flip pancakes.jpg bytes=47487 human=46.4KiB folder=False created=1574946741.9886782>, <FileInfo name=big sipp.jpg bytes=47076 human=46.0KiB folder=False created=1574028168.9891481>]
```

### ShowPath()
- path: str = Path to find files (Default: ".")
- exclude: str = Exclude files (Default: None)
- include_folder = Include folders in result (Default: True)
- human: bool = Show disk space in human-readable value (Default: False)
- include_stats: bool = Include stats of current disk in ShowPath.pretty_print (Default: True)
- whitelist: str = Only include X files (Default: None)
