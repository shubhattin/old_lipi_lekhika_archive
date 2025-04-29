from tkinter import (
    Canvas,
    Frame,
    IntVar,
    Menu,
    Toplevel,
    Tk,
    NW,
    Menubutton,
    Checkbutton,
    StringVar,
)
import tkinter.ttk as ttk
from tkinter.constants import CENTER, DISABLED, END, INSERT, NORMAL
from tkinter.font import Font
from os import startfile
from winregistry import WinRegistry
from dattAMsh import (
    akSharAH,
    lang_code,
    DISPLAY_DATA,
    display_lang_lists,
    bhAShAH,
    AJAY,
    bhAShAH_img,
    IMAGE_DB,
)
import pprint
from mouse import get_position
from json import dumps
from threading import Thread
from copy import deepcopy
from PIL import Image, ImageTk

ver = 2.0
lengths = [[], []]
for x in range(0, len(lang_code[2])):
    lengths[1].append(x)
for x in range(0, len(display_lang_lists)):
    lengths[0].append(x)


def start_file(f):
    def s():
        startfile(f)

    a = Thread(target=s)
    a.daemon = True
    a.start()


def get_registry(name):
    reg = WinRegistry()
    path = r"HKCU\SOFTWARE\lekhika"
    try:
        a = int(reg.read_value(path, name)["data"])
        err = False
        if name in ("app_status", "sa_mode", "sg_st", "window_start") and a not in (
            0,
            1,
        ):
            err = True
        elif name == "language" and (a not in lengths[0]):
            err = True
        elif name == "typ_lang" and (a not in lengths[1]):
            err = True
        if err:
            raise FileNotFoundError
        return a
    except:
        store_registry(0 if name != "sg_st" else 1, name)
        return get_registry(name)


def store_registry(value, name):
    reg = WinRegistry()
    path = r"HKCU\SOFTWARE\lekhika"
    if "lekhika" not in reg.read_key(r"HKCU\SOFTWARE")["keys"]:
        reg.create_key(path)
    reg.write_value(path, name, str(value).encode("ascii"), "REG_BINARY")


def alert(msg, color, AkAra=19, geo=None, lapse=0, wait=False, bg=None):
    def s(msg, color, lapse, geo, AkAra, bgi):
        master = Tk()
        master.overrideredirect(True)
        a = Frame(master, highlightbackground="brown", highlightthickness=3)
        style = ttk.Style(master)
        if bgi != None:
            style.configure(
                "A.TLabel",
                font=("Nirmala UI", AkAra, "bold"),
                foreground=color,
                background=bgi,
            )
        else:
            style.configure(
                "A.TLabel", font=("Nirmala UI", AkAra, "bold"), foreground=color
            )
        sd = ttk.Label(a, text=msg, style="A.TLabel", justify=CENTER)
        sd.pack()
        a.pack()
        master.title("")
        if geo == None:
            master.geometry("+20+10")
        else:
            master.eval("tk::PlaceWindow . center")
        master.attributes("-topmost", True)
        master.update()
        master.after(650 + lapse, master.destroy)
        master.mainloop()

    lapse += 650
    if wait:
        s(msg, color, lapse, geo, AkAra, bg)
        return
    a = Thread(target=s, args=(msg, color, lapse, geo, AkAra, bg))
    a.daemon = True
    a.start()


