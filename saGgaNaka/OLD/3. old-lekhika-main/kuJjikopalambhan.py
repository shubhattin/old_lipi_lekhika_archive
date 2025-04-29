from keyboard import (
    add_hotkey,
    on_press,
    on_release_key,
    wait,
    all_modifiers,
    on_press_key,
    write,
    press_and_release,
    add_hotkey,
)
from mouse import on_click, on_middle_click, on_right_click
from time import time, sleep
from dattAMsh import akSharAH, sarve_bhAShA
import pkg_resources


class kuYjikolambhikam:
    def __init__(self, obj):
        self.obj = obj
        first = obj.get("first")
        self.ks = obj.get("ks")
        self.get = lambda x, v=0: obj.get(x, v)
        self.main = parivartana(self)
        self.modifier_press_status = (False, "", 0)
        self.last_time = time()
        if first:
            obj.get("startup_msg")
        self.shortcut_press = False
        self.start_all_listeners()
        self.single_alt = True
        wait("windows+esc")

    def time_elphased(self, t=time()):
        elph = t - self.last_time
        self.last_time = t
        return elph

    def start_all_listeners(self):
        def change():
            self.ks = abs(self.ks - 1)
            if self.main.sg_status and self.main.sg:
                self.get("hide_sg")
                self.main.sg_status = False
            self.get("change_less")

        on_release_key("windows", self.on_release)
        on_release_key("shift", self.on_release)
        on_release_key("alt", self.on_release)
        on_release_key("ctrl", self.on_release)
        add_hotkey("ctrl+cmd", change)
        for x in sarve_bhAShA:
            on_press_key(x, self.process_key, suppress=True)
        on_press(self.detect_key)
        on_click(lambda: self.clear_all_val(True))
        on_middle_click(lambda: self.clear_all_val(True))
        on_right_click(lambda: self.clear_all_val(True))

    def on_release(self, c):
        # key = c.name
        # tm = c.time
        self.single_alt = True
        if self.modifier_press_status[0]:
            self.modifier_press_status = (False, "", 0)
            self.shortcut_press = False

    def detect_key(self, key):
        # print("####",key.name)
        self.update()
        tm = key.time
        t = self.time_elphased(tm)
        if t > 300 and self.ks == 1:
            self.ks = 0
            self.get("change_less")
        key = key.name
        more = True
        if self.modifier_press_status[0] and key != self.modifier_press_status[1]:
            self.shortcut_press = True
        if (
            key == "backspace"
            and self.main.varNa_sthiti == 1
            and self.main.sa_lang == 1
            and self.ks == 1
        ):
            send_keys("backspace")
            self.clear_all_val()
        elif "shift" in key or "caps" in key or self.modifier_press_status[0]:
            more = False
        else:
            self.clear_all_val()
        if key in all_modifiers and not self.modifier_press_status[0]:
            self.modifier_press_status = (True, key, tm)
        if self.main.sg_status and self.main.sg and self.ks == 1 and more:
            self.get("hide_sg")
            self.main.sg_status = False
        if (
            "alt" in key
            and tm - self.modifier_press_status[2] >= 1
            and not self.shortcut_press
            and self.single_alt
        ):
            self.get("show_status")
            self.single_alt = False

    def process_key(self, key, already_ready=False):
        # print("$$$$",key.name)
        a = self.update()
        if a == "close":
            send_keys(key.name)
            return
        t = self.time_elphased(key.time)
        if t > 15:
            self.clear_all_val()
            if t > 300 and self.ks == 1:
                self.ks = 0
                self.get("change_less")
        key = key.name if not already_ready else key
        if len(key) > 1:
            send_keys(key)
            if self.ks == 1:
                self.clear_all_val()
        elif (
            self.modifier_press_status[0]
            and "shift" not in self.modifier_press_status[1]
        ):
            self.shortcut_press = True
            press_and_release(key)
            self.clear_all_val()
        elif self.ks == 0:
            send_keys(key)
        else:
            self.main.prakriyA(key)

    def clear_all_val(self, mo=False):
        if mo:
            self.update(mo)
            if self.main.sg_status and self.main.sg:
                self.get("hide_sg")
                self.main.sg_status = False
        if self.ks == 0:
            return
        self.main.clear_all_val(True)

    def update(self, mouse=False):
        m = self.get("msg")
        if len(m) == 0:
            return
        for x in m:
            if x == "update_ks":
                self.ks = self.get("ks")
                self.get("null_msg")
                if not mouse:
                    return "close"
            elif x == "clear_vals":
                self.clear_all_val()
            elif x == "change_lang":
                self.main.set_typing_lang(self.get("lang"))
            elif x == "update_sa":
                self.main.sa_lang = self.get("sa")
            elif x == "sg":
                self.main.sg = not self.main.sg
        self.get("null_msg")


