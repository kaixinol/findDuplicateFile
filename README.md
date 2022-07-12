# findDuplicateFile
简单查找重复文件
### Language [README.md](README.md) | [README_en-us.md](README_en-us.md)

[![Python](https://img.shields.io/badge/Python-3.7%2B-brightgreen.svg)](https://www.python.org)

1. 生成指定目录（含子目录）中所有文件的 MD5 值

2. 对这些 MD5 查重

3. 输出具有相同 MD5 的文件路径

4. 自动移到回收站

## 使用方法
<kbd>Win+R</kbd>运行
```
pip install emoji
pip install send2trash
python3 find.py <folder> [-log <log_file> [level]]
# example:python3 find.py folder -log 1.log 40
```

## 开源协议
[MIT](LICENSE) 

