# findDuplicateFile
Simply find duplicate files
### Language [README.md](README.md) | [README_en-us.md](README_en-us.md)

[![Python](https://img.shields.io/badge/Python-3.7%2B-brightgreen.svg)](https://www.python.org)

1. Generate MD5 values of all files in the specified directory (including subdirectories)
2. Check these MD5 duplicates
3. Output the file path with the same MD5
4. Duplicate files are automatically moved to the recycle bin
## How to use
<kbd>Win+R</kbd>Run
```
pip install emoji
pip install send2trash
python3 find.py <folder> [-log <log_file> [level]]
# example:python3 find.py folder -log 1.log 40
```

## LICENSE
[MIT](LICENSE) 
