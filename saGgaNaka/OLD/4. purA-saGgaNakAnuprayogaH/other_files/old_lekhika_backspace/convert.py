from tkinter.constants import FALSE
from tkinter.font import families
from keyboard import write, press_and_release
import pkg_resources
from time import time
from dattAMsh import akSharAH, mAtrA
from Design import alert, get_registry, lang_code


class parivartana:
    def __init__(self, main):
        self.main_ready = False
        self.sa_lang = get_registry("sa_mode")
        self.set_typing_lang(main.lang_mode, 0)
        self.back_space = 0
        self.main = main
        self.main_ready = True
        self.current_lang_code = main.lang_mode
        self.small_to_capital = False
        # Format of varNa = [key record, output, whats on screen]
        self.varNa = ["", "", ""]
        self.varNa_sthiti = -1
        self.next_chars = ""
        self.mAtrA_sthiti = False
        self.halanta_add_status = False
        # [key code, whats on screen, varna sthiti]
        self.last_key_record = ["", "", -1, False]
        # also carrying exjktra information in breaker for its functioning
        # as (condition,next supported chars,varna sthiti)
        self.breaker_status = (False, "", 0)
        self.d = False  # for ch and chh like where c is free

    def set_typing_lang(self, lang, c=0):
        self.aksharANI = akSharAH[lang]
        self.current_lang_code = lang
        if self.main_ready:
            self.main.r.update_sans_mode(1, self.aksharANI["梵文"])
        self.sarve = [c for c in self.aksharANI]
        if lang != "ia":
            self.halant = self.aksharANI["!"]["!"][0]
        if c > 0:
            if c == 2:
                self.main.r.typing_lang.set(lang_code[1][lang])
            self.main.systray.update(hover_text=self.main.taskbar_text())
            alert(
                "Typing Language Changed To " + lang_code[2][lang],
                color="green",
                lapse=1200,
            )

    def prakriyA(self, key):
        if self.next_chars == "" and key in self.sarve:
            self.varNa[2] = key
            self.vitaraNa(key)
        elif key == ";":
            self.breaker_status = (True, self.next_chars, self.varNa_sthiti)
            # clearing all as what's required is already stored above
            self.clear_all_val(True)
        elif key == "," and self.last_key_record[3]:
            self.main.time_temp = time()
            self.main.small2capital = True
            self.last_key_record[3] = False
        elif self.next_chars != "":
            if key in self.next_chars:
                if self.d:
                    self.halanta_add_status = True
                    self.d = False
                self.varNa[2] = self.varNa[1] + key
                key = self.varNa[0] + key
                self.vitaraNa(key)
            elif key in self.sarve:  # resseting if next chars not continuable
                self.clear_all_val()
                self.varNa[2] = key
                self.vitaraNa(key)
            else:
                if key == "backspace" and self.varNa_sthiti == 1 and self.sa_lang == 1:
                    press_and_release("backspace")
                self.clear_all_val(True)  # if not found cleared.
        else:
            if key == "backspace" and self.varNa_sthiti == 1 and self.sa_lang == 1:
                press_and_release("backspace")
            # Just for clearing varNa_sthit as else eyerthing is ok
            self.clear_all_val(True)

    def vitaraNa(self, key):
        data = self.aksharANI[key[0]]
        current = data[key]
        temp = self.varNa_sthiti
        self.varNa_sthiti = current[-1]
        if self.mAtrA_sthiti and self.varNa_sthiti in [1, 2]:
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
            elif key == "%" and self.sa_lang == 0:
                # adding halant when % comes after 1(hal)
                self.halanta_add_status = True
            elif self.varNa_sthiti == 0:
                self.mAtrA_sthiti = True
        # taking out output letter in [1]
        self.varNa[1] = current[0]
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
                    self.d = True
                    break
        if self.sa_lang == 1 and self.varNa_sthiti == 1:
            # addition of halant in sanskrit mode
            self.varNa[1] += self.halant
        if self.breaker_status[0]:
            if key in self.breaker_status[1]:
                if self.breaker_status[2] == 1 and self.sa_lang == 0:
                    self.halanta_add_status = True
                self.back_space += 1
            self.breaker_status = (False, "", 0)
        self.likha(
            self.varNa[1], self.varNa[2], self.back_space, self.halanta_add_status
        )
        self.next_chars = current[-2]
        if self.next_chars == "":
            self.clear_all_val()
        if len(key) == 1 and key.islower() and key.upper() in self.sarve:
            self.last_key_record = [key, self.varNa[1], self.varNa_sthiti, True]
        else:
            self.last_key_record = ["", "", -1, False]

    def convert_small_to_big(self):
        self.back_space += 2
        if self.last_key_record[2] == 1 and self.sa_lang == 1:
            self.back_space += 1
        up = self.last_key_record[0].upper()
        if self.last_key_record[1] in mAtrA[self.current_lang_code].values():
            out = self.aksharANI[up][up][1]
        else:
            out = self.aksharANI[up][up][0]
        self.varNa_sthiti = self.aksharANI[up][up][-1]
        if self.varNa_sthiti == 1 and self.sa_lang == 1:
            out += self.halant
        self.varNa = [up, out, self.last_key_record[0]]
        self.next_chars = self.aksharANI[up][up][-2]
        self.likha(self.varNa[1], self.varNa[2], self.back_space)
        if self.next_chars == "":
            self.clear_all_val()

    def clear_all_val(self, special=False):
        self.next_chars = ""
        self.varNa = ["", "", ""]
        self.mAtrA_sthiti = False
        if special:
            self.varNa_sthiti = -1

    def likha(self, b, a, bk=0, hal=False):
        # a = what is currently on screen
        # b = it is that to which a has to be replaced
        if "見" in a:
            a = list(a)
            a.remove("見")
            a = "".join(a)
        back = 0
        lekha = ""
        if b[0] != a[0]:
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
        if "見" in lekha:
            lekha = ""
        elif hal:
            lekha = self.halant + lekha
        self.back_space = 0
        self.halanta_add_status = False
        write(lekha)
