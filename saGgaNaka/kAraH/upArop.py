from time import sleep
from git import GIT_OK
import shubhlipi as sh
from getpass import getpass
import os
from dotenv import load_dotenv

load_dotenv()
# Refer https://docs.github.com/en/rest/reference/releases


root = sh.env("sthAnam")
GIT_KEY = os.getenv("GIT_KEY")
if not GIT_KEY:
    print("create a .env file with 'GIT_KET'")
    exit(-1)
try:
    GIT_KEY = sh.decrypt_text(GIT_KEY, getpass("key = "))
except:
    print("Wrong key!")
    exit(-1)
f = [
    {
        "file": root + r"\bin\Lipi Lekhika Installer.zip",
        "tag": "v" + sh.env("pc_ver"),
        "repo": "lipilekhika/saGgaNaka",
        "more": f'scp "{root}\\bin\\Lipi Lekhika Installer.zip" lipilekhika@frs.sourceforge.net:/home/frs/project/lipilekhika',
    },
    {
        "file": root + r"\bin\Lipi Lekhika Portable.exe",
        "tag": "v" + sh.env("pc_ver"),
        "repo": "lipilekhika/saGgaNaka",
    },
    {
        "file": root + r"\bin\Lipi Lekhika.apk",
        "tag": "v" + sh.env("android_ver"),
        "repo": "lipilekhika/jAlAnuprayog",
        "more": f'scp "{root}\\bin\\Lipi Lekhika.apk" lipilekhika@frs.sourceforge.net:/home/frs/project/lipilekhika',
    },
]

if sh.args(0) == "release":
    for x in sh.argv[1:]:
        try:
            d = f[int(x) - 1]
        except:
            exit()
        if "more" in d and "s" in sh.argv:
            print("Enter for Source Forge Upload of :-", d["file"].split("\\")[-1])
            sh.cmd(d["more"], file=True)
        sh.upload_release_file(d["file"], d["repo"], d["tag"], GIT_KEY)
elif sh.args(0) == "kAraH":
    tag = sh.argv[2]
    link = f[int(sh.argv[1]) - 1]["repo"]
    if input(f"do you want to create new release {tag} in {link}? ") != "astu":
        exit()
    sh.make_release_tag(link, tag, GIT_KEY)
elif sh.args(0) == "delete":
    tag = sh.argv[2]
    link = f[int(sh.argv[1]) - 1]["repo"]
    if input(f"do you want delete release {tag} from {link}? ") != "astu":
        exit()
    sh.delete_release_tag(link, tag, GIT_KEY)
elif sh.args(0) == "delete_kAraH":
    tag = sh.argv[2]
    link = f[int(sh.argv[1]) - 1]["repo"]
    if input(f"do you want delete release {tag} from {link}? ") != "astu":
        exit()
    sh.delete_release_tag(link, tag, GIT_KEY)
    sh.make_release_tag(link, tag, GIT_KEY)
elif sh.args(0) == "tracker":
    if input("Are you sure to update tracking files ? ") != "astu":
        exit()
    datt = {
        "jala": [".js", "application/javascript", 0, "जालस्थानस्य"],
        "ext": [".js", "application/javascript", 0, "अन्यानाम्"],
        "sang": [".txt", "text/plain", 0, "सङ्गणकस्य"],
        "sang_bhasha": [".txt", "text/plain", 1, "सङ्गणकभाषायाः"],
        "bhasha": [".js", "application/javascript", 1, "जालभाषायाः"],
    }
    lst = [["su"] + list(sh.script_list.values()), list(sh.lang_list.values())]
    link = "lipilekhika/dist"
    GIT_KEY

    def mk(x):
        v = datt[x]
        sh.delete_release_tag(link, x, GIT_KEY, log=False)
        sh.make_release_tag(link, x, GIT_KEY, log=False, name=v[3])
        sleep(1)
        th = []
        for y in lst[v[2]]:
            th.append(
                sh.start_thread(
                    lambda: sh.upload_release_file(
                        y + v[0],
                        link,
                        x,
                        GIT_KEY,
                        fl_type=v[1],
                        fl_data=" ",
                        log=False,
                    )
                )
            )
        for y in th:
            y.join()

    thrds = []
    tm = sh.time()
    for x in datt:
        thrds.append(sh.start_thread(lambda: mk(x)))
    for x in thrds:
        x.join()
    print("Added Tracking Files", sh.time() - tm)
