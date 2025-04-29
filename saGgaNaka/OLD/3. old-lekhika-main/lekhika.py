from multiprocessing.managers import BaseManager
from infi.systray import SysTrayIcon
from threading import Thread
from pratidarshan import (
    Design,
    Tk,
    alert,
    get_registry,
    get_str_reg,
    lang_code,
    ajay,
    Suggestion,
    startfile,
    ver
)
from multiprocessing import Process, freeze_support
from sys import argv
from kuJjikopalambhan import kuYjikolambhikam


class Main:
    def __init__(self):
        self.ks = get_registry("app_status")
        self.sg_status = bool(get_registry("sg_st") - 1)
        self.msg = set([])
        self.lang_mode = get_str_reg("typ_lang")
        self.temp = self.ks
        th_tk = Thread(target=self.start_tk, name="TK")
        th_tk.daemon = True
        self.window_start_status = get_registry("window_start")
        self.first = True
        self.tk_status = False
        self.sa_lang = get_registry("sa_mode")
        th_tk.start()
        self.sg = Suggestion(self)

    def give_startup_msg(self):
        text = (
            "Lipi Lekhika Started:\nApp ➠ Turned {0}\nTyping "
            "Script ➠ {1}\nSanskrit Mode ➠ Turned {2}.\nYou Can accces App from Taskbar Icon\nEven "
            "after closing main App Window.\nPress Ctrl+F1 to start This Directly"
            ".".format(
                ("Off", "On")[self.ks],
                lang_code[1][self.lang_mode],
                {1: "On", 0: "Off"}.get(get_registry("sa_mode")),
            )
        )
        alert(text, color="green", lapse=4200, geo=True, AkAra=14)

    def get(self, name, val=0):
        if name == "ks":
            return self.ks
        elif name == "first":
            a = self.first
            self.first = False
            return a
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
        elif name == "show_status":
            alert(
                "Language ➠ {0}\nApp ➠ {1}\nSanskrit Mode ➠ {2}".format(
                    self.r.typing_lang.get(),
                    {0: "Off", 1: "On"}[self.ks],
                    {0: "Off", 1: "On"}[self.sa_lang],
                ),
                color="brown",
                lapse=1250,
                geo=True,
                AkAra=16,
            )
        elif name == "change_less":
            self.change(True, True)
        elif name == "msg":
            return self.msg
        elif name == "startup_msg":
            self.give_startup_msg()
        elif name == "sa":
            return self.sa_lang
        elif name == "lang":
            return self.lang_mode
        elif name == "update_sans":
            self.r.update_sans_mode(1, val)
        elif name == "set_typ_lang":
            self.r.typing_lang.set(val)
        elif name == "null_msg":
            self.msg = set([])

    def exec_taskbar_commands(self, n, m=True):
        if n == "show":
            self.r.display("show")
        elif n == "sa_update":
            self.r.update_sans_mode(2)
        elif n == "options":
            self.r.display("options")
        elif n == "sg":
            self.msg.add("sg")
            self.sg_status = not self.sg_status
            if m:
                self.r.sg.set(int(self.sg_status))
        elif n == "close_set_false":
            self.close_status = True
        elif n == "quit":
            self.close()

    def update_typ_lang(self, l):
        self.lang_mode = l
        self.msg.add("change_lang")
        self.get("set_typ_lang", lang_code[1][l])
        t = "ajay➠" + ajay[lang_code[0][self.r.typing_lang.get()]]
        self.r.ajay0.configure(text=t[:-1])
        self.r.ajay1.configure(text=t)
        alert(
            "Typing Language Changed To " + l,
            color="green",
            lapse=1200,
        )

    def open_img(self):
        self.r.open_img()

    def close(self, ev=False):
        if self.close_status:
            return
        else:
            self.close_status = True
            alert("लिपि लेखिका Closed", color="red", lapse=500, geo=True)

    def start_tk(self):
        self.master = Tk()
        self.r = Design(self, self.master)
        self.master.mainloop()

    def change(self, n=False, less=False):
        if n:
            self.ks = abs(self.ks - 1)
            self.r.karyAsthiti.set(self.ks)
        else:
            self.ks = self.r.karyAsthiti.get()
        if self.temp == self.ks:
            return
        if self.ks == 0:
            self.r.ex = True
        self.temp = self.ks
        if not less:
            self.msg.add("update_ks")
            self.msg.add("clear_vals")
        alert(
            {1: self.r.l_data["turned_on"], 0: self.r.l_data["turned_off"]}.get(self.ks)
        )