class pradarshanam:
    def __init__(self, m):
        self.main_object = m

    def prArambh(self):
        self.root = Tk()
        return self

    def init(self):
        main_obj = self.main_object
        self.ex = False
        self.centred = False
        self.style = ttk.Style(self.root)
        self.advanced_window_data_preperation = False
        self.root.wm_withdraw()
        self.img_window_status = False
        sdf = get_registry("language")
        self.language = StringVar(self.root, display_lang_lists[sdf])
        self.l_data = DISPLAY_DATA[self.language.get()]
        self.display_values = {}
        self.root.bind("<Control-q>", lambda s: self.open_img())
        for x in self.l_data["values"]:
            self.display_values[x] = StringVar(self.root, self.l_data["values"][x])
        b = lang_code[1][self.main_object.lang_mode]
        self.karyAsthiti = self.main_object.ks
        a = self.main_object.sa_lang
        self.typing_lang = StringVar(self.root, value=b)
        self.sanskrit_mode = IntVar(self.root, value=a)
        self.ajay_texts = [StringVar(self.root), StringVar(self.root)]
        t = "ajay➠" + AJAY[lang_code[0][self.typing_lang.get()]]
        self.ajay_texts[0].set(t[:-1])
        self.ajay_texts[1].set(t)
        self.option_values = {
            "startup": IntVar(self.root, value=main_obj.window_start_status),
            "app": IntVar(self.root, main_obj.ks),
            "typing": StringVar(self.root, value=b),
            "sg": IntVar(self.root, self.main_object.sg_status),
        }
        self.root.resizable(False, False)
        self.root.iconbitmap(r"resources\Icon.ico")
        self.root.title(self.l_data["app_title"])
        self.__top_frame()
        self.__input_frame()
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.hide(True))
        self.kAryaM.configure(image=self.image[self.karyAsthiti])
        self.sg_button.configure(image=self.image1[int(main_obj.sg_status)])
        about_img = ImageTk.PhotoImage(Image.open(IMAGE_DB["about"]))
        self.m.menu.entryconfigure(2, image=self.image[0], selectimage=self.image[1])
        self.m.menu.entryconfigure(3, image=self.image1[0], selectimage=self.image1[1])
        self.m.menu.entryconfigure(4, image=self.image1[0], selectimage=self.image1[1])
        self.m.menu.entryconfigure(8, image=about_img)
        fh = ImageTk.PhotoImage(Image.open(IMAGE_DB["menu"]))
        self.m.configure(image=fh)
        i = ImageTk.PhotoImage(master=self.root, image=Image.open(IMAGE_DB["usage"]))
        self.usage_btn.configure(image=i)
        lang_img = ImageTk.PhotoImage(Image.open(IMAGE_DB["lang"]))
        ttk.Label(self.top_frame, image=lang_img).grid(row=0, column=3, sticky=NW)
        if main_obj.window_start_status == 0:
            self.root.wm_deiconify()
            self.root.eval("tk::PlaceWindow . center")
            self.centred = True
            self.root.attributes("-topmost", True)
            self.root.after(600, lambda: self.root.attributes("-topmost", False))
        else:
            main_obj.give_startup_msg()
        self.root.update()
        main_obj.tk_status = True
        self.root.mainloop()

    def __top_frame(self):
        self.top_frame = Frame(self.root)
        ttk.Label(self.top_frame, text=" " * 5).grid(row=0, column=1, sticky=NW)
        self.style.configure(
            "B.TMenubutton",
            font=("Nirmala UI", 8, "bold"),
            foreground="purple",
            background="white",
        )
        self.usage_btn = ttk.Label(self.top_frame, compound="left", text="   ")
        self.usage_btn.bind("<Button-1>", lambda s: self.open_img())
        self.usage_btn.grid(row=0, column=2, sticky=NW)
        ad = list(deepcopy(display_lang_lists))[::-1]
        ad.append("")
        ad = ad[::-1]
        frame1 = Frame(
            self.top_frame, highlightbackground="black", highlightthickness=1
        )
        bhASA = ttk.OptionMenu(
            frame1,
            self.language,
            *ad,
            style="B.TMenubutton",
            command=self.update_lang_data,
        )
        bhASA.grid(row=0, column=0, stick=NW)
        frame1.grid(row=0, column=4, stick=NW)
        bhASA["menu"].config(font=("Nirmala UI", (8), "bold"), fg="red")
        ttk.Label(self.top_frame, text=" " * 7).grid(row=0, column=5, sticky=NW)
        self.style.configure(
            "A.TButton",
            font=("Nirmala UI", 9, "bold"),
            foreground="red",
            background="black",
        )
        ttk.Button(
            self.top_frame,
            style="A.TButton",
            compound="left",
            textvariable=self.display_values["background_run"],
            command=self.hide,
        ).grid(row=0, column=6, sticky="ne")
        ttk.Label(self.top_frame, text="    ").grid(row=0, column=7, sticky="ne")
        self.top_frame.grid(row=0, sticky=NW)
        self.__menu_kAraH()

    def __menu_kAraH(self):
        self.m = Menubutton(self.top_frame)
        self.m.menu = Menu(self.m, tearoff=False)
        self.m["menu"] = self.m.menu
        self.menu_values = self.l_data["menu_values"]
        font1 = Font(family="Nirmala UI", weight="bold", size=8)
        self.m.menu.add_command(
            label=self.menu_values["default"],
            foreground="#3a2e2e",
            activeforeground="yellow",
            font=Font(family="Nirmala UI", weight="bold", size=11),
        )
        nested = Menu(self.m.menu, tearoff=False)
        for x in bhAShAH[::-1]:
            nested.add_radiobutton(
                label=x,
                value=x,
                variable=self.option_values["typing"],
                font=Font(family="Nirmala UI", weight="bold", size=9),
                foreground="#8b0000",
                activeforeground="yellow",
                command=lambda: store_registry(
                    lang_code[2].index(
                        lang_code[0][self.option_values["typing"].get()]
                    ),
                    "typ_lang",
                ),
            )
        self.m.menu.add_cascade(
            label=self.menu_values["typing_lang"],
            menu=nested,
            font=font1,
            activeforeground="yellow",
            foreground="purple",
            background="#e8f5bf",
        )
        self.m.menu.add_checkbutton(
            variable=self.option_values["app"],
            indicatoron=False,
            background="#e8f5bf",
            foreground="green",
            command=lambda: store_registry(
                self.option_values["app"].get(), "app_status"
            ),
        )
        self.m.menu.add_checkbutton(
            label=self.menu_values["sahayika"],
            compound="left",
            variable=self.option_values["sg"],
            indicatoron=False,
            font=font1,
            activeforeground="yellow",
            background="#e8f5bf",
            foreground="blue",
            command=lambda: store_registry(self.option_values["sg"].get(), "sg_st"),
        )
        self.m.menu.add_checkbutton(
            label=self.menu_values["startup"],
            variable=self.option_values["startup"],
            onvalue=0,
            activeforeground="yellow",
            offvalue=1,
            background="#e8f5bf",
            compound="left",
            font=Font(family="Nirmala UI", weight="bold", size=7),
            foreground="brown",
            indicatoron=False,
            command=lambda: store_registry(
                self.option_values["startup"].get(), "window_start"
            ),
        )
        self.m.menu.add_separator()
        self.m.menu.add_separator()
        self.m.menu.add_command(
            label=self.menu_values["normal_version"],
            command=lambda: start_file("samanya.exe"),
            foreground="purple",
            background="#faf9ae",
            activeforeground="yellow",
            font=Font(family="Nirmala UI", weight="bold", size=8),
        )
        self.m.menu.add_command(
            label="  " + self.menu_values["about"],
            command=lambda: self.__about_window(),
            compound="left",
            background="#fdfdd6",
            foreground="green",
            activeforeground="yellow",
            font=font1,
        )
        self.m.grid(row=0, column=0, sticky="nw")

    def __input_frame(self):
        command_frame = Frame(self.root)
        self.image = (
            ImageTk.PhotoImage(Image.open(IMAGE_DB["off"])),
            ImageTk.PhotoImage(Image.open(IMAGE_DB["on"])),
        )
        self.kAryaM = ttk.Label(command_frame)
        self.kAryaM.grid(row=0, column=0, sticky=NW)
        self.kAryaM.bind(
            "<Button-1>", lambda x: self.main_object.change(True, False, True)
        )
        ttk.Label(command_frame, text=" " * 20).grid(row=0, column=1, sticky=NW)
        self.style.configure(
            "SA.TRadiobutton", font=("Nirmala UI", 9, "bold"), background="lightblue"
        )
        ttk.Radiobutton(
            command_frame,
            textvariable=self.ajay_texts[0],
            value=0,
            style="SA.TRadiobutton",
            variable=self.sanskrit_mode,
            command=self.update_sans_mode,
        ).grid(row=0, column=2, sticky=NW)
        ttk.Radiobutton(
            command_frame,
            textvariable=self.ajay_texts[1],
            value=1,
            style="SA.TRadiobutton",
            variable=self.sanskrit_mode,
            command=self.update_sans_mode,
        ).grid(row=0, column=3, sticky=NW)
        command_frame.grid(row=2, column=0, sticky=NW)
        frame = ttk.Frame(self.root)
        self.style.configure(
            "TYP.TLabel", font=("Nirmala UI", 12, "bold"), foreground="brown"
        )
        ttk.Label(
            frame,
            style="TYP.TLabel",
            textvariable=self.display_values["typing_lang_main"],
        ).grid(row=0, column=0, sticky=NW)
        frame1 = Frame(frame, highlightbackground="black", highlightthickness=1)
        self.style.configure(
            "A.TMenubutton",
            font=("Nirmala UI", 10, "bold"),
            foreground="green",
            background="white",
        )
        asd = deepcopy(bhAShAH)
        asd.append("")
        asd = asd[::-1]
        sd = ttk.OptionMenu(
            frame1,
            self.typing_lang,
            *asd,
            style="A.TMenubutton",
            command=lambda s: self.main_object.update_typ_lang(
                self.typing_lang.get(), True
            ),
        )
        sd.grid(row=0, column=1, stick=NW)
        frame1.grid(row=0, column=1, stick=NW)
        sd["menu"].config(font=("Nirmala UI", 10, "bold"), fg="red", bg="#faf9ae")
        self.image1 = (
            ImageTk.PhotoImage(Image.open(IMAGE_DB["off1"])),
            ImageTk.PhotoImage(Image.open(IMAGE_DB["on1"])),
        )
        ttk.Label(frame, text=" " * 4).grid(row=0, column=2, sticky=NW)
        self.sg_button = ttk.Label(frame)
        self.sg_button.grid(row=0, column=3, sticky=NW)
        self.sg_button.bind(
            "<Button-1>", lambda x: self.main_object.exec_taskbar_commands("sg", False)
        )
        self.style.configure(
            "sah.TLabel", font=("Nirmala UI", 11, "bold"), foreground="blue"
        )
        hl = ttk.Label(
            frame, textvariable=self.display_values["sahayika"], style="sah.TLabel"
        )
        hl.grid(row=0, column=4, sticky=NW)

        def sg_label_click():
            self.style.configure("sah.TLabel", foreground="black")
            self.root.after(
                300, lambda: self.style.configure("sah.TLabel", foreground="blue")
            )
            self.main_object.exec_taskbar_commands("sg", False)

        hl.bind("<Button-1>", lambda x: sg_label_click())
        frame.grid(row=3, column=0, sticky=NW)
        self.style.configure(
            "ins.TLabel", font=("Nirmala UI", 10, "bold"), foreground="purple"
        )
        ttk.Label(
            self.root,
            style="ins.TLabel",
            textvariable=self.display_values["instructions"],
        ).grid(row=4, column=0, sticky=NW)

    def update_sans_mode(self, mannual=0, v=0):
        if mannual == 1:  # from lang change
            self.sanskrit_mode.set(v)
            self.main_object.sa_lang = v
        else:
            self.main_object.sa_lang = self.sanskrit_mode.get()
        self.main_object.msg.add("update_sa")
        self.main_object.value_change[1] = True

    def __about_window(self):
        about = Toplevel(self.root)
        about.title(self.l_data["about_title"])
        about.geometry("+140+70")
        about.wm_withdraw()
        about.resizable(False, False)
        about.iconbitmap(r"resources\Icon.ico")
        self.style.configure(
            "about.TLabel", font=("Nirmala UI", 11, "bold"), foreground="brown"
        )
        self.style.configure(
            "email.TLabel", font=("Nirmala UI", 10, "bold"), foreground="green"
        )
        ttk.Label(
            about,
            textvariable=self.display_values["app_description"],
            style="about.TLabel",
            justify=CENTER,
        ).pack()
        ttk.Label(
            about, text="Email :- shubhamanandgupta@outlook.com", style="email.TLabel"
        ).pack()
        self.display_values["version"].set(
            self.display_values["version"].get().format(ver)
        )
        self.style.configure(
            "ver.TLabel", font=("Nirmala UI", 11, "bold"), foreground="red"
        )
        ttk.Label(
            about, textvariable=self.display_values["version"], style="ver.TLabel"
        ).pack()
        self.style.configure(
            "bh.TLabel", font=("Nirmala UI", 11, "bold"), foreground="blue"
        )
        ttk.Label(about, text="भारते रचितः", style="bh.TLabel").pack()
        about.wm_deiconify()
        about.mainloop()

    def update_img_win(self):
        self.img_window_status = False
        self.img_win.destroy()

    def open_img(self):
        self.img_on_top_status = False

        def change_img_top():
            self.img_on_top_status = not self.img_on_top_status
            self.img_win.attributes("-topmost", self.img_on_top_status)

        if self.img_window_status:
            self.img_win.wm_deiconify()
            return
        self.img_win = Toplevel(self.root)
        self.img_win.wm_withdraw()
        self.img_win.title("परिवर्तनसूच्यः")
        self.img_win.geometry("+{0}+0".format(int(self.root.winfo_screenwidth() - 600)))
        self.img_win.protocol("WM_DELETE_WINDOW", self.update_img_win)
        self.img_win.iconbitmap(r"resources\Icon.ico")
        image_collection = {}
        for v in bhAShAH_img:
            try:
                a = lang_code[0][v]
                if a in ["Sanskrit", "Nepali", "Konkani", "Marathi"]:
                    a = "Hindi"
                if a == "Kashmiri":
                    a = "Urdu"
                image_collection[v] = ImageTk.PhotoImage(
                    Image.open("resources\\img\\lang\\" + a + ".png")
                )
            except:
                pass
        try:
            image_collection["Vedic"] = ImageTk.PhotoImage(
                Image.open("resources\\img\\lang\\Vedic.png")
            )
        except:
            pass
        fr = ttk.Frame(self.img_win)
        lang = StringVar(self.img_win, value=self.typing_lang.get())
        self.style.configure(
            "B.TMenubutton",
            font=("Nirmala UI", 10, "bold"),
            background="white",
            foreground="green",
        )
        im = deepcopy(bhAShAH_img)[::-1]
        im.append("")
        im = im[::-1]
        frame1 = Frame(fr, highlightbackground="brown", highlightthickness=1)
        bhASAd = ttk.OptionMenu(
            frame1,
            lang,
            *im,
            style="B.TMenubutton",
            command=lambda _: sUchI.configure(image=image_collection[lang.get()]),
        )
        bhASAd.grid(row=0, column=0, stick=NW)
        frame1.grid(row=0, column=0, stick=NW)
        bhASAd["menu"].config(font=("Nirmala UI", (10), "bold"), fg="red", bg="#faf9ae")
        ck_btn = IntVar(self.img_win, 0)
        Checkbutton(
            fr,
            variable=ck_btn,
            offvalue=0,
            onvalue=1,
            textvariable=self.display_values["pin_top"],
            command=change_img_top,
            fg="purple",
            font=("Nirmala UI", 10, "bold"),
        ).grid(row=0, column=1, sticky=NW)
        fr.grid(row=0, column=0, sticky=NW)
        self.img_win.resizable(False, False)
        self.img_window_status = True
        self.style.configure(
            "SUC.TLabel", font=("Nirmala UI", 12, "bold"), foreground="green"
        )
        ttk.Label(
            self.img_win,
            textvariable=self.display_values["sUchI_msg"],
            style="SUC.TLabel",
            justify=CENTER,
        ).grid(row=1, column=0, sticky="n")
        self.style.configure("kl.TLabel", padding=5)
        sUchI = ttk.Label(
            self.img_win, image=image_collection[lang.get()], style="kl.TLabel"
        )
        sUchI.grid(row=2, column=0, sticky=NW)
        self.style.configure(
            "N.TLabel", font=("Nirmala UI", 9, "bold"), foreground="brown"
        )
        ttk.Label(
            self.img_win, textvariable=self.display_values["nirdesh"], style="N.TLabel"
        ).grid(row=3, column=0, sticky=NW)
        self.img_win.wm_deiconify()
        self.img_win.attributes("-topmost", True)
        self.img_win.after(2300, lambda: self.img_win.attributes("-topmost", False))
        self.root.after(20, lambda: self.img_win.mainloop())

    def hide(self, event=None):
        self.root.wm_withdraw()
        if self.main_object.tk_status:
            if event == True:
                self.main_object.sandesh.add("close")
                self.main_object.value_change[0] = True
            else:
                alert(
                    self.l_data["hide2"],
                    color="purple",
                    lapse=1800,
                    geo=True,
                    AkAra=13,
                )

    def display(self, t):
        if t == "show":
            self.root.wm_deiconify()
            if not self.centred:
                self.root.after(20, lambda: self.root.eval("tk::PlaceWindow . center"))
                self.centred = True
            self.root.attributes("-topmost", True)
            self.root.after(1300, lambda: self.root.attributes("-topmost", False))

    def update_lang_data(self, event):
        def set_text():
            for x in self.l_data["values"]:
                self.display_values[x].set(self.l_data["values"][x])
            self.root.title(self.l_data["app_title"])
            self.main_object.sg.set_extra_values()
            self.menu_values = self.l_data["menu_values"]
            loc = (
                "default",
                "typing_lang",
                None,
                "sahayika",
                "startup",
                None,
                None,
                "normal_version",
                "about",
            )
            for x in range(len(loc)):
                if loc[x] == None:
                    continue
                self.m.menu.entryconfigure(x, label=self.menu_values[loc[x]])
                self.m.update()

        self.ex = True
        a = display_lang_lists.index(self.language.get())
        self.l_data = DISPLAY_DATA[self.language.get()]
        store_registry(a, "language")
        set_text()
        self.display_values["version"].set(
            self.display_values["version"].get().format(ver)
        )
        self.root.update()
        self.main_object.sandesh.add("app_lang")
        self.main_object.value_change[0] = True


