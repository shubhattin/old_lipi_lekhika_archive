from tkinter import (
    Canvas, Frame,Button,IntVar,Label, Message,NW,PhotoImage,Scrollbar,Toplevel,Tk,
    Radiobutton,Checkbutton,LEFT,StringVar,OptionMenu,Text
)
import tkinter.ttk as ttk
from tkinter.constants import DISABLED, END, INSERT, NORMAL
from tkinter.font import Font
from os import startfile
from winregistry import WinRegistry
from dattAMsh import akSharAH,lang_code,sn_lng_data,en_lng_data,hn_lng_data,tri_bhASA,bhAShAH,ajay,bhAShAH_img
import pprint
from mouse import get_position
from json import dumps
from threading import Thread
ver = 1.0
def get_registry(name):
    reg = WinRegistry()
    path = r'HKCU\SOFTWARE\lekhika'
    try:
        a = int(reg.read_value(path, name)['data'])
        if a not in (0, 1) and (name == 'language' and a != 2):
            raise FileNotFoundError
        return a
    except FileNotFoundError:
        store_registry(0, name)
        return get_registry(name)


def store_registry(value, name):
    reg = WinRegistry()
    path = r'HKCU\SOFTWARE\lekhika'
    if 'lekhika' not in reg.read_key(r'HKCU\SOFTWARE')['keys']:
        reg.create_key(path)
    if name == 'language':
        reg.write_value(path, name, {
            0: b'0',
            1: b'1',
            2: b'2'
        }[value], 'REG_BINARY')
    else:
        reg.write_value(path, name, {0: b'0', 1: b'1'}[value], 'REG_BINARY')


def get_str_reg(name):
    reg = WinRegistry()
    path = r'HKCU\SOFTWARE\lekhika'
    try:
        a = reg.read_value(path, name)['data']
        if a not in lang_code[1]:
            raise FileNotFoundError
        return a
    except FileNotFoundError:
        store_str_reg('Hindi', name)
        return get_str_reg(name)


def store_str_reg(value, name):
    reg = WinRegistry()
    path = r'HKCU\SOFTWARE\lekhika'
    if 'lekhika' not in reg.read_key(r'HKCU\SOFTWARE')['keys']:
        reg.create_key(path)
    reg.write_value(path, name, value, 'REG_SZ')

def alert(msg, color=None, lapse=None, geo=None, AkAra=None,wait=False):
    if wait:
        alert_s(msg,color,lapse,geo,AkAra)
        return
    a=Thread(target=alert_s,args=(msg,color,lapse,geo,AkAra))
    a.daemon=True
    a.start()
    
def alert_s(msg, color=None, lapse=None, geo=None, AkAra=None):
    master = Tk()
    master.overrideredirect(True)
    if color == None:
        color = 'green' if 'On' in msg or 'चालू' in msg or \
            ('वि' not in msg and ('चलितम्' in msg or 'चलितं' in msg)) else 'red'
    if AkAra == None:
        AkAra = 19
    a = Frame(master,highlightbackground="brown",highlightthickness=3)
    Label(a,text=msg,
          font=Font(master,family="Nirmala Ui", weight='bold', size=AkAra),
          foreground=color).pack()
    a.pack()
    if lapse == None:
        lapse = 0 if 'Turn' in msg or 'किया' in msg or 'क्रियते' in msg else 300
    master.title('')
    if geo == None:
        master.geometry('+20+10')
    else:
        master.eval('tk::PlaceWindow . center')
    master.attributes('-topmost', True)
    master.update()
    master.after(650 + lapse, master.destroy)
    master.mainloop()

