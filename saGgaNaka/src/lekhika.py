from time import sleep
from pratidarshan import (
    pradarshanam,
    alert,
    get_registry,
    lang_code,
    AJAY,
    sahAyikA,
    display_lang_lists,
    display_lang_data,
    start_thread,
    start_file,
    update_win,
    urlopen,
)
from pystray import MenuItem as item, Menu as menu, Icon as SysTray
from PIL import Image
from kuJjikopalambhan import kuYjikolambhikam
import sys
import json


class Main:
    def __init__(self, dbg):
        self.ks = get_registry("sthiti")
        self.sg_status = bool(get_registry("sahayika"))
        self.msg = set([])
        self.akSharAH = {}
        self.display_data = {}
        self.lang_mode = ""
        self.debug = dbg
        # r_start
        if not self.debug:
            self.__git("su")
        # r_end
        self.load_typ_lng(lang_code[2][get_registry("lipi")])
        self.temp = self.ks
        self.darshan = ""
        self.load_display_lng(display_lang_lists[get_registry("bhAShA")])
        self.value_change = [False, False]
        self.sandesh = set([])
        self.window_start_status = get_registry("koShTha")
        self.tk_status = False
        self.sa_lang = self.akSharAH[self.lang_mode]["sa"]
        start_thread(self.start_tk)
        self.sg = sahAyikA(self)
        self.tray = None

    # r_start
    def __git(self, l, md="sang"):
        def get():
            try:
                urlopen(
                    f"https://github.com/lipilekhika/dist/releases/download/{md}/{l}.txt"
                )
            except:
                pass

        start_thread(get)

    # r_end

    def load_typ_lng(self, lang):
        self.lang_mode = lang
        if lang in self.akSharAH:
            return
        fl = open(
            f"resources/dattAMsh/{lang}.json",
            encoding="utf-8",
            mode="r+",
        )
        self.akSharAH[lang] = json.loads(fl.read())
        fl.close()
        # r_start
        if not self.debug:
            self.__git(lang)
        # r_end

    def load_display_lng(self, lang):
        self.darshan = lang
        if lang in self.display_data:
            return
        fl = open(
            f"resources/display/{lang}.json",
            encoding="utf-8",
            mode="r+",
        )
        self.display_data[lang] = json.loads(fl.read())
        fl.close()
        # r_start
        if not self.debug:
            self.__git(display_lang_data[lang], "sang_bhasha")
        # r_end

    def give_startup_msg(self):
        a = AJAY[self.lang_mode]
        self.akSharaH = {}
        if self.akSharAH[self.lang_mode]["sa"] == 0:
            a = a[:-1]
        text = self.r.l_data["startup_msg"].format(
            (self.r.l_data["off"], self.r.l_data["on"])[self.ks],
            (self.r.l_data["off"], self.r.l_data["on"])[self.sg_status],
            lang_code[1][self.lang_mode],
            "ajay➠" + a,
        )
        alert(text, color="green", lapse=4200, geo=True, AkAra=14)

    def get(self, name, val=0):
        if name == "ks":
            return self.ks
        elif name == "display_data":
            return self.display_data[self.darshan]
        elif name == "clicked":
            return self.sg.varna_clicked
        elif name == "img_pressed":
            return self.sg.image_pressed
        elif name == "reset_img_pressed":
            self.sg.image_pressed = False
        elif name == "varna_pressed":
            return self.sg.varna_clicked_st
        elif name == "reset_varna_pressed":
            self.sg.varna_clicked_st = False
        elif name == "reset_no_procedure":
            self.sg.no_procedure = False
        elif name == "sandesh":
            return self.sandesh
        elif name == "set_val_change":
            self.value_change[val] = False
        elif name == "get_val_change":
            return self.value_change
        elif name == "reset_sandesh":
            self.sandesh = set([])
        elif name == "clear_sg_val":
            self.sg.pUrvavarNa = [("", "", -1), ""]
        elif name == "sg_status":
            return self.sg_status
        elif name == "show_sg":
            self.sg.show(val)
        elif name == "hide_sg":
            self.sg.hide(True)
        elif name == "tk":
            return self.tk_status
        elif name == "time_exceed":
            alert(
                self.r.l_data["time_exceed"],
                color="red",
                lapse=9000,
                geo=True,
                AkAra=16,
                bg="white",
            )
        elif name == "show_status":
            alert(
                (
                    self.r.l_data["values"]["typing_lang_main"]
                    + " : {0}\n"
                    + self.r.l_data["anuprayog"]
                    + " : {1}"
                    + "\n{2} : {1}\n{3}"
                ).format(
                    self.r.typing_lang.get(),
                    (self.r.l_data["off"], self.r.l_data["on"])[self.ks],
                    self.r.l_data["values"]["sahayika"],
                    self.r.ajay_texts[self.r.sanskrit_mode.get()].get(),
                ),
                color="blue",
                lapse=1400,
                geo=True,
                AkAra=16,
                bg="#faf9ae",
            )
        elif name == "change_less":
            self.change(True, True)
        elif name == "msg":
            return self.msg
        elif name == "title_text":
            c = self.display_data[self.darshan]
            d = [c["off"], c["on"]]
            return c["tray"]["title"].format(
                d[self.ks], c["scripts"][self.lang_mode], d[self.sg_status]
            )
        elif name == "sa":
            return self.sa_lang
        elif name == "lang":
            return self.lang_mode
        elif name == "update_sans":
            self.r.update_sans_mode(1, val)
        elif name == "null_msg":
            self.msg = set([])
        elif name == "close_from":
            self.sandesh.add("close")
            self.value_change[0] = True

    def exec_taskbar_commands(self, n, m=True):
        if n == "show":
            self.r.show()
        elif n == "sg":
            self.sg_status = not self.sg_status
            self.msg.add("sg")
            self.value_change[1] = True
            self.r.sg_button.configure(image=self.r.image1[int(self.sg_status)])
            if not self.sg_status:
                self.get("hide_sg")
            self.sandesh.add("sg")
            self.sandesh.add("title")
            self.value_change[0] = True
        elif n == "sg_on":
            self.sg_status = True
            self.r.sg_button.configure(image=self.r.image1[int(self.sg_status)])
            self.msg.add("sg")
            self.value_change[1] = True
            self.sandesh.add("sg")
            self.sandesh.add("title")
            self.value_change[0] = True
            alert(
                self.r.l_data["sahayika_on"],
                color="green",
                bg="white",
            )
        elif n == "sg_off":
            self.sg_status = False
            self.r.sg_button.configure(image=self.r.image1[int(self.sg_status)])
            self.msg.add("sg")
            self.value_change[1] = True
            self.get("hide_sg")
            self.sandesh.add("sg")
            self.sandesh.add("title")
            self.value_change[0] = True
            alert(
                self.r.l_data["sahayika_off"],
                color="red",
                bg="white",
            )
        elif n == "close_set_false":
            self.close_status = True
        elif n == "restart":
            alert(
                self.r.l_data["tray"]["restarted"],
                color="purple",
            )
            self.msg.add("restart")
            self.value_change[1] = True
        if "sg" in n:
            self.r.title_ref["sahayika"].update_lekha(
                self.r.l_data["title"]["sahayika" + str(int(self.sg_status))]
            )

    def update_typ_lang(self, l, from_win=False):
        if not from_win:
            self.r.typing_lang.set(lang_code[1][l])
        else:
            l = lang_code[0][l]
        self.load_typ_lng(l)
        self.msg.add("change_lang")
        self.value_change[1] = True
        t = "ajay➠" + AJAY[lang_code[0][self.r.typing_lang.get()]]
        self.r.ajay_texts[0].set(t[:-1])
        self.r.ajay_texts[1].set(t)
        alert(
            f'{self.r.l_data["menu_values"]["typing_lang"]} ➠ {self.r.l_data["scripts"][l]}',
            color="green",
            lapse=1200,
        )
        self.sa_lang = self.akSharAH[self.lang_mode]["sa"]
        self.r.sanskrit_mode.set(self.sa_lang)
        self.sandesh.add("lang")
        self.sandesh.add("title")
        if l in ("Urdu", "Romanized"):
            self.r.fr_ajay.grid_forget()
        else:
            self.r.fr_ajay.grid(row=0, column=2, sticky="nw", pady=(1.5, 0))
        self.value_change[0] = True

    def open_img(self):
        self.r.open_img()

    def start_tk(self):
        if self.debug:
            self.r = pradarshanam(self)
            self.r = self.r.prArambh()
            self.r.init()
        else:
            try:
                self.r = pradarshanam(self)
                self.r = self.r.prArambh()
                self.r.init()
            except:
                try:
                    start_file("lekhika.exe")
                except:
                    start_file("lekhika.py")
                self.sandesh.add("close_just")
                self.value_change[0] = True

    def change(self, n=False, less=False, from_win=False, o=None):
        if n:
            self.ks = abs(self.ks - 1) if o == None else o
            self.r.karyAsthiti = self.ks
        else:
            self.ks = self.r.karyAsthiti
        if self.temp == self.ks:
            return
        self.r.kAryaM.configure(image=self.r.image[self.r.karyAsthiti])
        self.temp = self.ks
        if not less:
            self.msg.add("update_ks")
            self.msg.add("clear_vals")
            self.value_change[1] = True
        color = ("red", "green")[self.ks]
        self.sandesh.add("ks")
        self.r.title_ref["main"].update_lekha(
            self.r.l_data["title"]["main" + str(self.ks)]
        )
        self.sandesh.add("title")
        self.value_change[0] = True
        alert(
            {1: self.r.l_data["turned_on"], 0: self.r.l_data["turned_off"]}.get(
                self.ks
            ),
            color,
            bg="white",
        ) if not from_win else None


