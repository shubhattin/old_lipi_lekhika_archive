import os, shubhlipi as sh
from getpass import getpass

# 1 -> lekhika.py compile
# sign -> signing compiled file
# compile -> making setup and other archives
root = sh.env("sthAnam")
app_loc = "/saGgaNakAnuprayogaH"

if len(sh.argv) == 0:
    exit()
sign_key = ""
if "sign" in sh.argv or "compile" in sh.argv:
    sign_key = getpass("sign key = ")
for a in sh.argv:
    if a in "1":
        b1 = (
            lambda y, icon: f'pyinstaller.exe --noconfirm --onedir --window --icon "{root+app_loc}/src/resources/{icon}" "{root+app_loc}/src/{y}.py"'
        )
        dir1 = lambda y: f"kAraH/build/{y}/{y}.exe"
        i = int(a) - 1
        nm = ["lekhika"][i]
        b = b1(nm, ["Icon.ico"][i])
        dir = dir1(nm)
        sh.cmd(b, False)
        sh.delete_file(nm + ".spec")
        loca = f"{root+app_loc}/{dir}"
        to = f"{root}/bin/pc/{nm}.exe"
        sh.copy_file(loca, to)
        sh.delete_file(loca)
        if a == "1":
            sh.ver_info_add(
                to,
                sh.env("pc_ver"),
                "Lipi Lekhika",
                "Lipi Lekhika",
                "lipilekhika@gmail.com",
                "Lipi Lekhika",
            )
            sh.delete_folder(root + r"\bin\pc\resources")
            sh.copy_folder(
                root + app_loc + r"\src\resources", root + r"\bin\pc\resources"
            )
            for lc in ("display", "dattAMsh", "dattAMsh/table"):
                for x in os.listdir(f"{root+app_loc}/src/resources/{lc}"):
                    if ".json" in x:
                        sh.write(
                            f"{root}/bin/pc/resources/{lc}/{x}",
                            sh.minify_json(
                                sh.read(f"{root+app_loc}/src/resources/{lc}/{x}")
                            ),
                        )
    elif a == "sign":
        sh.sign_file(root + r"\bin\pc\lekhika.exe", sign_key)
        sh.cmd("pause", False)
        sh.cmd("cls", False)
    elif a == "compile":
        stp_loc = root + app_loc + r"\other_files\Setup Files\setup.iss"
        stp_dt = sh.read(stp_loc).split("\n")
        stp_dt[1] = f'#define MyAppVersion "{sh.env("pc_ver")}"'
        sh.write(stp_loc, "\n".join(stp_dt))
        cv = f'"{os.path.join(sh.tool,"compiler","ISCC.exe")}" "{stp_loc}"'
        sh.cmd(cv)
        sh.cmd("pause", False)
        sh.cmd("cls", False)

        # Making Lipi Lekhika Installer.zip
        zip = os.path.join(sh.tool, "7zip")
        pth = root + "/bin/Lipi Lekhika Installer.zip"
        sh.extract(pth, pth[:-4])
        sh.delete_file(pth)
        sh.delete_file(pth[:-4] + r"\files\Setup.exe")
        sh.copy_file(
            root + app_loc + "/other_files/Setup Files/Output/Setup.exe",
            pth[:-4] + r"/files\Setup.exe",
            True,
        )
        sh.delete_folder(root + app_loc + r"\other_files\Setup Files\Output")
        sh.sleep(1)
        sh.sign_file(pth[:-4] + r"\files\Setup.exe", sign_key)
        sh.sleep(1)
        sh.cmd(f'"{zip}/7za.exe" a -tzip "{pth}" "{pth[:-4]}/*" -y -mx9', file=True)
        sh.delete_folder(pth[:-4])

        # Making Lipi Lekhika Portable Archieve
        pth = root + "/bin/Lipi Lekhika Portable.exe"
        os.rename(root + r"\bin\pc", pth[:-4])
        sh.delete_file(pth)
        sh.cmd(
            f'"{zip}/7za.exe" a -t7z "{pth}" "{pth[:-4]}" -y -mx9 -sfx"{zip}/7z.sfx"',
            file=True,
        )
        sh.ver_info_add(
            pth,
            sh.env("pc_ver"),
            "Lipi Lekhika Portable",
            "Lipi Lekhika",
            "lipilekhika@gmail.com",
            "Lipi Lekhika",
        )
        os.rename(pth[:-4], root + r"\bin\pc")
        sh.sleep(1)
        sh.sign_file(pth, sign_key)
