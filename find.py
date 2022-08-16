import hashlib
import logging
import os
import sys
import logging
import emoji
import send2trash
logger = logging.getLogger("FINDPY")
logger.setLevel(logging.INFO)
logger1 = logging.StreamHandler()
logger1.setLevel(logging.INFO)
fomatter = logging.Formatter('%(asctime)s:%(message)s')
logger1.setFormatter(fomatter)
logger.addHandler(logger1)
if len(sys.argv) < 2:
    print('Usage:find.py <folder> [-log <log_file> [level]]')
    print('level:{INFO=20,ERROR=40}')
    sys.exit(-1)
if len(sys.argv) == 4:
    logger2 = logging.FileHandler(sys.argv[3])
    logger2.setLevel(logging.INFO)
    logger2.setFormatter(fomatter)
    logger.addHandler(logger2)
if len(sys.argv) == 5:
    logger2 = logging.FileHandler(sys.argv[3])
    logger2.setLevel(int(sys.argv[4]))
    logger2.setFormatter(fomatter)
    logger.addHandler(logger2)
rootFolder = sys.argv[1]
rootFolder+='\\'
temp = {}
duplicateList = {}


def getMD5List(folder):
    files = os.listdir(folder)
    if len(files) == 0:
        return False
    for file in files:
        filePath = '%s%s' % (folder, file)

        if os.path.isdir(filePath):
            getMD5List('%s\\' % filePath)
        else:
            oFile = open(filePath, 'rb')
            value = hashlib.md5()
            value.update(oFile.read())
            oFile.close()
            temp.update({filePath: value.hexdigest()})


def findDuplicateFile(md5List):
    for md5 in md5List:
        try:
            duplicateList[md5List[md5]].append(md5)
        except:
            duplicateList.update({md5List[md5]: [md5]})
            pass


def showDuplicateFile(duplicateArray):
    count = 0
    for one in duplicateArray:
        if len(duplicateArray[one]) > 1:
            count = count + 1
            for two in duplicateArray[one]:
                keep=duplicateArray[one][0]
                if keep!=two:
                    try:
                        send2trash.send2trash(two)
                    except Exception as e:
                        logger.error(e)
                        logger.error(emoji.demojize('[Failed to delete]'+two))
                    else:
                        logger.info(emoji.demojize('[deleted]'+two))
                    continue
                else:
                    logger.info(emoji.demojize(two))
                    deld=False
    logger.info('总共找到 %s 组文件重复。' % count)


getMD5List(rootFolder)
findDuplicateFile(temp)
showDuplicateFile(duplicateList)