def send_keys(key):
    if len(key) == 1:
        write(key)
    else:
        press_and_release(key)


class parivartana:
    def __init__(self, main):
        self.main = main
        if not self.main.get("tk"):
            while not self.main.get("tk"):
                pass
            sleep(2)
        self.sa_lang = main.obj.get("sa")
        lang = main.obj.get("lang")
        self.first = True
        self.set_typing_lang(lang)
        if self.aksharANI["く"] == 1 and self.sa_lang == 0:
            self.sa_lang = 1
        self.back_space = 0
        self.sg_status = False
        self.sg = self.main.get("sg_status")
        self.small_to_capital = False
        # Format of varNa = [key record, output, whats on screen]
        self.varNa = ["", "", ""]
        self.varNa_sthiti = -1
        self.next_chars = ""
        self.mAtrA_sthiti = False
        self.halanta_add_status = False
        # index,key itself,its varna sthiti,varna sthiti of char preceding it,current time,whats on screen its length
        self.capital = [0, "", -1, -1, 0, 0, False]
        self.d = False  # for ch and chh like where c is free

    def set_typing_lang(self, lang):
        self.aksharANI = akSharAH[lang]
        self.current_lang_code = lang
        self.sarve = [c for c in self.aksharANI]
        if lang not in ("Urdu", "Romanized"):
            self.halant = self.aksharANI["q"]["qq"][0]
        a = self.aksharANI["く"]
        t = self.main.get("sa")
        if self.first and a == 0 and t == 1:
            a = 1
        self.sa_lang = a
        self.main.get("update_sans", a)
        self.first = False

    def prakriyA(self, key):
        if self.next_chars == "" and key in self.sarve:
            self.varNa[2] = ""
            self.vitaraNa(key)
        elif self.next_chars == "" and key.isupper() and key.lower() in self.sarve:
            self.varNa[2] = ""
            self.vitaraNa(key.lower())
        elif self.next_chars != "":
            if key in self.next_chars:
                if self.d:
                    self.halanta_add_status = True
                    self.d = False
                self.varNa[2] = self.varNa[1]
                key = self.varNa[0] + key
                self.vitaraNa(key)
            elif key == "q" or key == ";":
                self.clear_all_val(True)
            elif key in self.sarve:  # resseting if next chars not continuable
                self.clear_all_val()
                self.vitaraNa(key)
            elif key.isupper() and key.lower() in self.sarve:
                self.clear_all_val()
                self.vitaraNa(key.lower())
            else:
                send_keys(key)
                self.clear_all_val(True)
        else:
            send_keys(key)
            self.clear_all_val(True)

    def vitaraNa(self, key):
        data = self.aksharANI[key[0]]
        current = data[key]
        temp = self.varNa_sthiti
        self.varNa_sthiti = current[-1]
        if self.capital[0] == 2:
            if key == self.capital[1] and time() - self.capital[4] <= 4.0:
                # converting small to capital
                key = key.upper()
                data = self.aksharANI[key]
                current = data[key]
                temp = self.capital[3]
                self.varNa_sthiti = current[-1]
                self.back_space += 2 * self.capital[5]
                if self.capital[6]:
                    self.back_space -= 1
                    if self.sa_lang == 1:
                        if self.capital[3] == 1:
                            self.back_space -= 1
                        if self.capital[2] == 1:
                            self.back_space += 2
                    if self.capital[3] != 1 and self.capital[2] == 1:
                        self.back_space -= 1
                if self.sa_lang == 0:
                    if self.capital[2] == 1:
                        self.back_space += 1
                        if self.capital[3] == 1 and not self.capital[6]:
                            self.back_space += 1
            self.capital = [0, "", -1, -1, 0, 0, False]
        if self.mAtrA_sthiti and self.varNa_sthiti in [1, 2]:  # for AUM like
            self.clear_all_val(True)
            self.prakriyA(key[-1])
            return
        # taking information of varana as [1 for svara and 0 others,max limit]
        self.varNa[0] = key
        # storing the state of varṇa i.e, svara or vyanjana
        if temp == 1:
            if (
                self.varNa_sthiti == 1
                and key[-1] not in self.next_chars
                and self.sa_lang == 0
            ):  # for adding halant if char is not continuable
                self.halanta_add_status = True
            elif self.varNa_sthiti == 0:
                self.mAtrA_sthiti = True
        # taking out output letter in [1]
        self.varNa[1] = current[0]
        if self.capital[0] == 1:
            if key == self.capital[1]:
                self.capital[0] = 2
            elif (
                key[-1] == self.capital[1]
                and self.aksharANI[self.capital[1].upper()][self.capital[1].upper()][0]
                != self.varNa[1]
            ):
                self.capital[6] = True
                self.capital[0] = 2
                self.capital[2] = self.varNa_sthiti
                self.capital[5] = len(self.varNa[1])
            else:
                self.capital = [0, "", -1, -1, 0, 0, False]
        if self.mAtrA_sthiti:
            self.varNa[1] = current[1]
            if self.sa_lang == 1 and temp == 1:
                self.back_space += 1
        if (
            temp == 1
            and self.varNa_sthiti == 2
            and len(key) == 1
            and len(data) > 1
            and self.sa_lang == 0
        ):
            # for ch, chh for where c is nothing
            for x in current[-2]:
                if key + x in data:
                    if data[key + x][-1] == 1:
                        self.d = True
                    break
        if self.sa_lang == 1 and self.varNa_sthiti == 1:
            # addition of halant in sanskrit mode
            self.varNa[1] += self.halant
        self.likha(
            self.varNa[1], self.varNa[2], self.back_space, self.halanta_add_status
        )
        if (
            len(key) == 1
            and key.islower()
            and key.upper() in self.aksharANI
            and self.capital[0] == 0
        ):
            a = [0, "", -1, -1, 0, 0, False]
            b = [1, key, self.varNa_sthiti, temp, time(), len(self.varNa[1]), False]
            if key + key in data:
                if self.aksharANI[key.upper()][key.upper()][0] != data[key + key][0]:
                    self.capital = b
                else:
                    self.capital = a
            else:
                self.capital = b
        self.next_chars = current[-2]
        if (
            (self.next_chars != "" or self.capital[0] == 1)
            and self.sg
            and self.current_lang_code not in ("Sharada", "Modi", "Brahmi")
        ):
            a = {"key": (key, self.next_chars), "status": (temp, self.varNa_sthiti)}
            if self.capital[0] == 1:
                a["cap"] = True
            self.main.get("show_sg", a)
            self.sg_status = True
        elif self.sg_status and self.sg:
            self.main.get("hide_sg")
            self.sg_status = False
        if self.next_chars == "":
            self.clear_all_val()

    def clear_all_val(self, special=False):
        self.next_chars = ""
        self.varNa = ["", "", ""]
        self.mAtrA_sthiti = False
        if special:
            self.varNa_sthiti = -1
            self.main.get("clear_sg_val")
            self.capital = [0, "", -1, -1, 0, 0, False]

    def likha(self, b, a, bk=0, hal=False):
        # a = what is currently on screen
        # b = it is that to which a has to be replaced
        back = 0
        lekha = ""
        if a == "" or b == "":
            lekha = b
            back = len(a)
        elif b[0] != a[0]:
            lekha = b
            back = len(a)
        else:
            x = 0
            for v in a:
                if len(b) == x:
                    break
                if b[x] != a[x]:
                    break
                x += 1
            lekha = b[x:]
            back = len(a) - x
        back += bk  # taking extra bksp's into consideratin
        for m in range(back):
            press_and_release("backspace")
        if hal:
            lekha = self.halant + lekha
        self.back_space = 0
        self.halanta_add_status = False
        write(lekha)
