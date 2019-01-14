# diskspace
Making it possible to use Linux df &amp; du command on Windows

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
