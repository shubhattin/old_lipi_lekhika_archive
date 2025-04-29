from keyboard import add_hotkey, on_press, on_release_key
from mouse import on_click, on_middle_click, on_right_click
from convert import parivartana
from infi.systray import SysTrayIcon
from threading import Thread
from os import startfile
from time import time
from Design import (
    Design,
    Tk,
    LEFT,
    alert,
    get_registry,
    store_registry,
    get_str_reg,
    lang_code,
)

class Main:
    def __init__(self):
        self.ks = get_registry("app_status")
        self.ds = 0
        self.lang_mode = get_str_reg("typ_lang")
        self.last_time = time()
        self.temp = self.ks
        self.window_start_status = get_registry("window_start")
        self.ctrl_press_status = False
        self.main = parivartana(self)
        self.main.devanAgari_saMkhyA = bool(self.ds)
        self.small2capital = False
        th_tk = Thread(target=self.start_tk)
        th_tk.daemon = True
        self.tk_start_status = False
        self.start_all_listeners()
        self.start_taskbar()
        th_tk.start()
        if get_registry("prathamakAlaH") == 0:
            startfile(r"assets\nirm.ttf")
            alert(
                "Please Install this Font which popped up now,\nFor Proper "
                "Functioning of this App.\nIt's required to be installed only once.",
                color="purple",
                lapse=5000,
                geo=True,
                AkAra=19,
            )
            store_registry(1, "prathamakAlaH")
        text = (
            "देवनागरी लेखिका Started:\nApp Status = Turned {0}\nTyping "
            "Script = {1}\nSanskrit Mode = Turned {2}.\nYou Can accces App from Taskbar Icon\nEven "
            "after closing main App Window.\nPress Shift+F1 to start This Directly"
            ".".format(
                ("Off", "On")[self.ks],
                lang_code[1][self.lang_mode],
                {1: "On", 0: "Off"}.get(get_registry("sa_mode")),
            )
        )
        alert(text, color="green", lapse=4200, geo=True, AkAra=14)
        self.tk_start_status = True

    def start_taskbar(self):
        menu_options = (
            ("Show Window", None, lambda _: self.r.display("show")),
            ("Turn On/Off", None, lambda _: self.change(True)),
            ("Turn Sanskrit Mode On/Off", None, lambda _: self.r.update_sans_mode(2)),
            ("Options", None, lambda _: self.r.display("options")),
            ("About", None, lambda _: self.r.display("about")),
            (
                "Change Typing Script",
                None,
                (
                    ("IAST", None, lambda _: self.main.set_typing_lang("ia", 2)),
                    ("Assamese", None, lambda _: self.main.set_typing_lang("as", 2)),
                    ("Punjabi", None, lambda _: self.main.set_typing_lang("pn", 2)),
                    ("Odia", None, lambda _: self.main.set_typing_lang("or", 2)),
                    ("Malayalam", None, lambda _: self.main.set_typing_lang("ma", 2)),
                    ("Gujarati", None, lambda _: self.main.set_typing_lang("gu", 2)),
                    ("Kannada", None, lambda _: self.main.set_typing_lang("ka", 2)),
                    ("Bengali", None, lambda _: self.main.set_typing_lang("be", 2)),
                    ("Telugu", None, lambda _: self.main.set_typing_lang("te", 2)),
                    ("Tamil", None, lambda _: self.main.set_typing_lang("ta", 2)),
                    ("Devanagari", None, lambda _: self.main.set_typing_lang("de", 2)),
                ),
            ),
            ("View Encoding Table", None, self.open_img)
        )
        self.systray = SysTrayIcon(
            "assets\\Icon.ico",
            self.taskbar_text(),
            menu_options,
            default_menu_index=1,
            on_quit=self.close,
        )
        self.close_status = False
        self.systray.start()

    def open_img(self, event):
        self.r.open_img()

    def close(self, ev):
        if self.close_status:
            return
        alert("देवनागरी लेखिका Closed", color="red", lapse=500, geo=True)
        self.close_status = True

    def start_all_listeners(self):
        add_hotkey("windows+z", lambda: self.change(True), timeout=2)
        add_hotkey("windows+z+esc", lambda: self.systray.shutdown(), timeout=2)
        on_press(self.detect_key)
        on_release_key("ctrl", self.set_ctrl)
        on_release_key("windows", self.set_ctrl)
        add_hotkey("shift+f4", lambda: self.change_num(True), timeout=2)
        on_click(lambda: self.main.clear_all_val(True))
        on_middle_click(lambda: self.main.clear_all_val(True))
        on_right_click(lambda: self.main.clear_all_val(True))

    def start_tk(self):
        self.master = Tk()
        self.r = Design(self, self.master)
        self.master.mainloop()

    def set_ctrl(self, c):
        self.ctrl_press_status = False

    def detect_key(self, key, already_ready=False):
        if time() - self.last_time > 60:
            self.main.clear_all_val()
            if time() - self.last_time > 300:
                if self.ks == 1:
                    self.change(True)
                self.last_time = time()
                return
            self.last_time = time()
        if self.ks == 0:
            return
        if not already_ready:
            try:
                key = key.char
            except AttributeError:
                key = key.name
        if key == None:
            return
        elif self.small2capital:
            if time() - self.time_temp <= 2.5 and key == ",":
                self.small2capital = False
                self.main.small_to_capital = True
                self.main.convert_small_to_big()
            else:
                self.small2capital = False
                self.main.clear_all_val(True)
                self.detect_key(key, already_ready=True)
        elif "ctrl" in key or "windows" in key:
            self.ctrl_press_status = True
        elif "shift" in key or "caps" in key or self.ctrl_press_status:
            pass
        elif key in "1234567890":
            if self.ds == 1 or self.check_num(self.main.next_chars):
                self.main.prakriyA(key)
        else:
            self.main.prakriyA(key)

    def check_num(self, st):
        for x in "1234567890":
            if x in st:
                return True
        return False

    def change(self, n=None):
        if n:
            self.ks = abs(self.ks - 1)
            if self.start_tk:
                self.r.karyAsthiti.set(self.ks)
        else:
            self.ks = self.r.karyAsthiti.get()
        if self.temp == self.ks:
            return
        if self.ks == 0:
            self.r.ex = True
            self.r.num.pack_forget()
        else:
            self.r.num.pack(side=LEFT)
        self.temp = self.ks
        self.systray.update(hover_text=self.taskbar_text())
        alert(
            {1: self.r.l_data["turned_on"], 0: self.r.l_data["turned_off"]}.get(self.ks)
        )
        self.main.clear_all_val(True)

    def change_num(self, n=None):
        if n:
            self.ds = abs(self.ds - 1)
            self.r.dev_saMkyA.set(self.ds)
        else:
            self.ds = self.r.dev_saMkyA.get()
        self.main.devanAgari_saMkhyA = bool(self.ds)
        self.systray.update(hover_text=self.taskbar_text())
        alert(
            {1: self.r.l_data["dev_num_on"], 0: self.r.l_data["dev_num_off"]}.get(
                self.ds
            )
        )

    def taskbar_text(self) -> str:
        try:
            a = lang_code[2][lang_code[0][self.r.typing_lang.get()]]
            b = {1: "On.", 0: "Off."}.get(self.r.sanskrit_mode.get())
        except AttributeError:
            a = lang_code[2][self.lang_mode]
            b = {1: "On.", 0: "Off."}.get(get_registry("sa_mode"))
        return (
            "Devanagari Lekhika is " + {1: "On", 0: "Off"}.get(self.ks) + "\n"
            "Typing Script is " + a + "\nSanskrit mode is " + b
        )


App = Main()
