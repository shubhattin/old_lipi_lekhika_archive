import keyboard as kb
import mouse
from time import time, sleep
from threading import Thread
from json import loads

# sarve_bhAShA
sarve_bhAShA = "#$',-.0123456789;ACDEGHIJKLMNOQRSTUWYabcdefghijklmnopqrstuvwxyz"
# sarve_bhAShA


class varna:
    def __init__(self, v, t):
        self.name = v
        self.time = time()


class kuYjikolambhikam:
    def __init__(self, obj):
        self.obj = obj
        self.ks = obj.get("ks")
        self.get = lambda x, v=0: obj.get(x, v)
        th = Thread(target=self.__check_value_updates)
        th.daemon = True
        th.start()
        self.main = parivartana(self)
        self.modifier_press_status = (False, "", 0)
        self.last_time = time()
        self.shortcut_press = False
        self.single_alt = True
        self.vrn = varna("", -1)

    def __check_value_updates(self):
        self.__start_all_listeners()
        self.t = 0
        t = 0.1
        while True:
            a = self.get("get_val_change")[1]
            if a:
                self.update()
                self.get("set_val_change", 1)
            else:
                sleep(t)
                if self.ks == 1:
                    self.t += t
            if self.t > 600.0 and self.ks == 1:
                self.ks = 0
                self.t = 0
                self.get("time_exceed")
                self.get("change_less")

    def time_elphased(self, t=time()):
        elph = t - self.last_time
        self.last_time = t
        return elph

    def __start_all_listeners(self):
        def change():
            self.ks = abs(self.ks - 1)
            if self.main.sg_status and self.main.sg:
                self.get("hide_sg")
                self.main.sg_status = False
            self.get("change_less")

        kb.on_release_key("windows", self.on_release)
        kb.on_release_key("shift", self.on_release)
        kb.on_release_key("alt", self.on_release)
        kb.on_release_key("ctrl", self.on_release)
        kb.add_hotkey("ctrl+cmd", change)
        kb.add_hotkey("windows+f6", lambda: kb.press_and_release("volume up"))
        kb.add_hotkey("windows+f5", lambda: kb.press_and_release("volume down"))
        kb.add_hotkey("windows+esc", lambda: self.get("close_from"))
        for x in sarve_bhAShA:
            kb.on_press_key(x, self.process_key, suppress=True)
        kb.on_press(self.detect_key)
        mouse.on_click(lambda: self.clear(mouse=True))
        mouse.on_middle_click(lambda: self.clear(mouse=True))
        mouse.on_right_click(lambda: self.clear(mouse=True))

    def on_release(self, c):
        self.single_alt = True
        if self.modifier_press_status[0]:
            self.modifier_press_status = (False, "", 0)
            self.shortcut_press = False

    def detect_key(self, key):
        tm = key.time
        key = key.name
        if key == None:
            return
        more = True
        if self.modifier_press_status[0] and key != self.modifier_press_status[1]:
            self.shortcut_press = True
        if (
            key == "backspace"
            and self.main.pUrva_lekhit[2][1] == 1
            and self.main.sa_lang == 1
            and self.ks == 1
        ):
            send_keys("backspace")
            self.clear()
        elif self.ks == 1 and self.main.current_lang_code == "Urdu" and key in ("?",):
            send_keys("backspace")
            kb.write(self.main.aksharANI[key][key][0])
            self.clear()
        elif "shift" in key or "caps" in key or self.modifier_press_status[0]:
            more = False
        else:
            self.clear()
        if key in kb.all_modifiers and not self.modifier_press_status[0]:
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
        self.t = 0
        t = self.time_elphased(key.time)
        if t > 15:
            self.clear()
        key = key.name if not already_ready else key
        if len(key) > 1:
            send_keys(key)
            if self.ks == 1:
                self.clear()
        elif (
            self.modifier_press_status[0]
            and "shift" not in self.modifier_press_status[1]
        ):
            self.shortcut_press = True
            kb.press_and_release(key)
            self.clear()
        elif self.ks == 0:
            send_keys(key)
        else:
            self.main.prakriyA(key)

    def clear(self, mouse=False):
        if mouse:
            if self.get("img_pressed"):
                self.get("reset_img_pressed")
                return
            elif self.get("varna_pressed"):
                self.get("reset_varna_pressed")
                return
        if self.ks == 0:
            return
        self.main.clear_all_val(True)

    def update(self):
        m = self.get("msg")
        if len(m) == 0:
            return
        for x in m:
            if x == "update_ks":
                self.ks = self.get("ks")
                if self.ks == 1:
                    self.t = 0
            elif x == "clear_vals":
                self.clear()
            elif x == "change_lang":
                self.main.set_typing_lang(self.get("lang"))
            elif x == "update_sa":
                self.main.sa_lang = self.get("sa")
            elif x == "sg":
                self.main.sg = not self.main.sg
            elif x == "clear_sg":
                self.main.capital = [0, "", -1, -1, 0, 0, False]
            elif x == "clicked":
                val = self.get("clicked")
                l = len(val)
                v = 0
                for y in val:
                    v += 1
                    if v == l:
                        self.get("reset_no_procedure")
                    self.vrn.name = y
                    self.vrn.time = time()
                    self.process_key(self.vrn)
            elif x == "restart":
                kb.unhook_all()
                mouse.unhook_all()
                self.__start_all_listeners()
        self.get("null_msg")


