# deprecated

from time import sleep
import shubhlipi as sh, os, json
from getpass import getpass
import dotenv

link = ""
try:
    link = f'{sh.env("link")}/api'
except:
    pass
reg = sh.REG
loc = "HKCU\\SOFTWARE\\" + sh.to_base64("lipivars")
if sh.args(0) == "backup":
    for o in sh.argv[1:]:
        if o == "env":
            v = reg.read_key(loc).entries
            r = {}
            for rg in v:
                r[rg.name] = sh.from_base64(rg.value)
            rq = sh.post(
                link + "/env",
                json={
                    "key": getpass("key = "),
                    "reg": r,
                },
            )
            res = rq.json()
            print("BACKUP", "=>", res["detail"], rq.status_code)
    exit()
elif sh.args(0) == "setup":
    for o in sh.argv[1:]:
        if o == "env":
            if link == "":
                link = input("enter link:") + "/api"
            rq = sh.post(
                link + "/env",
                json={"key": getpass("key = ")},
            )
            res = rq.json()
            if rq.status_code != 200:
                print(res["detail"])
                exit()
            v = res
            try:
                reg.create_key(loc)
            except:
                pass
            for x in v:
                reg.write_entry(loc, x, sh.to_base64(v[x]))
            print("ADDED ENV VARIABLES")
        elif o == "deta":
            key = getpass("key = ")
            rq = sh.post(link + "/deta_auth", json={"key": key})
            res = rq.json()
            if rq.status_code == 200:
                sh.write(
                    sh.home() + r"\.deta\tokens",
                    sh.dump_json(dict(deta_access_token=res["value"])),
                )
            else:
                print(res["detail"])
            print("WROTE DETA AUTH KEYS")
    exit()
elif sh.args(0) == "logout":  # delete git keys from windows credential manager
    for o in sh.argv[1:]:
        if o == "deta":
            sh.delete_file(sh.home() + r"\.deta\tokens")
            print("DELETED deta tokens")
        elif o == "env":
            try:
                reg.delete_key(loc)
                print("DELTED env variables")
            except FileNotFoundError:
                print("env variable not found to delete")
        elif o[:3] == "win":
            for y in o[3:]:
                d = (
                    "git:https://github.com",
                    "vscodevscode.github-authentication/github.auth",
                )[int(y) - 1]
                sh.cmd(f"cmdkey /delete:{d}")
                print("Deleted ", d)
    exit()
elif sh.args(0) == "curl":
    url = input("enter url: ")
    rq = sh.post(link + "/" + url, json=dict(key=getpass("key = ")))
    res = rq.json()
    if rq.status_code == 200:
        sh.clip_copy(res["value"])
    else:
        print(res["detail"])
root = sh.env("sthAnam")
if sh.args(0) == "clone":
    d = (
        ("https://github.com/lipilekhika/saGgaNaka.git", "saGgaNakAnuprayogaH"),
        # 1
        ("https://github.com/lipilekhika/jAlAnuprayog", "jAlAnuprayogaH"),
        # 2
        ("https://github.com/lipilekhika/app.lipilekhika", "jAlasthAnam"),
        # 3
        ("https://github.com/lipilekhika/dist", "dist"),
        # 4
    )
    from git import Repo

    for x in sh.argv[1:]:
        f = d[int(x) - 1]
        to = root + f"\\{f[1]}"
        sh.makedir(to)
        print("started cloning", f[0])
        Repo.clone_from(f[0], to)
        print("done cloning of", f[0], "to", to)
        sleep(1)
    exit()
elif sh.args(0) == "avahar":
    for x in sh.argv[1:]:
        if x in "123":
            d = (
                ("https://app-lipilekhika.pages.dev/pc", "Lipi Lekhika Installer.zip"),
                # 1
                ("https://app-lipilekhika.pages.dev/portable", "Lipi Lekhika Portable.exe"),
                # 2
                ("https://app-lipilekhika.pages.dev/android", "Lipi Lekhika.apk"),
                # 3
            )[int(x) - 1]
            sh.makedir(root + "\\bin")
            to = root + "\\bin\\" + d[1]
            sh.download_file(d[0], to)
            print("Downloaded", d[1])
            if x == "2":
                sh.extract(to, root + "\\bin")
                sh.sleep(1)
                os.rename(to[:-4], root + "\\bin\\pc")
