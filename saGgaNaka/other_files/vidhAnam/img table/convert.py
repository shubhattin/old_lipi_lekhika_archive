"""
python -m pip install pywin32
python pywin32_postinstall.py -install
Try to first run this in adminstrative mode
"""
from PIL import ImageGrab
import win32com.client as win32
from os import listdir, makedirs as mk_dir
import shubhlipi as sh

excel = win32.gencache.EnsureDispatch("Excel.Application")
root = sh.env("sthAnam")
pc = r"\saGgaNakAnuprayogaH"
web1 = r"\jAlAnuprayogaH\src"
web2 = r"\jAlasthAnam"
lst = listdir("./")
if len(sh.argv) > 0:
    lst1 = []
    for x in sh.argv:
        if x + ".xlsx" in lst:
            lst1.append(x + ".xlsx")
    lst = lst1
for x in lst:
    if x[:2] == "~$" or x[-5:] != ".xlsx":
        continue
    lng = x[:-5]
    workbook = excel.Workbooks.Open(
        f"{root+pc}\\other_files\\vidhAnam\\img table\\{lng}.xlsx"
    )
    for sheet in workbook.Worksheets:
        for i, shape in enumerate(sheet.Shapes):
            if shape.Name.startswith("Picture"):  # or try 'Image'
                shape.Copy()
                image = ImageGrab.grabclipboard()
                for y in (
                    pc + r"\src\resources\img\lang",
                    web1 + r"\img\lang",
                    web2 + r"\img\lang",
                ):
                    try:
                        mk_dir(root + y)
                    except:
                        pass
                    # cropping image
                    sz = image.size
                    im = image.crop((0, 0, sz[0], sz[1] - 3))
                    im.save(f"{root+y}\\{lng}.png", "PNG")
                    if lng == "Sanskrit":
                        for t in ["Hindi", "Marathi", "Konkani", "Nepali"]:
                            im.save(f"{root+y}\\{t}.png", "PNG")
    workbook.Close(True)
    print(lng + " done")
    # Close any Excel Process from Task manager