class sahAyikA:
    def __init__(self, m):
        th = Thread(target=self.__start)
        th.daemon = True
        th.start()
        self.c = 0
        self.d = 0
        self.main = m
        self.closed = True

    def __start(self):
        self.root = Tk()
        self.extra = [StringVar(self.root), StringVar(self.root)]
        self.set_extra_values()
        self.root.wm_withdraw()
        self.root.configure(bg="#faf9ae")
        self.root.attributes("-topmost", True)
        self.key = [StringVar(self.root), StringVar(self.root)]
        self.next = []
        self.varna = []
        self.reset_capital_status = False
        for x in range(0, 60):
            self.next.append(StringVar(self.root, value=""))
            self.varna.append(StringVar(self.root, value=""))
        self.root.overrideredirect(True)
        self.root.update()
        f = Frame(self.root, bg="#faf9ae")
        f.grid(row=0, column=0, sticky=NW)
        style = ttk.Style(self.root)
        f2 = Frame(f, bg="#faf9ae")
        can = Canvas(f2, width=24, height=43, bg="#faf9ae")
        can.pack()
        img = ImageTk.PhotoImage(image=Image.open(IMAGE_DB["main"]), master=can)
        can.create_image(3, 24, anchor=NW, image=img)
        f2.grid(row=0, column=0, sticky=NW)
        self.frame = Frame(f, bg="#faf9ae")
        style.configure(
            "A.TLabel",
            font=("Nirmala UI", 18, "bold"),
            foreground="brown",
            background="#faf9ae",
        )
        style.configure(
            "B.TLabel",
            font=("Nirmala UI", 13, "bold"),
            foreground="red",
            background="#faf9ae",
        )
        style.configure(
            "C.TLabel",
            font=("Nirmala UI", 15, "bold"),
            foreground="black",
            background="#faf9ae",
        )
        style.configure(
            "D.TLabel",
            font=("Nirmala UI", 15, "bold"),
            foreground="green",
            background="#faf9ae",
        )
        style.configure(
            "U.TLabel", font=("Nirmala UI", 15, "bold"), background="#faf9ae"
        )
        frm = Frame(self.frame, bg="#faf9ae")
        ttk.Label(frm, textvariable=self.key[0], style="A.TLabel", justify=CENTER).grid(
            row=0, column=0, sticky="n"
        )
        ttk.Label(frm, textvariable=self.key[1], style="B.TLabel", justify=CENTER).grid(
            row=1, column=0, sticky="n"
        )
        ttk.Label(frm, text=" ", style="U.TLabel").grid(row=0, column=1)
        ttk.Label(frm, text=" ", style="U.TLabel").grid(row=1, column=1)
        frm.grid(row=0, column=0, sticky=NW)
        self.f = []
        for x in range(0, 60):
            self.f.append(None)
        for x in range(0, 13):
            self.f[x] = Frame(self.frame, bg="#faf9ae")
            ttk.Label(
                self.f[x], textvariable=self.next[x], style="C.TLabel", justify=CENTER
            ).pack()
            ttk.Label(
                self.f[x], textvariable=self.varna[x], style="D.TLabel", justify=CENTER
            ).pack()
            self.f[x].grid(row=0, column=x + 1, sticky=NW)
        self.f_count = 12
        self.pUrvavarNa = [("", "", -1), ""]
        self.frame.grid(row=0, column=1, sticky=NW)
        f1 = Frame(self.root, bg="#faf9ae")
        style.configure(
            "Z1.TLabel",
            font=("Nirmala UI", 9, "bold"),
            foreground="purple",
            background="#faf9ae",
        )
        ttk.Label(f1, textvariable=self.extra[0], style="Z1.TLabel").grid(
            row=0, column=0, sticky=NW
        )
        style.configure(
            "Z2.TLabel", font=("Nirmala UI", 8), foreground="blue", background="#faf9ae"
        )
        ttk.Label(f1, textvariable=self.extra[1], style="Z2.TLabel").grid(
            row=1, column=0, sticky=NW
        )
        f1.grid(row=1, column=0, sticky=NW)
        self.root.mainloop()

    def hide(self, s=False):
        if s:
            if not self.closed:
                self.__reset()
                self.closed = True
            return
        if self.c == 1 and not self.closed:
            self.__reset()
            self.closed = True
        self.c -= 1

    def __reset(self):
        self.root.wm_withdraw()
        if self.f_count > 12:
            for x in range(13, self.f_count + 1):
                self.f[x].grid_forget()
            self.f_count = 12
        for x in range(0, 13):
            self.next[x].set("")
            self.varna[x].set("")

    def show(self, v):
        self.reset_capital_status = False

        def reset_capital(k):
            self.d -= 1
            if not self.reset_capital_status:
                return
            if self.d == 0:
                x = k[0]
                while x < k[1]:
                    self.varna[x].set("")
                    self.next[x].set("")
                    x += 1
                self.main.msg.add("clear_sg")
                self.main.value_change[1] = True

        if self.f_count > 12:
            for x in range(13, self.f_count + 1):
                self.f[x].grid_forget()
            self.f_count = 12
        next = v["key"][1]
        key = v["key"][0]
        matra = v["mAtrA"]
        extra_cap = v["special_cap"]
        if extra_cap[0]:
            self.pUrvavarNa = (
                [
                    akSharAH[self.main.lang_mode][extra_cap[1][0]][extra_cap[1][0]][0],
                    "",
                    extra_cap[1][1],
                ],
                extra_cap[1][0],
            )
        s = get_position()
        self.root.geometry("+{0}+{1}".format(s[0] + 5, s[1] + 25))
        halant = ("", False)
        if self.main.lang_mode not in ("Urdu", "Romanized"):
            halant = (
                akSharAH[self.main.lang_mode]["q"]["qq"][0],
                self.main.sa_lang == 1,
            )
        a = {}
        b = akSharAH[self.main.lang_mode][key[0]]
        count = 0
        for x in next:
            if key + x in b:
                a[x] = b[key + x]
                for y in b[key + x][-2]:
                    if key + x + y in b:
                        a[x + y] = b[key + x + y]
                        count += 1
                count += 1
        c = 0
        cap_count = [0, 0]  # to store of capitals to be cleared
        if "cap" in v:
            cap_count[0] = count
            b1 = akSharAH[self.main.lang_mode][key.upper()]
            a[key + key] = b1[key.upper()]
            next = a[key + key][-2]
            tmp = key.upper()
            for x in next:
                if tmp + x in b1:
                    a[key + key + x] = b1[tmp + x]
                    for y in b1[tmp + x][-2]:
                        if tmp + x + y in b1:
                            a[key + key + x + y] = b1[tmp + x + y]
                            count += 1
                    count += 1
            cap_count[1] = count + 1
        if (self.pUrvavarNa[0][-1] in [1, 3] or matra) and b[key][-1] == 0:
            k12 = self.pUrvavarNa[0][0] + b[key][1]
            if self.pUrvavarNa[0][-1] == 3 and key != "a":
                k12 = k12[:-2] + k12[-1] + k12[-2]
            elif self.pUrvavarNa[0][-1] == 3 and key == "a":
                k12 = k12[:-1] + k12[-1]
            self.key[0].set(self.pUrvavarNa[1] + key)
            self.key[1].set(k12)
        else:
            self.key[0].set(key)
            l12 = b[key][0] + (halant[0] if b[key][-1] in [1, 3] else "")
            if b[key][-1] == 3:
                l12 = l12[:-2] + l12[-1] + l12[-2]
            self.key[1].set(l12)
        for x in a:
            self.next[c].set(x)
            k = a[x][0]
            if a[x][-1] == 0 and self.pUrvavarNa[0][-1] in [1, 3]:
                k = a[x][1]
            if a[x][-1] in [1, 3] and halant[1]:
                k += halant[0]
                if a[x][-1] == 3:
                    k = k[:-2] + k[-1] + k[-2]
            if (self.pUrvavarNa[0][-1] in [1, 3] or matra) and a[x][-1] == 0:
                k = self.pUrvavarNa[0][0] + k
                if self.pUrvavarNa[0][-1] == 3:
                    k = k[:-2] + k[-1] + k[-2]
            self.varna[c].set(k)
            c += 1
        if len(a) - 1 > self.f_count + 1:
            for x in range(self.f_count + 1, len(a)):
                self.f[x] = Frame(self.frame, bg="#faf9ae")
                ttk.Label(
                    self.f[x],
                    textvariable=self.next[x],
                    style="C.TLabel",
                    justify=CENTER,
                ).pack()
                ttk.Label(
                    self.f[x],
                    textvariable=self.varna[x],
                    style="D.TLabel",
                    justify=CENTER,
                ).pack()
                self.f[x].grid(row=0, column=x + 1, sticky=NW)
            self.f_count = len(a) - 1
        for x in range(c, 13):
            self.next[x].set("")
            self.varna[x].set("")
        self.c += 1
        if not matra:
            self.pUrvavarNa = (b[key], key)
        if self.closed:
            self.closed = False
            self.root.wm_deiconify()
        if "cap" in v:
            self.d += 1
            self.reset_capital_status = True
            self.frame.after(4000, lambda: reset_capital(cap_count))
        self.root.after(15000, self.hide)

    def set_extra_values(self):
        l_data = DISPLAY_DATA[display_lang_lists[get_registry("language")]]
        self.extra[0].set(l_data["sahAyikA_msg"][0])
        self.extra[1].set(l_data["sahAyikA_msg"][1])
