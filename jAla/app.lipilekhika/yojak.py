from copy import deepcopy
import os
import json, os, sys, shutil


def read(loc):
    f = open(loc, encoding="utf-8", mode="r+")
    v = f.read()
    f.close()
    return v


def delete_folder(loc):
    try:
        shutil.rmtree(loc)
    except:
        pass


if sys.argv[-1] == "build_cloud":
    for x in ["Jinja2"]:
        os.system(f"pip install {x}")
import jinja2

if sys.argv[-1] == "clear":
    LIST = read("./out/.gitignore").split("\n")
    for x in LIST:
        pth = f"./out/{x}"
        if os.path.isfile(pth):
            os.remove(pth)
        elif os.path.isdir(pth):
            shutil.rmtree(pth)
    exit()


def write(loc, val):
    f = open(loc, encoding="utf-8", mode="w+")
    f.write(val)
    f.close()


ln = json.loads(read("nirmana/ln.json"))


def render(fl, **o):
    return (
        jinja2.Environment(loader=jinja2.FileSystemLoader("nirmana/temp"))
        .get_template(fl)
        .render(**o)
    )


op = {"url": "https://app-lipilekhika.pages.dev", "lng_lst": list(ln.values())}

f = {
    "main": render("main.asp", name="", pRShTha="", **op),
    "lang": render("lang.asp", name="_lang", pRShTha="/{LANG}", **op),
    "convert": render("convert.asp", name="_convert", pRShTha="/{LANG1}/{LANG2}", **op),
    "parivartak": render(
        "convert.asp", name="_parivartak", pRShTha="/parivartak", **op
    ),
}
ln_f = {}


def devAdhirita_lipayaH(s):
    return s in (
        "Devanagari",
        "Hindi",
        "Nepali",
        "Marathi",
        "Konkani",
        "Sanskrit",
        "Purna-Devanagari",
    )


def st(link, tm=0, pr=0, o=False):
    if o:
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">{link}
</urlset>"""
    return f"""
    <url>
        <loc>{link}</loc>
        <changefreq>{["monthly","weekly"][tm]}</changefreq>
        <priority>{[0.7,1,0.5][pr]}</priority>
    </url>"""


def rd(fr, to, code=302, dp=True):
    v = f"\n{fr} {to} {code}"
    if dp and (fr != fr.lower() or to != to.lower()):
        v += f"\n{fr.lower()} {to.lower()} {code}"
    return v


def makedir(loc):
    try:
        os.makedirs(loc)
    except:
        pass


rdr = ""
ver = read("nirmana/ver.txt").split(",")
rdr += rd("/api/api", "https://codepen.io/shubhattin/pen/dyZoWBV", 301, False)
rdr += rd(
    "/android",
    f"https://github.com/lipilekhika/jAlAniuprayog/releases/download/v{ver[1]}/Lipi.Lekhika.apk",
    301,
    False,
)
rdr += rd(
    "/pc",
    f"https://github.com/lipilekhika/saGgaNaka/releases/download/v{ver[0]}/Lipi.Lekhika.Installer.zip",
    301,
    False,
)
rdr += rd(
    "/portable",
    f"https://github.com/lipilekhika/saGgaNaka/releases/download/v{ver[0]}/Lipi.Lekhika.Portable.exe",
    301,
    False,
)
rdr = rdr[1:]
for x in ln:
    ln_f[x] = json.loads(read(f"nirmana/data/{x}.json"))
lst = list(ln.keys())
lst.append("Main")
ln_f["Main"] = deepcopy(ln_f["English"])
ln_f["Main"]["replaces"]["lang_code"] = ""  # location code for directory
ln_f["Main"]["replaces"]["up_page"] = "https://lipilekhika.pages.dev"
# import dotenv

# dotenv.load_dotenv(".env.production")
G_AN_ID = os.getenv("GOOGLE_ANALYTICS_ID")
G_SR_ID = os.getenv("GOOGLE_SEARCH_ID")
GOOGLE_AN_TAG = ""
GOOGLE_SR_TAG = ""
if G_SR_ID:
    GOOGLE_SR_TAG = f'<meta name="google-site-verification" content="{G_SR_ID}" />'
if G_AN_ID:
    GOOGLE_AN_TAG = """