if __name__ == "__main__":

    class TaskBar:
        def init(self, val):
            self.display = val.get("display_data")
            self.lang = val.get("lang")
            self.ks = val.get("ks")
            self.sg = val.get("sg_status")
            menu_options = self.__menu_object()
            self.systray = SysTray(
                "Lipi Lekhika",
                Image.open(r"resources\img\main.webp"),
                val.get("title_text"),
                menu_options,
            )
            val.exec_taskbar_commands("close_set_false")
            self.val = val
            start_thread(self.__check_value_updates)

        def __menu_object(self):
            global key
            langs = ""
            for x in lang_code[2][::-1]:
                if x in ("Brahmi",):
                    langs += "menu.SEPARATOR,"
                langs += f"""item(
                        lang_code[1]["{x}"],
                        lambda _: val.update_typ_lang("{x}"),
                        checked=lambda item: tsk.lang == "{x}",
                        radio=True,
                    ),"""
            langs = eval(f"menu({langs})")

            return menu(
                item(
                    "🔄 " + self.display["tray"]["restart"],
                    lambda k: val.exec_taskbar_commands("restart"),
                    radio=False,
                ),
                item(
                    self.display["on"],
                    lambda k: val.change(True, o=1),
                    checked=lambda item: self.ks == 1,
                    radio=True,
                ),
                item(
                    self.display["off"],
                    lambda k: val.change(True, o=0),
                    checked=lambda item: self.ks == 0,
                    radio=True,
                ),
                menu.SEPARATOR,
                item(
                    self.display["values"]["sahayika"],
                    menu(
                        item(
                            self.display["on"],
                            lambda _: val.exec_taskbar_commands("sg_on"),
                            checked=lambda item: self.sg == True,
                            radio=True,
                        ),
                        item(
                            self.display["off"],
                            lambda _: val.exec_taskbar_commands("sg_off"),
                            checked=lambda item: self.sg == False,
                            radio=True,
                        ),
                    ),
                ),
                item(self.display["values"]["typing_lang_main"], langs),
                item(
                    self.display["menu_values"]["encoding_table"],
                    lambda x: val.open_img(),
                ),
                menu.SEPARATOR,
                item(
                    "💻" + self.display["tray"]["show"],
                    lambda _: val.exec_taskbar_commands("show"),
                ),
                item("❌ " + self.display["tray"]["exit"], lambda k: self.close()),
            )

        def close(self, k=False):
            if not k:
                alert(
                    self.display["exit_msg"],
                    color="red",
                    lapse=500,
                    geo=True,
                    wait=True,
                )
            self.systray.visible = False
            self.systray.stop()

        def __update_values(self):
            sam = self.val.get("sandesh")
            for x in sam:
                if x == "sg":
                    self.sg = self.val.get("sg_status")
                elif x == "lang":
                    self.lang = self.val.get("lang")
                elif x == "ks":
                    self.ks = val.get("ks")
                elif x == "app_lang":
                    self.display = self.display = val.get("display_data")
                    self.systray.menu = self.__menu_object()
                    self.systray.title = self.val.get("title_text")
                    self.systray._update_title()
                elif x == "title":
                    self.systray.title = val.get("title_text")
                    self.systray._update_title()
                elif x == "close":
                    self.close()
                    return
                elif x == "close_just":
                    self.close(True)
                    return
            val.get("reset_sandesh")
            self.systray.update_menu()

        def __check_value_updates(self):
            while True:
                a = self.val.get("get_val_change")[0]
                if a:
                    self.__update_values()
                    self.val.get("set_val_change", 0)
                else:
                    sleep(0.5)

    dbg = False
    try:
        args = sys.argv[-1]
        if args == "doShAnusandhAna":
            dbg = True
    except:
        pass

    val = Main(dbg)
    tsk = TaskBar()
    key = kuYjikolambhikam(val)
    tsk.init(val)

    if not val.debug:
        start_thread(lambda: update_win(tsk))
    tsk.systray.run()
