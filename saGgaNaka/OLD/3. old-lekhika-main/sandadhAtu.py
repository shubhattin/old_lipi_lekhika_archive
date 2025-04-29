from os import system, remove
from sys import argv

root = r"D:\Softwares\Z"
args = argv
full = args[-1]
a = full[0]
ex = [False, False]
if len(full) > 1:
    if full[1] == "1":
        ex[0] = True
if len(full) > 2:
    if full[2] == "1":
        ex[1] = True
dir = ""
if a == "1":
    b = 'pyinstaller --noconfirm --onedir --window --icon "assets/Icon.ico" lekhika.py'
    dir = r"\LipiLekhika\build\lekhika\lekhika.exe"
elif a == "2":  # or console
    b = 'pyinstaller --noconfirm --onedir --window --icon "assets/favicon.ico" samanya.py'
    dir = r"\LipiLekhika\build\samanya\samanya.exe"
system(b)
if a == "1":
    remove("lekhika.spec")
elif a == "2":
    remove("samanya.spec")
system("pause")
system("cls")
a1 = root + dir
system('xcopy "' + a1 + '" "' + root + r'\lekhika-bin"')
if ex[0]:
    system('"kAraH\signer.py" ' + a)
if ex[1]:
    cv = '"D:\Softwares\Z\LipiLekhika\other_files\Setup Files\compiler\ISCC.exe" "D:\Softwares\Z\LipiLekhika\other_files\Setup Files\setup.iss"'
    file = open("compile.cmd", "w")
    file.write(cv)
    file.close()
    system("compile.cmd")
    remove("compile.cmd")
    system("pause")
    system("cls")
    system(
        r'xcopy "D:\Softwares\Z\LipiLekhika\other_files\Setup Files\Output\Lipi Lekhika Setup.exe" "D:\Softwares\Z\lipilekhika.github.io"'
    )
    system(r'"kAraH\signer.py" 4')