from json import load, dumps
from pyperclip import copy
from copy import deepcopy

file = open(r"mukhya.json", mode="r", encoding="utf-8")
a = load(file)
a["Assamese"] = deepcopy(a["Bengali"])
a["Assamese"]["w"]["w"][0] = "ৱ"
a["Assamese"]["v"]["v"][0] = "ৱ"
a["Assamese"]["r"]["r"][0] = "ৰ"
a["Normal"] = {}
a["Sanskrit"] = a["Hindi"]
b = a["Sanskrit"]
b["#"] = {}
b["#"]["#"] = ["#", "as0123456789'MukrvpnH", 2]
b["#"]["#a"] = ["꣪", "n", 2]
b["#"]["#an"] = ["॒", "", 2]
b["#"]["#s"] = ["॑", "s", 2]
b["#"]["#ss"] = ["᳚", "s", 2]
b["#"]["#sss"] = ["᳛", "", 2]
b["#"]["#0"] = ["꣠", "", 2]
b["#"]["#1"] = ["꣡", "", 2]
b["#"]["#2"] = ["꣢", "", 2]
b["#"]["#3"] = ["꣣", "", 2]
b["#"]["#4"] = ["꣤", "", 2]
b["#"]["#5"] = ["꣥", "", 2]
b["#"]["#6"] = ["꣦", "", 2]
b["#"]["#7"] = ["꣧", "", 2]
b["#"]["#8"] = ["꣨", "", 2]
b["#"]["#9"] = ["꣩", "", 2]
b["#"]["#'"] = ["꣱", "", 2]
b["#"]["#M"] = ["ꣳ", "1", 2]
b["#"]["#M1"] = ["ꣲ", "1", 2]
b["#"]["#u"] = ["꣫", "", 2]
b["#"]["#k"] = ["꣬", "", 2]
b["#"]["#n"] = ["꣭", "", 2]
b["#"]["#p"] = ["꣮", "", 2]
b["#"]["#r"] = ["꣯", "", 2]
b["#"]["#v"] = ["꣰", "", 2]
b["#"]["#H"] = ["ᳵ", "1", 2]
b["#"]["#H1"] = ["ᳶ", "", 2]
mAtrA = {
    "Sanskrit": {
        "a": "",
        "A": "ा",
        "i": "ि",
        "auU": "ॉ",
        "aiI": "ॅ",
        "I": "ी",
        "e": "े",
        "ai": "ै",
        "o": "ो",
        "au": "ौ",
        "RR": "ॄ",
        "R": "ृ",
        "u": "ु",
        "U": "ू",
        "LRR": "ॣ",
        "LR": "ॢ",
    },
    "Sinhala": {
        "a": "",
        "A": "ා",
        "i": "ි",
        "aiI": "ැ",
        "auU": "ෑ",
        "I": "ී",
        "u": "ු",
        "U": "ූ",
        "e": "ෙ",
        "ai": "ෛ",
        "E": "ේ",
        "o": "ො",
        "au": "ෞ",
        "au1": "ෞ",
        "o1": "ො",
        "O": "ෝ",
        "O2": "ෝ",
        "O1": "ෝ",
        "RR": "ෲ",
        "R": "ෘ",
        "LRR": "ෳ",
        "LR": "ෟ",
    },
    "Telugu": {
        "a": "",
        "A": "ా",
        "i": "ి",
        "I": "ీ",
        "u": "ు",
        "U": "ూ",
        "e": "ె",
        "ai": "ై",
        "ai1": "ై",
        "E": "ే",
        "o": "ొ",
        "au": "ౌ",
        "O": "ో",
        "RR": "ౄ",
        "R": "ృ",
        "LRR": "ౣ",
        "LR": "ౢ",
    },
    "Tamil": {
        "a": "",
        "A": "ா",
        "i": "ி",
        "I": "ீ",
        "e": "ெ",
        "au": "ௌ",
        "au1": "ௌ",
        "E": "ே",
        "o": "ொ",
        "o1": "ொ",
        "ai": "ை",
        "O": "ோ",
        "O1": "ோ",
        "u": "ு",
        "U": "ூ",
    },
    "Malayalam": {
        "a": "",
        "A": "ാ",
        "i": "ി",
        "I": "ീ",
        "u": "ു",
        "U": "ൂ",
        "e": "െ",
        "ai": "ൈ",
        "E": "േ",
        "o": "ൊ",
        "o1": "ൊ",
        "au": "ൗ",
        "O": "ോ",
        "O1": "ോ",
        "au1": "ൌ",  # alternative of au
        "RR": "ൄ",
        "R": "ൃ",
        "LRR": "ൣ",
        "LR": "ൢ",
    },
    "Oriya": {
        "a": "",
        "A": "ା",
        "i": "ି",
        "I": "ୀ",
        "u": "ୁ",
        "U": "ୂ",
        "e": "େ",
        "ai": "ୈ",
        "ai1": "ୈ",
        "o": "ୋ",
        "o1": "ୋ",
        "au": "ୌ",
        "au1": "ୌ",
        "RR": "ୄ",
        "R": "ୃ",
        "LRR": "ୣ",
        "LR": "ୢ",
    },
    "Kannada": {
        "a": "",
        "A": "ಾ",
        "i": "ಿ",
        "I1": "ೀ",
        "I": "ೀ",
        "u": "ು",
        "U": "ೂ",
        "e": "ೆ",
        "ai": "ೈ",
        "ai1": "ೈ",
        "E": "ೇ",
        "E1": "ೇ",
        "o": "ೊ",
        "o1": "ೊ",
        "au": "ೌ",
        "O": "ೋ",
        "O1": "ೋ",
        "O2": "ೋ",
        "RR": "ೄ",
        "R": "ೃ",
        "LRR": "ೣ",
        "LR": "ೢ",
    },
    "Bengali": {
        "a": "",
        "A": "া",
        "i": "ি",
        "I": "ী",
        "u": "ু",
        "U": "ূ",
        "e": "ে",
        "ai": "ৈ",
        "o": "ো",
        "o1": "ো",
        "au": "ৌ",
        "au1": "ৌ",
        "RR": "ৄ",
        "R": "ৃ",
        "LRR": "ৣ",
        "LR": "ৢ",
    },
    "Gujarati": {
        "a": "",
        "A": "ા",
        "i": "િ",
        "I": "ી",
        "u": "ુ",
        "U": "ૂ",
        "e": "ે",
        "ai": "ૈ",
        "aiI": "ૅ",
        "auU": "ૉ",
        "o": "ો",
        "au": "ૌ",
        "RR": "ૄ",
        "R": "ૃ",
        "LRR": "ૣ",
        "LR": "ૢ",
    },
    "Punjabi": {
        "a": "",
        "A": "ਾ",
        "i": "ਿ",
        "I": "ੀ",
        "u": "ੁ",
        "U": "ੂ",
        "e": "ੇ",
        "ai": "ੈ",
        "o": "ੋ",
        "au": "ੌ",
    },
    "Romanized": {},
    "Normal": {},
    "Urdu": {},
    "Sharada": {
        "a": "",
        "A": "𑆳",
        "i": "𑆴",
        "I": "𑆵",
        "e": "𑆼",
        "ai": "𑆽",
        "o": "𑆾",
        "au": "𑆿",
        "RR": "𑆹",
        "R": "𑆸",
        "u": "𑆶",
        "U": "𑆷",
        "LRR": "𑆻",
        "LR": "𑆺",
    },
    "Modi": {
        "a": "",
        "A": "𑘰",
        "i": "𑘱",
        "I": "𑘲",
        "e": "𑘹",
        "ai": "𑘺",
        "o": "𑘻",
        "au": "𑘼",
        "RR": "𑘶",
        "R": "𑘵",
        "u": "𑘳",
        "U": "𑘴",
        "LRR": "𑘸",
        "LR": "𑘷",
    },
    "Brahmi": {
        "a": "",
        "A": "𑀸",
        "i": "𑀺",
        "I": "𑀻",
        "e": "𑁂",
        "ai": "𑁃",
        "o": "𑁄",
        "au": "𑁅",
        "RR": "𑀿",
        "R": "𑀾",
        "u": "𑀼",
        "U": "𑀽",
        "LRR": "𑁁",
        "LR": "𑁀",
    },
    "Siddham": {
        "a": "",
        "A": "𑖯",
        "i": "𑖰",
        "I": "𑖱",
        "e": "𑖸",
        "ai": "𑖹",
        "o": "𑖺",
        "o1": "𑖺",
        "au": "𑖻",
        "au1": "𑖻",
        "RR": "𑖵",
        "R": "𑖴",
        "u": "𑖲",
        "U": "𑖳",
        "u1": "𑗜",
        "U1": "𑗝",
    },
    "Granth": {
        "a": "",
        "A": "𑌾",
        "i": "𑌿",
        "I": "𑍀",
        "u": "𑍁",
        "U": "𑍂",
        "e": "𑍇",
        "ai": "𑍈",
        "o": "𑍋",
        "o1": "𑍋",
        "au": "𑍌",
        "au1": "𑍌",
        "RR": "𑍄",
        "R": "𑍃",
        "LRR": "𑍣",
        "LR": "𑍢",
    },
    "Tamil-Extended": {
        "a": "",
        "A": "ா",
        "i": "ி",
        "I": "ீ",
        "E": "ெ",
        "au": "ௌ",
        "au1": "ௌ",
        "e": "ே",
        "O": "ொ",
        "O1": "ொ",
        "ai": "ை",
        "o": "ோ",
        "o1": "ோ",
        "u": "ு",
        "U": "ூ",
    },
}
mAtrA["Assamese"] = deepcopy(mAtrA["Bengali"])
lang_list = [
    "Sanskrit",
    "Bengali",
    "Telugu",
    "Tamil",
    "Sinhala",
    "Gujarati",
    "Malayalam",
    "Kannada",
    "Oriya",
    "Assamese",
    "Punjabi",
    "Urdu",
    "Romanized",
    "Sharada",
    "Modi",
    "Brahmi",
    "Normal",
    "Siddham",
    "Tamil-Extended",
    "Granth",
]
p = {}
bhAShAmAtrA = {}
for x in lang_list:
    p[x] = {}
    bhAShAmAtrA[x] = {}


