let html_data = [
    document.getElementById("0").innerHTML,
    document.getElementById("1").innerHTML,
    document.getElementById("2").innerHTML,
    document.getElementById("3").innerHTML,
    document.getElementById("4").innerHTML,
    document.getElementById("5").innerHTML
];
document.getElementById("bdy").innerHTML = html_data[0];

let dynamic_redirect_status = false;

function swap(js) {
    let ret = {};
    for (let key in js)
        ret[js[key]] = key;
    return ret;
}

varNAH = {
    //त्रयोवर्णस्य
    "Dhx": "ढ़्",
    "khz": "ख़्",
    "phz": "फ़्",
    //द्वौवर्णस्य
    "#0": "०",
    "#1": "१",
    "#2": "२",
    "#3": "३",
    "#4": "४",
    "#5": "५",
    "#6": "६",
    "#7": "७",
    "#8": "८",
    "#9": "९",
    "kh": "ख्",
    "gz": "ग़्",
    "kz": "क़्",
    "jz": "ज़्",
    "fz": "फ़्",
    "gh": "घ्",
    "ch": "छ्",
    "jh": "झ्",
    "Sh": "ष्",
    "th": "थ्",
    "dh": "ध्",
    "Th": "ठ्",
    "Dh": "ढ्",
    "ph": "फ्",
    "bh": "भ्",
    "Dx": "ड़्",
    "sh": "श्",
    "yz": "य़्",
    "Lz": "ऴ्",
    "MM": "ँ",
    "..": "॥",
    //एकोवर्णस्य
    "k": "क्",
    "g": "ग्",
    "G": "ङ्",
    "c": "च्",
    "j": "ज्",
    "Y": "ञ्",
    "J": "ञ्",
    "T": "ट्",
    "D": "ड्",
    "N": "ण्",
    "t": "त्",
    "d": "द्",
    "n": "न्",
    "p": "प्",
    "f": "फ्",
    "b": "ब्",
    "m": "म्",
    "s": "स्",
    "S": "ष्",
    "y": "य्",
    "r": "र्",
    "l": "ल्",
    "v": "व्",
    "w": "व्",
    "L": "ळ्",
    "h": "ह्",
    "H": "ः",
    "M": "ं",
    "F": "ऽ",
    "~": "॒",
    "$": "₹",
    ".": "।",
    "Q":"०"
}
mAtrA_chihna = {
    "IRR":"ॣ",
    //द्वौवर्णस्य
    "RR": "ॄ",
    "IR": "ॢ",
    "AW": "ॉ",
    "W": "ॅ",
    "aa": "ा",
    "ii": "ी",
    "uu": "ू",
    "ee": "ै",
    "oo": "ौ",
    //एकोवर्णस्य
    "a": "",
    "A": "ा",
    "i": "ि",
    "I": "ी",
    "u": "ु",
    "U": "ू",
    "e": "े",
    "E": "ै",
    "o": "ो",
    "O": "ौ",
    "R": "ृ"
}
keval_mAtrA = {
    "AUं": "ॐ",
    "IRR":"ॡ",
    //द्वौवर्णस्य
    "RR": "ॠ",
    "IR": "ऌ",
    "aa": "आ",
    "ii": "ई",
    "uu":"ऊ",
    "ee":"ऐ",
    "oo":"औ",
    "AW": "ऑ",
    //एकोवर्णस्य
    "a": "अ",
    "A": "आ",
    "i": "इ",
    "I": "ई",
    "u": "उ",
    "U": "ऊ",
    "e": "ए",
    "E": "ऐ",
    "o": "ओ",
    "O": "औ",
    "R": "ऋ"
}
halant = "्";