class Design:
    def __init__(self, main_obj, master):
        self.main_object = main_obj
        self.ex = True
        self.img_on_top_status=False
        self.advanced_window_data_preperation = False
        self.root = master
        self.style=ttk.Style(self.root)
        self.root.wm_withdraw()
        self.language_code = get_registry('language')
        self.img_window_status=False
        self.language = StringVar(self.root, tri_bhASA[self.language_code])
        self.l_data = {
            0: en_lng_data,
            1: hn_lng_data,
            2: sn_lng_data
        }[self.language_code]
        b = lang_code[1][main_obj.lang_mode]
        self.typing_lang_sub = StringVar(self.root, value=b)
        self.advanced_langauge = StringVar(self.root, value=b)
        self.karyAsthiti = IntVar(self.root, main_obj.ks)
        a = main_obj.sa_lang
        self.sanskrit_mode = IntVar(self.root, value=a)
        self.sanskrit_mode_sub = IntVar(self.root, value=a)
        a = int(main_obj.sg_status)
        self.sg = IntVar(self.root,value=a)
        self.sg_sub = IntVar(self.root,value=a)
        self.root.resizable(False, False)
        self.root.iconbitmap(r'assets\Icon.ico')
        self.root.title(self.l_data['app_title'])
        self.typing_lang = StringVar(self.root,
                                     value=lang_code[1][main_obj.lang_mode])
        self.design_top_frame()
        self.design_input_frame()
        self.set_text()
        self.root.protocol('WM_DELETE_WINDOW', self.hide)
        self.startup_window = IntVar(self.root,
                                     value=main_obj.window_start_status)
        self.app_status = IntVar(self.root, value=main_obj.ks)
        main_obj.tk_status=True
        if main_obj.window_start_status == 0:
            self.root.wm_deiconify()
              
    def design_top_frame(self):
        self.top_frame = Frame(self.root)
        my_font = Font(size=13, weight='bold', family='Nirmala UI')
        self.option_button = Button(self.top_frame,
                                    font=my_font,
                                    fg='blue',
                                    bg='yellow',
                                    relief='ridge',
                                    command=self.option_frame)
        self.option_button.grid(row=0, column=1, sticky=NW)
        self.usage_button = Button(self.top_frame,
                                   font=my_font,
                                   fg='green',
                                   bg='yellow',
                                   relief='ridge',
                                   command=self.open_pdf)
        self.usage_button.grid(row=0, column=2, sticky=NW)
        self.launch_button = Button(self.top_frame,
                                    font=my_font,
                                    fg='red',
                                    bg='yellow',
                                    relief='ridge',
                                    command=self.open_exe)
        self.launch_button.grid(row=0, column=3, sticky=NW)
        self.about_button = Button(self.top_frame,
                                   font=my_font,
                                   fg='brown',
                                   bg='yellow',
                                   relief='ridge',
                                   command=self.about_window)
        self.about_button.grid(row=0, column=4, sticky=NW)
        self.top_frame.grid(row=0, sticky=NW)
        seperator = Label(self.root, text=' ' * 20)
        seperator.grid(row=1, sticky=NW)

    def design_input_frame(self):
        self.command_frame = Frame(self.root)
        self.On = Radiobutton(self.command_frame,
                              font= Font(size=13, weight='bold', family='Nirmala UI'),
                              value=1, variable=self.karyAsthiti,
                              command=self.main_object.change,
                              fg="green",bg="lightgreen")
        self.On.pack(side=LEFT)
        self.Off = Radiobutton(self.command_frame,
                               font= Font(size=13, weight='bold', family='Nirmala UI'),
                               value=0,variable=self.karyAsthiti,
                               command=self.main_object.change,
                               fg="red",bg="lightgreen")
        self.Off.pack(side=LEFT)
        seperator0 = Label(self.command_frame, text='                ')
        seperator0.pack(side=LEFT)
        t="ajay➠"+ajay[lang_code[0][self.typing_lang.get()]]
        self.ajay0 = Radiobutton(self.command_frame, text=t[:-1],
                              font= Font(size=11, weight='bold', family='Nirmala UI'),
                              value=0, variable=self.sanskrit_mode,bg="lightblue",fg="brown",
                              command=self.update_sans_mode)
        self.ajay0.pack(side=LEFT)
        self.ajay1 = Radiobutton(self.command_frame,text=t,
                               font= Font(size=11, weight='bold', family='Nirmala UI'),
                               value=1,variable=self.sanskrit_mode,bg="lightblue",fg="brown",
                               command=self.update_sans_mode)
        self.ajay1.pack(side=LEFT)
        self.command_frame.grid(row=2, column=0, sticky=NW)
        frame = Frame(self.root)
        self.typ_l_main = Label(frame,
                                font=Font(size=10,
                                        weight='bold',
                                          family='Nirmala UI'),
                                fg='brown')
        self.typ_l_main.grid(row=0, column=0, sticky=NW)
        OptionMenu(frame,
                   self.typing_lang,
                   *bhAShAH,
                   command=self.update_typ_lang).grid(row=0,
                                                      column=1,
                                                      stick=NW)
        self.sanskrit_button = Checkbutton(frame,
                                           variable=self.sanskrit_mode,
                                           text=self.l_data['sanskrit'],
                                           fg='blue',
                                           font=Font(size=8,
                                                     weight='bold',
                                                     family='Nirmala UI'),
                                           command=self.update_sans_mode)
        self.sanskrit_button.grid(row=0, column=2,sticky=NW)
        self.sg_button = Checkbutton(frame,variable=self.sg,text="Show Suggestions",fg="brown",
                                     font=Font(size=8, weight='bold', family='Nirmala UI'),
                                     command=lambda :self.main_object.exec_taskbar_commands("sg",False))
        self.sg_button.grid(row=0,column=3,sticky=NW)
        frame.grid(row=3, column=0, sticky=NW)
        self.short_lbl = Label(self.root,
                               font=Font(size=8,
                                         weight='bold',
                                         family='Nirmala UI'),
                               fg='purple')
        self.short_lbl.grid(row=4, column=0, sticky=NW)

    def update_sans_mode(self,mannual=0,v=0):
        if mannual == 1:# from lang change
            self.sanskrit_mode.set(v)
            self.main_object.sa_lang=v
        elif mannual == 2:# from taskbar
            a=abs(self.sanskrit_mode.get()-1)
            self.sanskrit_mode.set(a)
            self.main_object.sa_lang=a
        else:
            self.main_object.sa_lang=self.sanskrit_mode.get()
        self.main_object.msg.add("update_sa")
        if mannual != 1:
            alert(msg="Sanskrit Mode Turned "+{0:"Off",1:"On"}[self.sanskrit_mode.get()],
              lapse=300)

    def option_frame(self):
        self.option_window = Toplevel(self.root)
        self.option_window.wm_withdraw()
        self.option_window.title(self.l_data['option'])
        self.option_window.iconbitmap(r'assets\Icon.ico')
        self.option_window.geometry('+180+80')
        my_font = Font(root=self.option_window,
                       size=11,
                       weight='bold',
                       family='Nirmala UI')
        self.lbl = Label(self.option_window,
                         text=self.l_data['language'],
                         font=my_font,
                         fg='green')
        self.lbl.grid(row=0, column=0, sticky=NW)
        bhASA = OptionMenu(self.option_window,
                           self.language,
                           *tri_bhASA,
                           command=self.update_lang_data)
        bhASA.grid(row=0, column=1, stick=NW)
        self.startup_message = Label(self.option_window,
                                     text=self.l_data['start_label'],
                                     font=Font(root=self.option_window,
                                               size=12,
                                               weight='bold',
                                               underline=1,
                                               family='Nirmala UI'),
                                     fg='brown')
        self.startup_message.grid(row=1, column=0, sticky=NW)
        self.startup = Checkbutton(
            self.option_window,
            text=self.l_data['start_win'],
            font=my_font,
            fg='purple',
            variable=self.startup_window,
            onvalue=0,
            offvalue=1,
            command=lambda: store_registry(self.startup_window.get(),
                                           'window_start'))
        self.startup.grid(row=2, column=0, sticky=NW)
        self.app_Status = Checkbutton(self.option_window,
                                      text=self.l_data['status_main'],
                                      font=my_font,
                                      fg='red',
                                      variable=self.app_status,
                                      command=lambda: store_registry(
                                          self.app_status.get(), 'app_status'))
        self.app_Status.grid(row=3, column=0, sticky=NW)
        self.sg_button_sub = Checkbutton(self.option_window,text="Show Suggestions",font=my_font,
                                         fg="purple",variable=self.sg_sub,
                                         command=lambda : store_registry(abs(self.sg_sub.get()-1),"sg_st"))
        self.sg_button_sub.grid(row=4,column=0,sticky=NW)
        self.typ_lang = Label(self.option_window,
                              text=self.l_data['lang_mode'],
                              font=my_font,
                              fg='green')
        self.typ_lang.grid(row=5, column=0, sticky=NW)
        bhASAd = OptionMenu(
            self.option_window,
            self.typing_lang_sub,
            *bhAShAH,
            command=lambda _: store_str_reg(
                lang_code[0][self.typing_lang_sub.get()], 'typ_lang'))
        bhASAd.grid(row=6, column=1, stick=NW)
        self.sa_mode = Checkbutton(
            self.option_window,
            text=self.l_data['sanskrit'],
            font=my_font,
            fg='purple',
            variable=self.sanskrit_mode_sub,
            command=lambda: store_registry(self.sanskrit_mode_sub.get(),
                                           'sa_mode'))
        self.sa_mode.grid(row=7, column=0, sticky=NW)
        self.extra = Label(self.option_window, text=self.l_data['extra'])
        self.extra.grid(row=8, column=0, sticky=NW)
        self.advanced_button = Button(self.option_window,
                                      text='Advanced',
                                      bg='red',
                                      font=Font(root=self.option_window,
                                                size=8,
                                                weight='bold',
                                                family='Nirmala UI'),
                                      command=self.advanced_options)
        self.advanced_button.grid(row=9, column=0, sticky=NW)
        self.option_window.resizable(False, False)
        self.option_window.wm_deiconify()
        try:
            self.option_window.mainloop()
        except:
            pass            

    def advanced_options(self):
        self.advanced_window = Toplevel(self.root)
        self.advanced_window.iconbitmap(r'assets\Icon.ico')
        self.advanced_window.geometry('+10+50')
        self.prepare_advanced_window_data()
        bhASAd = OptionMenu(self.advanced_window,
                            self.advanced_langauge,
                            *bhAShAH,
                            command=self.set_advanced_data)
        bhASAd.grid(row=1, column=0, stick=NW)
        f = Frame(self.advanced_window)
        self.advanced_text = Text(f,
                                  font=Font(root=self.root,
                                            size=14,
                                            weight='bold',
                                            family='Nirmala UI'),
                                  fg='green')
        self.advanced_text.configure(state=DISABLED)
        self.advanced_text.pack(side=LEFT)
        scr = Scrollbar(f, command=self.advanced_text.yview)
        self.advanced_text['yscrollcommand'] = scr.set
        scr.pack(side=LEFT, fill='y')
        f.grid(row=2, column=0)
        self.advanced_window.resizable(False, False)
        self.advanced_window.mainloop()

    def prepare_advanced_window_data(self):
        if self.advanced_window_data_preperation:
            return
        self.advanced_window_data = {}
        pprint.sorted = lambda x, key=None: x # for py 3.7
        for x in bhAShAH:
            if x in ("शारदा लिपि","मोडी लिपि","ब्रह्मी लिपि"):
                dta=dumps(akSharAH[lang_code[0][x]],ensure_ascii=True,sort_keys=False)
            else:
                dta=pprint.pformat(akSharAH[lang_code[0][x]], indent=4)
            self.advanced_window_data[x] = dta
        self.advanced_window_data_preperation = True

    def set_advanced_data(self, event):
        self.advanced_text.configure(state=NORMAL)
        self.advanced_text.delete('1.0', END)
        self.advanced_text.insert(
            INSERT,
            self.advanced_window_data.get(self.advanced_langauge.get()))
        self.advanced_text.configure(state=DISABLED)

    def set_text(self, c=False):
        if c:
            self.root.title(self.l_data['app_title'])
            self.option_window.title(self.l_data['option'])
            self.lbl.configure(text=self.l_data['language'])
            self.startup_message.configure(text=self.l_data['start_label'])
            self.startup.configure(text=self.l_data['start_win'])
            self.startup_message.configure(text=self.l_data['start_label'])
            self.app_Status.configure(text=self.l_data['status_main'])
            self.extra.configure(text=self.l_data['extra'])
            self.typ_lang.configure(text=self.l_data['lang_mode'])
            self.sa_mode.configure(text=self.l_data['sanskrit'])
        self.option_button.configure(text=self.l_data['option'])
        self.usage_button.configure(text=self.l_data['usage_button'])
        self.launch_button.configure(text=self.l_data['normal_button'])
        self.about_button.configure(text=self.l_data['about'])
        self.On.configure(text=self.l_data['on'])
        self.Off.configure(text=self.l_data['off'])
        self.sanskrit_button.configure(text=self.l_data['sanskrit'])
        self.typ_l_main.configure(text=self.l_data['lang_mode_text'])
        self.short_lbl.configure(text=self.l_data['shortcut_instruction'])

    def update_lang_data(self, event):
        self.ex = True
        self.language_code = tri_bhASA.index(self.language.get())
        self.l_data = {
            0: en_lng_data,
            1: hn_lng_data,
            2: sn_lng_data
        }[self.language_code]
        store_registry(self.language_code, 'language')
        self.set_text(True)

    def update_typ_lang(self, event):
        l=lang_code[0][self.typing_lang.get()]
        self.main_object.lang_mode=l
        self.main_object.msg.add("change_lang")
        t="ajay➠"+ajay[lang_code[0][self.typing_lang.get()]]
        self.ajay0.configure(text=t[:-1])
        self.ajay1.configure(text=t)
        alert(
            "Typing Language Changed To " + l,
            color="green", lapse=1200,
        )
        
    def about_window(self):
        about = Tk()
        about.title(self.l_data['about'])
        about.geometry('+140+70')
        about.wm_withdraw()
        about.resizable(False, False)
        about.iconbitmap(r'assets\Icon.ico')
        my_font = Font(root=about, size=13, weight='bold', family='Nirmala UI')
        Label(about,
              text=self.l_data['app_description'],
              font=my_font,
              fg='brown').pack()
        Label(about,
              text='भारते रचितः',
              font=Font(root=about,
                        size=11,
                        weight='bold',
                        family='Nirmala UI'),
              fg='purple').pack()
        Label(about,
              text='Email :- lipilekhika@gmail.com',
              font=my_font,
              fg='green').pack()
        Label(about,
              text="Version : "+str(ver),
              font=my_font,
              fg='red').pack()
        about.wm_deiconify()
        about.mainloop()
    
    def update_img_win(self):
        self.img_window_status=False
        self.img_win.destroy()
    
    def open_img(self):
        if self.img_window_status:
            self.img_win.wm_deiconify()
            return
        self.img_win = Toplevel(self.root)
        self.img_win.title('परिवर्तनसूच्यः')
        self.img_win.geometry('+870+0')
        self.img_win.protocol('WM_DELETE_WINDOW', self.update_img_win)
        self.img_win.iconbitmap(r'assets\Icon.ico')
        self.image_collection={}
        for v in bhAShAH:
            try:
                a=lang_code[0][v]
                if a in ["Sanskrit","Nepali","Konkani","Marathi"]:
                    a="Hindi"
                self.image_collection[v]=PhotoImage(
                    file=("assets\\img\\"+a+".gif"))
            except:
                pass
        try:
            self.image_collection["वैदिकसंस्कृत"]=PhotoImage(
                    file=("assets\\img\\Vedic.gif"))
        except:
            pass
        fr=Frame(self.img_win)
        lang=StringVar(self.img_win,value=self.typing_lang.get())
        bhASAd = OptionMenu(fr,lang,*bhAShAH_img,
            command=lambda _:
                    self.canvas.itemconfig(self.image_on_canvas,image=self.image_collection[lang.get()]))
        bhASAd.grid(row=0, column=0, stick=NW)
        Checkbutton(fr,text="Pin on Top",command=self.change_img_top).grid(row=0,column=1,sticky=NW)
        fr.grid(row=0,column=0,sticky=NW)
        self.canvas = Canvas(self.img_win, width = 466, height = 545)      
        self.canvas.grid(row=1,column=0,sticky=NW)
        self.image_on_canvas = self.canvas.create_image(5,0, anchor=NW,
                        image=self.image_collection[lang.get()])
        self.img_win.resizable(False, False)
        self.img_window_status=True
        try:
            self.img_win.mainloop()
        except:
            pass
    
    def change_img_top(self):
        self.img_on_top_status = not self.img_on_top_status
        self.img_win.attributes('-topmost', self.img_on_top_status)
    
    def open_pdf(self):
        path = 'assets\\' + {
            1: 'उपयोगकर्ता पुस्तिका.pdf',
            0: 'User Manual.pdf',
            2: 'उपयोगकर्तृपुस्तिका.pdf'
        }.get(self.language_code)
        try:
            startfile(path)
        except FileNotFoundError:
            alert('File Not Found !')

    def open_exe(self):
        path = 'samanya.exe'
        try:
            startfile(path)
        except FileNotFoundError:
            alert('File Not Found !')

    def hide(self, event=None):
        if self.ex:
            self.ex = False
            return
        self.root.wm_withdraw()
        if self.main_object.tk_status:
            alert(
                'Lipi Lekhika Still running in Background.\nCan be Closed and Operated through Taskbar icon.',
                color='purple',
                lapse=1500,
                geo=True,
                AkAra=13)

    def display(self, t):
        if t == 'about':
            self.about_window()
        elif t == 'options':
            self.option_frame()
        elif t == 'show':
            self.root.wm_deiconify()