def swap(js):
    ret = {}
    for key in js:
        ret[js[key]] = key
    return ret


for lang in mAtrA:
    bhAShAmAtrA[lang] = swap(mAtrA[lang])
for lang in a:
    if lang in ("Hindi", "Marathi", "Konkani", "Nepali"):
        continue
    for char in a[lang]:
        if char == "く" or char == "x":
            continue
        for varna in a[lang][char]:
            v = a[lang][char][varna]
            if varna == "AU":
                continue
            if v[0] in p[lang]:
                pUrva = p[lang][v[0]]
                if len(pUrva) > len(varna):
                    p[lang][v[0]] = varna + (
                        "此" if v[-1] == 1 else ("百" if v[-1] == 3 else "")
                    )
                else:
                    continue
            else:
                if v[0] in bhAShAmAtrA[lang]:
                    p[lang][v[0]] = "." + bhAShAmAtrA[lang][v[0]]
                else:
                    p[lang][v[0]] = varna + (
                        "此" if v[-1] == 1 else ("百" if v[-1] == 3 else "")
                    )
for lang in a:
    extra = ""
    if lang in ("Hindi", "Marathi", "Konkani", "Nepali"):
        continue
    if lang in ("Normal"):
        continue
    p1 = p[lang]
    ak = a[lang]
    if lang == "Punjabi":
        p1["ੰ"] = "M"
    if lang == "Romanized":
        p1[ak["."][".A"][0]] = "A"
        p1[ak["."][".AI"][0]] = "ai"
        p1[ak["."][".AU"][0]] = "au"
        p1[ak["a"]["aiI"][0]] = "ai"
        p1[ak["a"]["auU"][0]] = "au"
        p1[ak["."][".O"][0]] = "O"
        p1[ak["."][".E"][0]] = "E"
        p1[ak["."][".I"][0]] = "I"
        p1[ak["."][".U"][0]] = "U"
        p1[ak["."][".R"][0]] = "R"
        p1[ak["."][".Rz"][0]] = "Rz"
        p1[ak["."][".RR"][0]] = "RR"
        p1[ak["."][".G"][0]] = "G"
        p1[ak["."][".J"][0]] = "J"
        p1[ak["."][".Y"][0]] = "Y"
        p1[ak["."][".T"][0]] = "T"
        p1[ak["."][".D"][0]] = "D"
        p1[ak["."][".Dz"][0]] = "Dz"
        p1[ak["."][".Dhz"][0]] = "Dhz"
        p1[ak["."][".N"][0]] = "N"
        p1[ak["."][".LR"][0]] = "LR"
        p1[ak["."][".LRR"][0]] = "LRR"
        p1[ak["."][".Lz"][0]] = "Lz"
        p1[ak["."][".L"][0]] = "L"
        p1[ak["."][".M"][0]] = "M"
        p1[ak["."][".MM"][0]] = "MM"
        p1[ak["."][".M1"][0]] = "M"
        p1[ak["."][".H"][0]] = "H"
        p1[ak["L"]["Lz"][0]] = "Lz"
        p1[ak["r"]["rz"][0]] = "rz"
        p1[ak["n"]["nz"][0]] = "nz"
        p1[ak["y"]["yz"][0]] = "yz"
        p1[ak["M"]["M2"][0]] = "M"
        p1[ak["."][".M1"][0]] = "M"
        p1["M"] = "m"
        p1["M1"] = "M"
        p1["z"] = "jz"
        for x in ak:
            if not (x.isascii() and x.isupper()) or x in "SMく":
                continue
            p1[ak[x][x + "1"][0]] = x.lower()
        continue
    if lang != "Urdu":
        extra = "此"
        p1[ak["Q"]["QQ"][0]] = "''"
        p1[ak["Y"]["Y"][0]] = "Y" + extra
    p1[ak["f"]["f"][0]] = "ph" + (extra if lang != "Tamil-Extended" else "百")
    p1[ak["c"]["ch"][0]] = "ch" + extra
    p1[ak["c"]["chh"][0]] = "chh" + extra
    p1[ak["w"]["w"][0]] = "v" + extra
    p1[ak["q"]["qq"][0]] = "基"
    if ".z" in ak["."] or lang == "Urdu":
        p1[ak["D"]["Dz"][0]] = "Dz" + extra
        p1[ak["D"]["Dhz"][0]] = "Dhz" + extra
        p1[ak["j"]["jz"][0]] = "jz" + extra
    if lang == "Malayalam":
        p1[ak["a"]["au"][0]] = "au"
        p1[ak["a"]["au1"][1]] = "au"
        p1[mAtrA[lang]["o1"]] = "o"
        p1[mAtrA[lang]["O1"]] = "O"
    elif lang == "Sinhala":
        p1[ak["a"]["aiI"][0]] = "au"
        p1[ak["a"]["auU"][0]] = "ai"
        p1[mAtrA[lang]["o1"]] = "o"
        p1[mAtrA[lang]["O1"]] = "O"
        p1[mAtrA[lang]["au1"]] = "au"
        p1[ak["a"]["aiI"][1]] = "au"
        p1[ak["a"]["auU"][1]] = "ai"
        p1[ak["G"]["G1"][0]] = "G" + extra
        p1[ak["J"]["J1"][0]] = "J" + extra
        p1[ak["j"]["j1"][0]] = "jY" + extra
        p1[ak["n"]["nz"][0]] = "nd" + extra
        p1[ak["m"]["mz"][0]] = "mb" + extra
        p1[ak["N"]["Nz"][0]] = "ND" + extra
    elif lang == "Sanskrit":
        p1[ak["a"]["aiI"][0]] = "au"
        p1[ak["a"]["auU"][0]] = "ai"
        p1[ak["a"]["aiI"][1]] = "au"
        p1[ak["a"]["auU"][1]] = "ai"
        p1["ऒ"] = "o"
        p1["ॊ"] = "o"
        p1["ऎ"] = "e"
        p1["ॆ"] = "e"
        p1["ऄ"] = "a"
        p1["ॳ"] = "oe"
        p1["ऺ"] = "oe"
        p1["ॴ"] = "aue"
        p1["ऻ"] = "aue"
        p1["ॵ"] = "au"
        p1["ॏ"] = "au"
    elif lang == "Urdu":
        p1[ak["a"]["a1"][0]] = "a"
        p1[ak["a"]["aa"][0]] = "a"
        p1[ak["i"]["i1"][0]] = "i"
        p1[ak["u"]["u1"][0]] = "u"
        p1[ak["e"]["e1"][0]] = "e"
        p1[ak["U"]["U1"][0]] = "U"
        p1[ak["I"]["I1"][0]] = "I"
        p1[ak["y"]["y"][0]] = "i"
        p1[ak["v"]["v"][0]] = "u"
        p1[ak["y"]["y4"][0]] = "i"
        p1[ak["v"]["v4"][0]] = "u"
        p1[ak["h"]["h4"][0]] = "h"
        p1[ak["k"]["k1"][0]] = "k"
        p1[ak["k"]["kh1"][0]] = "khz"
        p1[ak["g"]["g1"][0]] = "gz"
        p1[ak["j"]["jz1"][0]] = "jz"
        p1[ak["j"]["jz2"][0]] = "jz"
        p1[ak["j"]["jz3"][0]] = "jz"
        p1[ak["z"]["z"][0]] = "jz"
        p1[ak["z"]["z1"][0]] = "jz"
        p1[ak["z"]["z2"][0]] = "jz"
        p1[ak["z"]["z3"][0]] = "jz"
        p1[ak["t"]["t1"][0]] = "t"
        p1[ak["t"]["t2"][0]] = "t"
        p1[ak["s"]["s1"][0]] = "s"
        p1[ak["s"]["s2"][0]] = "s"
        p1[ak["h"]["h1"][0]] = "h"
        p1[ak["h"]["h2"][0]] = "h"
        p1[ak["s"]["sh"][0]] = "sh"
        p1[ak["R"]["R"][0]] = "ri"
        p1["ف"] = "phz"
    elif lang == "Tamil":
        p1["க"] = "k" + extra
        p1["ச"] = "ch" + extra
        p1["த"] = "t" + extra
        p1["ட"] = "T" + extra
        p1["ப"] = "p" + extra
        p1["ரு"] = "ru"
        p1[ak["L"]["LR"][0]] = "lri"
        p1["ஔ"] = "au"
        p1[mAtrA[lang]["au1"]] = "au"
        p1[mAtrA[lang]["o1"]] = "o"
        p1[mAtrA[lang]["O1"]] = "O"
        p1["ஔ"] = "au"
    elif lang == "Tamil-Extended":
        p1["ச²"] = "chh百"
        p1[mAtrA[lang]["au1"]] = "au"
        p1[mAtrA[lang]["o1"]] = "o"
        p1[mAtrA[lang]["O1"]] = "O"
        p1[ak["R"]["R"][0]] = "R"
        p1[ak["L"]["LR"][0]] = "LR"
        p1[ak["R"]["R"][0][:-1]+"₂"] = "R"
        p1[ak["L"]["LR"][0][:-1]+"₂"] = "LR"
        for w in "kh,g,gh,chh,jh,th,d,dh,Th,D,Dh,ph,b,bh".split(","):
            vb = ak[w[0]][w][0]
            p1[vb[:-1] + {"²": "₂", "³": "₃", "⁴": "₄"}[vb[-1]]] = w + "百"
    elif lang == "Punjabi":
        p1["ਰਿ"] = "ri"
    elif lang == "Bengali":
        p1[ak["b"]["b"][0]] = "b" + extra
        p1[ak["t"]["t1"][0]] = "t" + extra
        p1[mAtrA[lang]["o1"]] = "o"
        p1[mAtrA[lang]["au1"]] = "au"
    elif lang == "Siddham":
        p1[ak["i"]["i1"][0]] = "i"
        p1[ak["i"]["i2"][0]] = "i"
        p1[ak["I"]["I1"][0]] = "I"
        p1[ak["."][".u1"][0]] = ".u"
        p1[ak["."][".U1"][0]] = ".U"
    elif lang == "Telugu":
        p1[mAtrA[lang]["ai1"]] = "ai"
        pass
    elif lang == "Oriya":
        p1[mAtrA[lang]["ai1"]] = "ai"
        p1[mAtrA[lang]["o1"]] = "o"
        p1[mAtrA[lang]["au1"]] = "au"
        p1["ୱ"] = "v" + extra
        p1["ଯ"] = "y" + extra
    elif lang == "Kannada":
        p1[mAtrA[lang]["I1"]] = "I"
        p1[mAtrA[lang]["ai1"]] = "ai"
        p1[mAtrA[lang]["E1"]] = "E"
        p1[mAtrA[lang]["o1"]] = "o"
        p1[mAtrA[lang]["O1"]] = "O"
        p1[mAtrA[lang]["O2"]] = "O"
    elif lang == "Gujarati":
        p1[ak["a"]["aiI"][0]] = "au"
        p1[ak["a"]["auU"][0]] = "ai"
        p1[ak["a"]["aiI"][1]] = "au"
        p1[ak["a"]["auU"][1]] = "ai"
    elif lang == "Sharada":
        p1[ak["'"]["''1"][0]] = "''"
    elif lang == "Siddham":
        p1[mAtrA[lang]["o1"]] = "o"
        p1[mAtrA[lang]["au1"]] = "au"
        p1[mAtrA[lang]["u1"]] = "u"
        p1[mAtrA[lang]["U1"]] = "U"
    elif lang == "Granth":
        p1[mAtrA[lang]["o1"]] = "o"
        p1[mAtrA[lang]["au1"]] = "au"
    p1["↓"] = "#an"
    p1["↑"] = "#s"
    p1["↑↑"] = "#ss"
    p1["↑↑↑"] = "#sss"
    if "AUM1" in ak["A"]:
        if ak["A"]["AUM1"][0] == "ॐ":
            p1["ॐ"] = "AUM"
p1 = deepcopy(p)
for lang in p:
    if lang in ("Romanized", "Normal"):
        continue
    if ".z" not in a[lang]["."]:
        continue
    for varna in p[lang]:
        v = p[lang][varna]
        if v[-1] == "此" and v[-2] == "z" and len(varna) == 1:
            tr = v[:-2]
            p1[lang][a[lang][tr[0]][tr][0] + a[lang]["."][".z"][0]] = v
p = p1
for lang in a:
    if lang in ("Hindi", "Marathi", "Konkani", "Nepali"):
        continue
    if lang in ("Romanized", "Normal", "Urdu"):
        continue
    p1 = p[lang]
    ak = a[lang]
    if ".z" in ak["."]:
        nukta = ak["."][".z"][0]
        p1[ak["p"]["ph"][0] + nukta] = "phz此"
d = dumps(p, ensure_ascii=False, sort_keys=False, indent=4)
copy(d)
file = open(r"anudattAMsh.json", mode="w+", encoding="utf-8")
file.write(d)
file.close()
file = open(
    r"D:\Softwares\Z\jAlAnuprayogaH\src\datt\anudattAMsh.json",
    mode="w+",
    encoding="utf-8",
)
file.write(d)
file.close()