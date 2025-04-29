import shubhlipi as sh

root = sh.env("sthAnam")
app_loc = "\\jAlAnuprayogaH\\nirmana"
ln = sh.lang_list
ln_f = {}
for x in ln:
    ln_f[x] = sh.load_json(sh.read(f"lang\\{x}.json"))
    c = sh.load_json(sh.read(f"{root}\\jAlAnuprayogaH\\src\\src\\display\\{x}.json"))
    c1 = c["scripts"]
    c2 = c["others"]
    del c1["Vedic"]
    repl = ln_f[x]["replaces"]
    repl["ln_code"] = repl["lang_code"]
    ln_f[x]["scripts"] = c1
    repl["up_page"] = "https://app-lipilekhika.pages.dev"
    repl["title_lang"] = c2["title_lang"]
    repl["title"] = c2["page_title"]
    repl["title_parivartak"] = c2["title_convert"].replace("{0} - ", "")
    repl["title_convert"] = c2["title_convert"].format(c2["from"])
    repl["description_parivartak"] = repl["description_convert"].replace(" {0}.", ".")
    repl["description_convert"] = repl["description_convert"].format(c2["from"])
    sh.write(f"data\\{x}.json", sh.dump_json(ln_f[x]))
sh.write("ver.txt", f'{sh.env("pc_ver")},{sh.env("android_ver")}')

sh.write(f"ln.json", sh.dump_json(ln))
