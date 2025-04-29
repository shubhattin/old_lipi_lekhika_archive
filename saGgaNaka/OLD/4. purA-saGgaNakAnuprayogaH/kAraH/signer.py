from os import remove, system
from sys import argv

mode = -1
s = r'"D:\Softwares\Z\saGgaNakAnuprayogaH\other_files\Certificate\signtool.exe"'
cert = r'"D:\Softwares\Z\saGgaNakAnuprayogaH\other_files\Certificate\Certificate_key.pfx"'
file = (
    r'"D:\Softwares\Z\lekhika-bin\lekhika.exe"',
    r'"D:\Softwares\Z\lekhika-bin\samanya.exe"',
    r'"D:\Softwares\Z\saGgaNakAnuprayogaH\other_files\Setup Files\Output\setup.exe"',
    r'"D:\Softwares\Z\#\Setup.exe"',
    r'"D:\Softwares\Z\#\Lipi Lekhika Portable.exe"'
)
ex = False
if len(argv) > 1:
    ex = True
while mode != 0:
    if not ex:
        mode = int(input("mode="))
        p = input("gUDhashabdam=")
    else:
        mode = int(argv[-1])
        p = "hariom123"
    c = (
        s
        + " sign /tr http://timestamp.digicert.com /td sha256 /fd sha256 /f "
        + cert
        + " /p "
        + p
        + " "
        + file[mode - 1]
    )
    file = open("sign.cmd", "w")
    file.write(c)
    file.close()
    system("sign.cmd")
    remove("sign.cmd")
    system("pause")
    system("cls")
    if ex:
        mode = 0
