import tkinter as tk
from tkinter.font import Font


class qr:
    def __init__(self, el) -> None:
        self.r = el

    def add(self, el, **keys) -> None:
        css = None
        if "cls" in keys:
            keys["class"] = keys["cls"]
            del keys["cls"]
        if "css" in keys:
            css = keys["css"]
            del keys["css"]
        for x in keys:
            if x not in self.r.wdgts:
                self.r.wdgts[x] = {}
            vl: str = keys[x]
            ky = self.r.wdgts[x]
            if x == "id":
                vl = vl.split(" ")[0]
            for y in vl.split(" "):
                if y not in ky:
                    ky[y] = set()
                elif x == "id":
                    continue
                ky[y].add(el)
        if css != None:
            self.css(el, css)
        return el

    def get(self, id: str) -> list:
        tp = str(type(id))[8:-2]
        if tp == "list":
            return id
        elif tp != "str":
            return [id]
        el = set()
        for x in id.split(", "):
            tag = ""
            nm = ""
            if x[0] in ["#", "."]:
                tag = {"#": "id", ".": "class"}[x[0]]
                nm = x[1:]
            elif x[0] == "[" and x[-1] == "]":
                tmp = x[1:-1].split("=")
                tag = tmp[0]
                nm = tmp[1]
            if tag in self.r.wdgts and nm in self.r.wdgts[tag]:
                el = el | self.r.wdgts[tag][nm]  # Appending the Found Elements
        return list(el)

    def __normalize_css(self, e, p: dict):
        tp = str(type(e))[8:-2]
        mp = {
            "color": "foreground",
            "background-color": "background"
        }
        r = {}
        fnt = dict(family="Nirmala UI", size=10, weight="bold")
        if ("font-weight" in p) or ("font-size" in p) or ("font-family" in p):
            for x in fnt.keys():
                if f"font-{x}" in p:
                    fnt[x] = p[f"font-{x}"]
            r["font"] = Font(**fnt)
        for x in p:
            if x in mp:
                r[mp[x]] = p[x]
        return r

    def css(self, e, p) -> None:
        tp = str(type(e))[8:-2]
        if tp == "str":
            e = self.get(e)
        elif tp == "list":
            pass
        else:
            e = [e]
        for el in e:
            pr = self.__normalize_css(el, p)  # Normalizing
            el.configure(pr)

    def on(self, id, typ: str, func) -> None:
        el = self.get(id)
        mp = {
            "onclick": "<Button-1>",
            "onhoverin": "<Enter>",
            "onhoverout": "<Leave>",
        }
        if typ in mp:
            typ = mp[typ]
        for x in el:
            x.bind(typ, func)

    def onclick(self, id, func):
        self.on(id, "onclick", func)

    def onhover(self, id, func):
        self.on(id, "onhoverin", func)

    def onhoverin(self, id, func):
        self.on(id, "onhoverin", func)

    def onhoverout(self, id, func):
        self.on(id, "onhoverout", func)


class chitra_mUla:
    def __init__(self, el: tk.Tk) -> None:
        self.root = el
        self.query = qr(self)
        self.wdgts = {}  # Storing Widgets
