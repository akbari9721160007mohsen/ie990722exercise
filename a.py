import codecs
import os, shutil

folder = './'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


BLOCKSIZE = 1048576 

with codecs.open('main.txt', "r", "utf-8") as sourceFile:
    with codecs.open('src/utf8.txt', "w", "utf-8") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)

with codecs.open('main.txt', "r", "utf-8") as sourceFile:
    with codecs.open('src/ucs2le.txt', "w", "utf-16-le") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)

with codecs.open('main.txt', "r", "utf-8") as sourceFile:
    with codecs.open('src/ucs2be.txt', "w", "utf-16-be") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)

with codecs.open('main.txt', "r", "utf-8") as sourceFile:
    with codecs.open('src/ucs4le.txt', "w", "utf-32-le") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)


with codecs.open('main.txt', "r", "utf-8") as sourceFile:
    with codecs.open('src/ucs4be.txt', "w", "utf-32-be") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)

# with codecs.open('main.txt', "r", "utf-8") as sourceFile:
#     with codecs.open('src/cp1256.txt', "w", "cp1256") as targetFile:
#         while True:
#             contents = sourceFile.read(BLOCKSIZE)
#             if not contents:
#                 break
#             targetFile.write(contents)
