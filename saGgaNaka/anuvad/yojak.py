import shubhlipi as sh, yaml

ln = sh.lang_list
root = sh.env("sthAnam")
anuvad = {}
for x in ln:
    anuvad[x] = yaml.safe_load(sh.read(f"lang\\{x}.yaml"))
    data = sh.dump_json(anuvad[x])
    sh.write(
        f"{root}\\saGgaNakAnuprayogaH\\src\\resources\\display\\{x}.json",
        data,
    )