class Suggestion:
    def __init__(self,m):
        th=Thread(target=self.__start)
        th.daemon=True
        th.start()
        self.c = 0
        self.d = 0
        self.main = m
        self.closed = True
        self.pUrvavarNa=""  
                 
    def __start(self):
        self.root = Tk()
        self.root.wm_withdraw()
        self.root.attributes('-topmost', True)
        self.key=[StringVar(self.root), StringVar(self.root)]
        self.next=[]
        self.varna=[]
        self.reset_capital_status=False
        for x in range(0,60):
            self.next.append(StringVar(self.root,value=""))
            self.varna.append(StringVar(self.root,value=""))
        self.root.overrideredirect(True)
        self.root.update()
        style=ttk.Style(self.root)
        self.frame=Frame(self.root,highlightbackground="blue",highlightthickness=3.5)
        style.configure("A.TLabel", font=("Nirmala UI", 18, "bold"), foreground="brown")
        style.configure("B.TLabel", font=("Nirmala UI", 13, "bold"), foreground="red")
        style.configure("C.TLabel", font=("Nirmala UI", 15, "bold"), foreground="black")
        style.configure("D.TLabel", font=("Nirmala UI", 15, "bold"), foreground="green")
        frm=ttk.Frame(self.frame)
        ttk.Label(frm,textvariable=self.key[0],style="A.TLabel").grid(row=0,column=0,sticky=NW)
        ttk.Label(frm,textvariable=self.key[1],style="B.TLabel").grid(row=1,column=0,sticky=NW)
        ttk.Label(frm,text=" ").grid(row=0,column=1)
        ttk.Label(frm,text=" ").grid(row=1,column=1)
        frm.grid(row=0,column=0,sticky=NW)
        self.frame.grid(row=0,column=0,sticky=NW)
        self.f = []
        for x in range(0,60):
            self.f.append(None)
        for x in range(0,13):
            self.f[x]=ttk.Frame(self.frame)
            ttk.Label(self.f[x],textvariable=self.next[x],style="C.TLabel").pack()
            ttk.Label(self.f[x],textvariable=self.varna[x],style="D.TLabel").pack()
            self.f[x].grid(row=0,column=x+1,sticky=NW)
        self.f_count = 12
        self.pUrvavarNa = [("","",-1),""]
        self.root.mainloop()
        
    def hide(self,s=False):
        if s:
            if not self.closed:
                self.__reset()
                self.closed=True
            return
        if self.c==1 and not self.closed:
            self.__reset()
            self.closed = True
        self.c-=1
    
    def __reset(self):
        self.root.wm_withdraw()
        if self.f_count > 12:
            for x in range(13,self.f_count+1):
                self.f[x].grid_forget()
            self.f_count=12
        for x in range(0,13):
            self.next[x].set("")
            self.varna[x].set("")
                    
    def show(self,v):
        self.reset_capital_status=False
        def reset_capital(k,l):
            if not self.reset_capital_status:
                return
            if self.d==1:
                if l == 1:
                    self.hide(True)
                else:
                    k[1]+=1
                    for x in k:
                        self.varna[x].set("")
                        self.next[x].set("")
            self.d-=1
        if self.f_count > 12:
            for x in range(13,self.f_count+1):
                self.f[x].grid_forget()
            self.f_count=12
        next = v["key"][1]
        key = v["key"][0]
        s=get_position()
        self.root.geometry("+{0}+{1}".format(s[0]+5,s[1]+25))
        halant=("",False)
        if self.main.lang_mode not in ("Urdu","Romanized"):
            halant=(akSharAH[self.main.lang_mode]["q"]["qq"][0],self.main.sa_lang == 1)
        a={}
        b = akSharAH[self.main.lang_mode][key[0]]
        count=0
        for x in next:
            if key+x in b:
                a[x] = b[key+x]
                for y in b[key+x][-2]:
                    if key+x+y in b:
                        a[x+y] = b[key+x+y]
            count+=1
        c=0
        cap_count = [0,0]   #to store of capitals to be cleared
        if "cap" in v:
            cap_count[0] = count
            b1=akSharAH[self.main.lang_mode][key.upper()]
            a[key+key] = b1[key.upper()]
            next=a[key+key][-2]
            tmp=key.upper()
            for x in next:
                if tmp+x in b1:
                    a[key+key+x]=b1[tmp+x]
                    for y in b1[tmp+x][-2]:
                        if tmp+x+y in b:
                            a[key+key+x+y] = b[tmp+x+y]
                count+=1
            cap_count[1]=count-1
        if self.pUrvavarNa[0][-1] == 1 and b[key][-1] == 0:
            self.key[0].set(self.pUrvavarNa[1]+key)
            self.key[1].set(self.pUrvavarNa[0][0]+b[key][1])
        else:
            self.key[0].set(key)
            self.key[1].set(b[key][0] + (halant[0] if b[key][-1]==1 else ""))
        for x in a:
            self.next[c].set(x)
            k=a[x][0]
            if a[x][-1] == 0 and self.pUrvavarNa[0][-1] == 1:
                k=a[x][1]
            if a[x][-1] == 1 and halant[1]:
                k+=halant[0]
            if self.pUrvavarNa[0][-1] == 1 and a[x][-1] == 0:
                k=self.pUrvavarNa[0][0] + k
            self.varna[c].set(k)
            c+=1
        if len(a) - 1 > self.f_count+1:
            for x in range(self.f_count+1, len(a)):
                self.f[x] = ttk.Frame(self.frame)
                ttk.Label(self.f[x],textvariable=self.next[x],style="C.TLabel").pack()
                ttk.Label(self.f[x],textvariable=self.varna[x],style="D.TLabel").pack()
                self.f[x].grid(row=0,column=x+1,sticky=NW)
            self.f_count = len(a) - 1
        for x in range(c,13):
            self.next[x].set("")
            self.varna[x].set("")
        self.c+=1
        self.pUrvavarNa = (b[key],key)
        if self.closed:
            self.closed = False
            self.root.wm_deiconify()
        if "cap" in v:
            self.d+=1
            self.reset_capital_status=True
            self.frame.after(4000,lambda :reset_capital(cap_count,len(a)))
        self.root.after(15000,self.hide)