<script async src="https://www.googletagmanager.com/gtag/js?id={0}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());gtag('config', '{0}');
</script>""".replace(
        "{0}", G_AN_ID
    )
ln_f["Main"]["replaces"]["options"] = "{}"
rs = ""
for x in lst:  # for main
    l = deepcopy(ln_f[x])
    repl = l["replaces"]
    if G_AN_ID != "":
        repl["extras1"] = GOOGLE_AN_TAG
    if G_SR_ID != "" and x == "Main":
        repl["extras0"] = GOOGLE_SR_TAG
    fg = repl["lang_code"]
    rt = "./out/" + ((fg + "/") if x != "Main" else "")
    t = f["main"].format(**repl)
    if x != "Main":
        delete_folder(rt)
    else:
        delete_folder(rt + r'lang"')
        delete_folder(rt + r'converter"')
    makedir(rt)
    if fg != "en":
        rs += st(f"https://app-lipilekhika.pages.dev/{fg}", 1, 1)
    if fg == "en":
        t = t.replace('content="index">', 'content="noindex">')
    if fg == "":
        write(f"{rt}index.html", t)
    else:
        write(f"{rt[:-1]}.html", t)
for x in lst:  # for parivartak
    l = deepcopy(ln_f[x])
    repl = l["replaces"]
    if G_AN_ID != "":
        repl["extras1"] = GOOGLE_AN_TAG
    if True:
        v = repl["options"]
        v = v[:-1] + f'{"," if x!="Main" else ""}page:1' + "}"
        repl["options"] = v
    fg = repl["lang_code"]
    rt = "./out/" + ((fg + "/") if x != "Main" else "")
    t = f["parivartak"].format(**repl)
    if fg != "en":
        rs += st(
            f"https://app-lipilekhika.pages.dev/{fg+'/' if fg!='' else fg}parivartak",
            1,
            1,
        )
    if fg == "en":
        t = t.replace('content="index">', 'content="noindex">')
    write(f"{rt}parivartak.html", t)

write(f"./out/sitemap.xml", st(rs, o=True))
write(f"./out/_redirects", rdr)
r = ["/parivartak.html", "/index.html", "*__pycache__"]
for x in list(ln.values()):
    r.append("/" + x)
    r.append(f"/{x}.html")
write("./out/.gitignore", "\n".join(r))
if sys.argv[-1] == "build_cloud":
    os.remove("./out/.gitignore")
    print("SUCCESS -> BUILD -> LIPILEKHIKA")

exit(0)
for x in lst:  # for lang
    l = deepcopy(ln_f[x])
    fg = l["replaces"]["lang_code"]
    rt = "./out/" + ((fg + "/") if x != "Main" else "")
    # already deleted above folders
    makedir(f"{rt}lang")
    for sc in l["scripts"]:
        repl = {"LANG": sc}
        if sc == "Normal":
            continue
        for y in l["replaces"]:
            v = l["replaces"][y]
            if y == "up_page":
                v += f"/{fg}"
                if x == "Main":
                    v = "https://app-lipilekhika.pages.dev"
            elif y == "options":
                df = deepcopy(sc)
                if df == "Devanagari":
                    df = "Sanskrit"
                v = v[:-1] + f'{"," if x!="Main" else ""}main_lang:"{df}"' + "}"
            elif y == "title_lang":
                v = v.format(l["scripts"][sc])
            elif y == "description_lang":
                v = v.format(l["scripts"][sc])
            repl[y] = v
        t = f["lang"].format(**repl)
        if fg != "en":
            rs += st(
                f'https://app-lipilekhika.pages.dev{f"/{fg}" if x != "Main" else ""}/lang/{sc}',
                1,
                0,
            )
        if fg == "en":
            t = t.replace('content="index">', 'content="noindex">')
        write(f"{rt}lang/{sc}.html", t)
for x in lst:  # for convert
    l = deepcopy(ln_f[x])
    fg = l["replaces"]["lang_code"]
    rt = "./out/" + ((fg + "/") if x != "Main" else "")
    for sc in l["scripts"]:
        if sc == "Normal":
            continue
        makedir(f"{rt}converter/{sc}")
        for sz in l["scripts"]:
            if sz == sc:
                continue
            repl = {"LANG1": sc, "LANG2": sz}
            for y in l["replaces"]:
                v = l["replaces"][y]
                if y == "up_page":
                    v += f"/{fg}"
                    if x == "Main":
                        v = "https://app-lipilekhika.pages.dev"
                elif y == "options":
                    v = (
                        v[:-1]
                        + f'{"," if x!="Main" else ""}page:1,from:"{sc}",to:"{sz}"'
                        + "}"
                    )
                elif y == "title_convert":
                    v = v.format(l["scripts"][sc], l["scripts"][sz])
                elif y == "description_convert":
                    v = v.format(l["scripts"][sc], l["scripts"][sz])
                repl[y] = v
            t = f["convert"].format(**repl)
            if (
                fg != "en"
                and sz not in ("Urdu", "Normal")
                and sc != "Urdu"
                and not (devAdhirita_lipayaH(sz) and devAdhirita_lipayaH(sc))
            ):
                rs += st(
                    f'https://app-lipilekhika.pages.dev{f"/{fg}" if x != "Main" else ""}/converter/{sc}/{sz}',
                    1,
                    2,
                )
            if (
                fg == "en"
                or sz in ("Urdu", "Normal")
                or sc == "Urdu"
                or (devAdhirita_lipayaH(sz) and devAdhirita_lipayaH(sc))
            ):
                t = t.replace('content="index">', 'content="noindex">')
            write(f"{rt}converter/{sc}/{sz}.html", t)