def send_keys(key):
    if len(key) == 1:
        kb.write(key)
    else:
        kb.press_and_release(key)


class parivartana:
    def __init__(self, main):
        self.main = main
        self.loaded_scripts = []
        self.akSharAH = {}
        self.sa_lang = main.obj.get("sa")
        lang = main.obj.get("lang")
        self.first = True
        self.set_typing_lang(lang)
        if self.aksharANI["sa"] == 1 and self.sa_lang == 0:
            self.sa_lang = 1
        self.back_space = 0
        self.sg_status = False
        self.sg = self.main.get("sg_status")
        self.small_to_capital = False
        # Format of varNa = [key record, output, whats on screen]
        self.varNa = ["", "", ""]
        self.next_chars = ""
        self.mAtrA_sthiti = False
        self.halanta_add_status = False
        # index,key itself,its varna sthiti,varna sthiti of char preceding it,current time,whats on screen its length
        self.capital = [0, "", -1, -1, 0, 0, False]
        self.d = False  # for ch and chh like where c is free
        self.store_last_of_3 = ""
        self.last_of_3_status_for_mAtrA = False
        self.special_ved_s = False
        self.pUrva_lekhit = [["", -1], ["", -1], ["", -1], ["", -1], ["", -1]]
        self.second_cap_time = 0

    def set_typing_lang(self, lang):
        if lang not in self.loaded_scripts:
            fl = open(
                f"resources/dattAMsh/{lang}.json",
                encoding="utf-8",
                mode="r+",
            )
            self.akSharAH[lang] = loads(fl.read())
            fl.close()
            self.loaded_scripts.append(lang)
        self.aksharANI = self.akSharAH[lang]
        self.current_lang_code = lang
        self.sarve = [c for c in self.aksharANI]
        if lang not in ("Urdu", "Romanized"):
            self.halant = self.aksharANI["."][".x"][0]
        self.sa_lang = self.aksharANI["sa"]
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
                self.main.get("hide_sg")
                self.clear_all_val(True)
            elif key in self.sarve:  # resseting if next chars not continuable
                self.clear_all_val()
                if (
                    self.store_last_of_3 != ""
                    and self.pUrva_lekhit[4][1] != 0
                    and key == "#"
                    and self.current_lang_code == "Tamil-Extended"
                ):
                    self.clear_all_val(True)
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
        cap_0_from_1 = [False, ["", -1]]
        if (
            self.current_lang_code == "Urdu"
            and key in ("a", "i", "u")
            and self.pUrva_lekhit[4][1] == -1
        ):
            key += "1"
        data = self.aksharANI[key[0]]
        current = data[key]
        prev_temp = self.pUrva_lekhit[3][1]
        temp = self.pUrva_lekhit[4][1]
        varna_sthiti = current[-1]
        if self.capital[0] == 2:
            if key == self.capital[1]:
                if time() - self.capital[4] <= 4.0:
                    # converting small to capital
                    key = key.upper()
                    data = self.aksharANI[key]
                    current = data[key]
                    temp = self.capital[3]
                    varna_sthiti = current[-1]
                    self.back_space += 2 * self.capital[5]
                    if varna_sthiti == 0 and self.pUrva_lekhit[2][1] in [1, 3]:
                        cap_0_from_1 = [True, self.pUrva_lekhit[2]]
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
                    if self.sa_lang == 1 and self.capital[3] == 3:
                        self.back_space -= 1
                    self.capital = [3, "", -1, -1, 0, 0, False]
                else:
                    self.capital = [
                        2,
                        key,
                        varna_sthiti,
                        self.pUrva_lekhit[3][1],
                        self.second_cap_time,
                        self.capital[5],
                        False,
                    ]
            else:
                self.capital = [0, "", -1, -1, 0, 0, False]
        if self.mAtrA_sthiti and varna_sthiti in [1, 2]:  # for AUM like
            self.clear_all_val(True)
            self.prakriyA(key[-1])
            return
        # taking information of varana as [1 for svara and 0 others,max limit]
        self.varNa[0] = key
        # storing the state of varṇa i.e, svara or vyanjana
        # taking out output letter in [1]
        self.varNa[1] = current[0]
        if temp in [1, 3]:
            if (
                varna_sthiti == 1
                and key[-1] not in self.next_chars
                and self.sa_lang == 0
            ):  # for adding halant if char is not continuable
                self.halanta_add_status = True
                if temp == 3:
                    self.back_space += 1
                    self.varNa[1] = self.store_last_of_3 + self.varNa[1]
            elif varna_sthiti == 0:
                self.mAtrA_sthiti = True
        if self.capital[0] == 1:
            if key == self.capital[1]:
                self.capital[0] = 2
                self.second_cap_time = time()
            elif (
                key[-1] == self.capital[1]
                and self.aksharANI[self.capital[1].upper()][self.capital[1].upper()][0]
                != self.varNa[1]
            ):
                self.capital[6] = True
                self.capital[0] = 2
                self.capital[2] = varna_sthiti
                self.capital[5] = len(self.varNa[1])
                self.second_cap_time = time()
            else:
                self.capital = [0, "", -1, -1, 0, 0, False]
        if (key == "LR" or key == "r3") and varna_sthiti == 0:
            if prev_temp != 1:
                self.mAtrA_sthiti = False
            elif self.sa_lang == 0:
                self.back_space += 1
        if (
            key == "R"
            and self.current_lang_code == "Tamil"
            and varna_sthiti == 2
            and temp == 1
        ):
            self.back_space += 1
        if self.mAtrA_sthiti:
            self.varNa[1] = current[1]
            if self.sa_lang == 1 and temp == 1:
                self.back_space += 1
            if temp == 3:
                self.back_space += 1
                if self.sa_lang == 1:
                    self.back_space += 1
                self.varNa[1] += self.store_last_of_3
                self.last_of_3_status_for_mAtrA = True
            elif temp == 0 and self.last_of_3_status_for_mAtrA:
                self.varNa[1] += self.store_last_of_3
                self.last_of_3_status_for_mAtrA = True
        if (
            self.current_lang_code == "Tamil-Extended"
            and key == "M"
            and (
                (
                    (
                        prev_temp == 3
                        or (prev_temp == 0 and self.pUrva_lekhit[2][1] == 3)
                    )
                    and temp == 0
                )
                or (
                    self.capital[0] == 3
                    and (
                        (
                            self.pUrva_lekhit[1][1] == 3
                            or (
                                self.pUrva_lekhit[1][1] == 0
                                and self.pUrva_lekhit[0][1] == 3
                            )
                        )
                        and self.pUrva_lekhit[2][1] == 0
                    )
                )
            )
        ):
            self.varNa[1] += self.store_last_of_3
            self.back_space += 1
        if self.current_lang_code == "Tamil-Extended" and key in ["#an", "#s"]:
            if key == "#an" and (
                (
                    self.pUrva_lekhit[1][1] == 3
                    or (self.pUrva_lekhit[1][1] == 0 and self.pUrva_lekhit[0][1] == 3)
                )
                and self.pUrva_lekhit[2][1] == 0
            ):
                self.varNa[1] += self.store_last_of_3
                self.back_space += 1
            elif key == "#s" and (
                (
                    self.pUrva_lekhit[2][1] == 3
                    or (self.pUrva_lekhit[2][1] == 0 and self.pUrva_lekhit[1][1] == 3)
                )
                and self.pUrva_lekhit[3][1] == 0
            ):
                self.varNa[1] += self.store_last_of_3
                self.back_space += 1
                self.special_ved_s = True
        if (
            self.current_lang_code == "Tamil-Extended"
            and key in ["#ss", "#sss"]
            and self.special_ved_s
        ):
            self.varNa[1] += self.store_last_of_3
        if (
            temp == 1
            and varna_sthiti == 2
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
        if (
            ("Tamil" in self.current_lang_code or self.current_lang_code == "Punjabi")
            and key in ["R", "LR", "LRR", "RR"]
            and varna_sthiti == 1
        ):
            varna_sthiti = 2
        if self.sa_lang == 1:
            if varna_sthiti == 1:
                self.varNa[1] += self.halant
            elif varna_sthiti == 3:
                self.varNa[1] = self.varNa[1][:-1] + self.halant + self.varNa[1][-1]
        self.likha(
            self.varNa[1], self.varNa[2], self.back_space, self.halanta_add_status
        )
        if self.capital[0] == 3:
            self.capital = [0, "", -1, -1, 0, 0, False]
        if (
            len(key) == 1
            and key.islower()
            and key.upper() in self.aksharANI
            and self.capital[0] == 0
        ):
            a = [0, "", -1, -1, 0, 0, False]
            b = [1, key, varna_sthiti, temp, time(), len(self.varNa[1]), False]
            if key + key in data:
                if self.aksharANI[key.upper()][key.upper()][0] != data[key + key][0]:
                    self.capital = b
                else:
                    self.capital = a
            else:
                self.capital = b
        self.next_chars = current[-2]
        if self.sg:
            a = {
                "key": (key, self.next_chars),
                "status": (temp, varna_sthiti),
                "mAtrA": self.mAtrA_sthiti,
                "special_cap": cap_0_from_1,
            }
            if self.capital[0] == 1:
                a["cap"] = True
            if key != ".":
                self.main.get("show_sg", a)
            else:

                def jkl():
                    self.main.get("show_sg", a)

                th = Thread(target=jkl)
                th.daemon = True
                th.start()
            self.sg_status = True
        elif self.sg_status and self.sg:
            self.main.get("hide_sg")
            self.sg_status = False
        if varna_sthiti == 3:
            self.store_last_of_3 = self.varNa[1][-1]
        if self.next_chars == "":
            self.clear_all_val()
        self.pUrva_lekhit[0] = self.pUrva_lekhit[1]
        self.pUrva_lekhit[1] = self.pUrva_lekhit[2]
        self.pUrva_lekhit[2] = self.pUrva_lekhit[3]
        self.pUrva_lekhit[3] = self.pUrva_lekhit[4]
        self.pUrva_lekhit[4] = [key, varna_sthiti]

    def clear_all_val(self, special=False):
        self.next_chars = ""
        self.varNa = ["", "", ""]
        self.mAtrA_sthiti = False
        self.last_of_3_status_for_mAtrA = False
        self.special_ved_s = False
        self.back_space = 0
        if special:
            self.store_last_of_3 = ""
            self.pUrva_lekhit = [["", -1], ["", -1], ["", -1], ["", -1], ["", -1]]
            self.main.get("hide_sg")
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
            kb.press_and_release("backspace")
        if hal:
            lekha = self.halant + lekha
        self.back_space = 0
        self.halanta_add_status = False
        kb.write(lekha)