function IN(a, b) {
    for (let x = 0; x < b.length; x++)
        if (b[x] === a)
            return true;
    return false;
}
varNAH1 = {
    " ँ": "MM",
    "ं": "M",
    "ः": "H",
    "ॅ": "W",
    "क": "k",
    "ख": "kh",
    "ऑ": "AW",
    "ॉ": "AW",
    "ग": "g",
    "घ": "gh",
    "ङ": "G",
    "०": "#0",
    "१": "#1",
    "२": "#2",
    "३": "#3",
    "४": "#4",
    "५": "#5",
    "६": "#6",
    "७": "#7",
    "८": "#8",
    "९": "#9",
    "च": "c",
    "छ": "ch",
    "ज": "j",
    "झ": "jh",
    "ञ": "Y",
    "ट": "T",
    "ठ": "Th",
    "ड": "D",
    "ढ": "Dh",
    "ण": "N",
    "त": "t",
    "थ": "th",
    "द": "d",
    "़": "z",
    "ध": "dh",
    "न": "n",
    "प": "p",
    "फ": "ph",
    "ब": "b",
    "भ": "bh",
    "म": "m",
    "य": "y",
    "र": "r",
    "ल": "l",
    "ळ": "L",
    "व": "v",
    "श": "sh",
    "ष": "Sh",
    "स": "s",
    "ह": "h",
    "ऽ": "F",
    "॒": "~",
    "क़": "kz",
    "ख़": "khz",
    "ग़": "gz",
    "ज़": "jz",
    "ड़": "Dx",
    "ढ़": "Dhx",
    "फ़": "fz",
    "य़": "yz",
    "ऴ": "Lz",
    "।": ".",
    "॥": "..",
    "₹": "$",
    "ा": "A",
    "ि": "i",
    "ी": "I",
    "ु": "u",
    "ू": "U",
    "ृ": "R",
    "ॄ": "RR",
    "े": "e",
    "ै": "E",
    "ो": "o",
    "ॅ": "W",
    "ौ": "O",
    "ॢ": "IR",
    "ॉ":"AW",
    "ॣ": "IRR",
    "अ": "a",
    "आ": "A",
    "इ": "i",
    "ई": "I",
    "उ": "u",
    "ऊ": "U",
    "ऋ": "R",
    "ॠ":"RR",
    "ऌ": "IR",
    "ॡ":"IRR",
    "ए": "e",
    "ऐ": "E",
    "ओ": "o",
    "औ": "O",
    "ॐ": "AUM"
}
allowed = ["्", "ा", "ि", "ी", "ु", "ू", "े", "ै", "ो", "ौ", "ृ", "ॄ", "ॢ", "ॣ", "ॉ", "ॅ"]

vyanjana = "ढ़ख़फ़खग़क़ज़फ़घछझषथधठढफभड़शय़ऴकगङचजञञटडणतदनपफबमसषयरलवळह".split("")

function replace(str, replaceWhat, replaceTo) {
    replaceWhat = replaceWhat.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&");
    var re = new RegExp(replaceWhat, "g");
    return str.replace(re, replaceTo);
}

function dev_to_code(dev) {
    dev = (dev).split("");
    for (x = 0; x < dev.length; x++) {
        if (IN(dev[x], vyanjana)) {
            if (x === dev.length - 1)
                dev[x] = dev[x] + "a";
            else if (!IN(dev[x + 1], allowed))
                dev[x] = dev[x] + "a";
        }
    }
    dev = dev.join("");
    dev = replace(dev, "्", "");
    a = Object.keys(varNAH1);
    for (x = 0; x < a.length; x++) {
        y = a[x];
        dev = replace(dev, y, varNAH1[y]);
    }
    return dev;
}

function code_to_dev(code) {
    //Converting all vyanjanAH
    a = Object.keys(varNAH);
    for (x = 0; x < a.length; x++) {
        y = a[x];
        code = replace(code, y, varNAH[y]);
    }
    //adding mAtrA chihna
    a = Object.keys(mAtrA_chihna);
    for (x = 0; x < a.length; x++) {
        y = a[x];
        code = replace(code, halant + y, mAtrA_chihna[y]);
    }
    //adding leftover only mAtrA"s
    a = Object.keys(keval_mAtrA);
    for (x = 0; x < a.length; x++) {
        y = a[x];
        code = replace(code, y, keval_mAtrA[y]);
    }
    return code;
}




function display(n) {
    if (n === 3) {
        dynamic_text = document.getElementById("dynamic").value;
        dynamic_text = dev_to_code(dynamic_text);
        dynamic_text = code_to_dev(dynamic_text);
        document.getElementById("dynamic").value = dynamic_text;
        dev_text = dynamic_text
    } else if (n === 2) {
        dev_text = document.getElementById("dev").value;
        code_text = dev_to_code(dev_text);
        document.getElementById("code").value = code_text;
        dynamic_text = code_text
    } else if (n === 1) {
        code_text = document.getElementById("code").value;
        dev_text = code_to_dev(code_text);
        document.getElementById("dev").value = dev_text;
        dynamic_text = dev_text;
    }
}

function change_mode_text(m) {

    if (m === 1) {
        document.getElementById("mode").innerHTML = html_data[4];
        document.getElementById("dynamic").value = dynamic_text;
    } else if (m === 2) {
        dev_num = !dev_num;
        document.getElementById("mode").innerHTML = html_data[5];
        document.getElementById("dev").value = dynamic_text;
        dev_text = document.getElementById("dev").value;
        code_text = dev_to_code(dev_text);
        document.getElementById("code").value = code_text;
    }
}
change_mode_text(1);