error_checkup = False
if len(argv) > 1:
    if argv[-1] == "truTInupalambhayatu":
        import truTyupalambhikA

        error_checkup = True

if __name__ == "__main__" and not error_checkup:
    freeze_support()

    class KeyProcessManager:
        def __init__(self, v):
            self.v = v
            self.exit = True

        def start(self):
            self.process = Process(target=kuYjikolambhikam, args=(self.v,))
            self.process.daemon = True
            self.process.start()
            self.process.join()
            if self.exit:
                global systray
                systray.shutdown()
            elif not self.exit:
                self.exit = True

        def restart(self, ev):
            self.exit = False
            self.process.kill()
            th = Thread(target=self.start)
            th.daemon = True
            th.start()
            alert("Restarted", color="purple")

    BaseManager.register("Main", Main)
    m = BaseManager()
    m.start()
    val = m.Main()
    k = KeyProcessManager(val)
    th = Thread(target=k.start)
    th.daemon = True
    th.start()
    close_status = False

    def qiut(ev):
        global close_status
        if close_status:
            return
        alert("Lipi Lekhika Closed", color="red", lapse=500, geo=True, wait=True)
        close_status = True

    menu_options = (
        ("Show Window", None, lambda _: val.exec_taskbar_commands("show")),
        ("Turn On/Off", None, lambda _: val.change(True)),
        (
            "Turn Sanskrit Mode On/Off",
            None,
            lambda _: val.exec_taskbar_commands("sa_update"),
        ),
        ("Options", None, lambda _: val.exec_taskbar_commands("options")),
        ("Show/Hide Suggestions", None, lambda _: val.exec_taskbar_commands("sg")),
        (
            "Change Typing Language",
            None,
            (
                ("Brahmi", None, lambda _: val.update_typ_lang("Brahmi")),
                ("Modi", None, lambda _: val.update_typ_lang("Modi")),
                ("Sharada", None, lambda _: val.update_typ_lang("Sharada")),
                ("Romanized", None, lambda _: val.update_typ_lang("Romanized")),
                ("Urdu", None, lambda _: val.update_typ_lang("Urdu")),
                ("Punjabi", None, lambda _: val.update_typ_lang("Punjabi")),
                ("Nepali", None, lambda _: val.update_typ_lang("Nepali")),
                ("Assamese", None, lambda _: val.update_typ_lang("Assamese")),
                ("Konkani", None, lambda _: val.update_typ_lang("Konkani")),
                ("Odia", None, lambda _: val.update_typ_lang("Oriya")),
                ("Kannada", None, lambda _: val.update_typ_lang("Kannada")),
                ("Malayalam", None, lambda _: val.update_typ_lang("Malayalam")),
                ("Sanskrit", None, lambda _: val.update_typ_lang("Sanskrit")),
                ("Gujarati", None, lambda _: val.update_typ_lang("Gujarati")),
                ("Marathi", None, lambda _: val.update_typ_lang("Marathi")),
                ("Tamil", None, lambda _: val.update_typ_lang("Tamil")),
                ("Telugu", None, lambda _: val.update_typ_lang("Telugu")),
                ("Bengali", None, lambda _: val.update_typ_lang("Bengali")),
                ("Hindi", None, lambda _: val.update_typ_lang("Hindi")),
            ),
        ),
        ("View Encoding Table", None, lambda x: val.open_img()),
        ("Restart", None, k.restart),
    )
    systray = SysTrayIcon(
        "assets\\Icon.ico",
        "Lipi Lekhika",
        menu_options,
        default_menu_index=1,
        on_quit=qiut,
    )
    val.exec_taskbar_commands("close_set_false")

    def update():
        from urllib.request import urlopen

        ver1 = 0
        try:
            o = urlopen("https://rebrand.ly/lipiupdate")
            ver1 = float(o.read().decode("utf-8"))
        except:
            pass
        if ver1 > ver:
            startfile(r"assets\updatewebsite.url")
            alert(
                "New Version Of Lipi Lekhika is available.\nPlease Download Latest version from lipilekhika.com",
                color="red",
                lapse=9000,
                geo=True,
                AkAra=17,
            )

    y = Thread(target=update)
    y.daemon = True
    y.start()
    systray.start()
