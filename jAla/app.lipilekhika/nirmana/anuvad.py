from time import time
import shubhlipi as sh, json

ln = sh.lang_list
ln2 = sh.dict_rev(ln)

if sh.args(0) in ln2:
    src = sh.args(0)
else:
    src = "en"
if input(f"Do you want to translate with {src} as base? ") != "yes":
    exit()
main_db = json.loads(sh.read(f"lang\\{ln2[src]}.json"))
anu = {}
only = {
    "yes": {
        "replaces": {"description": -1, "description_lang": -1, "descripton_convrt": -1}
    },
    "no": {},
}
for y in ln:
    if ln[y] == "en":
        continue
    tm = time()
    anu[y] = {}
    org = json.loads(sh.read(f"lang/{y}.json"))
    if ln[y] != "ur":
        anu[y] = sh.process_json(
            main_db,
            org,
            src,
            ln[y],
            no=only["no"],
            yes=only["yes"],
            only_org=ln[y] in ("sa", "hi"),
        )
    else:
        anu[y] = sh.process_json(
            anu["हिन्दी"],
            org,
            "Hindi",
            "Urdu",
            no=only["no"],
            yes=only["yes"],
            func=sh.parivartak,
        )
    sh.write(
        f"lang\\{y}.json",
        json.dumps(anu[y], ensure_ascii=False, sort_keys=False, indent=4),
    )
    print(ln[y], f"{time()-tm}s")
if True:
    import bring
