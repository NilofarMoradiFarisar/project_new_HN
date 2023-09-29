from pathlib import Path
from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("Hamid").rglob("*.*"):
#         zip.write(path)

# zip = ZipFile("files.zip", "w")
# for path in Path("Hamid").rglob("*.*"):
#     zip.write(path)
# zip.close()


with ZipFile("files.zip") as zip:
    print(zip.namelist()[0])
    info = zip.getinfo(zip.namelist()[0])
    print(info)
    print(info.file_size)
    print(info.compress_size)

with ZipFile("files.zip") as zip:
    zip.extractall("extracted")
