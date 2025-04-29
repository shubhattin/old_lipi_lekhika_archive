from tkinter import (
    Canvas, Frame,Button,IntVar,Label,NW,PhotoImage,Scrollbar,Toplevel,Tk,
    Radiobutton,Checkbutton,LEFT,StringVar,OptionMenu,Text
)
from tkinter.ttk import Scrollbar
from tkinter.constants import DISABLED, END, INSERT, NORMAL
from tkinter.font import Font
from os import startfile
from winregistry import WinRegistry
from dattAMsh import akSharAH
import pprint

lang_code = [{
    'देवनागरी': 'de',
    'తెలుగు': 'te',
    'தமிழ்': 'ta',
    'മലയാളം': 'ma',
    'ଓଡିଆ': 'or',
    'ಕನ್ನಡ': 'ka',
    'IAST': 'ia',
    'ગુજરાતી': 'gu',
    'বাংলা': 'be',
    'ਪੰਜਾਬੀ': 'pn',
    'অসমীয়া': 'as'
}, {
    'de': 'देवनागरी',
    'te': 'తెలుగు',
    'ta': 'தமிழ்',
    'ma': 'മലയാളം',
    'or': 'ଓଡିଆ',
    'ka': 'ಕನ್ನಡ',
    'ia': 'IAST',
    'be': 'বাংলা',
    'gu': 'ગુજરાતી',
    'pn': 'ਪੰਜਾਬੀ',
    'as': 'অসমীয়া'
}, {
    'de': 'Devanagari',
    'te': 'Telugu',
    'ta': 'Tamil',
    'ma': 'Malayalam',
    'or': 'Odia',
    'ka': 'Kannada',
    'ia': 'IAST',
    'be': 'Bengali',
    'gu': 'Gujarati',
    'pn': 'Punjabi',
    'as': 'Assamese'
}]
tri_bhASA = ('English', 'हिन्दी', 'संस्कृतम्')
bhAShAH = ('देवनागरी', 'தமிழ்', 'తెలుగు', 'বাংলা', 'ಕನ್ನಡ', 'ગુજરાતી',
           'മലയാളം', 'ଓଡିଆ', 'ਪੰਜਾਬੀ', 'অসমীয়া','IAST')
en_lng_data = {
    'language':
    'Langauage',
    'about':
    'About',
    'app_title':
    'Devanagari Lekhika',
    'app_description':
    'This Application is Typing Tool for Indian Scripts.'
    '\nFor Writing :- Hindi, Tamil, Telugu, Sanskrit, Marathi, Malayalam,\n Kannada, Odia, Bengali, Punjabi and Gujarati.',
    'usage_button':
    '  Usage Instructions  ',
    'normal_button':
    ' Open  Normal Version',
    'on':
    'On',
    'off':
    'Off',
    'dev_numbers':
    'Devanagari Numerals',
    'turned_on':
    'Turned On',
    'turned_off':
    'Turned Off',
    'dev_num_on':
    'Devanagari Numeral mode On',
    'dev_num_off':
    'Devanagari Numeral mode Off',
    'shortcut_instruction':
    'Press Windows + z to Turn Main On/Off.\n'
    'Press Shift + F4 to Turn Devanagari Numeral Mode On/off.'
    '\nDouble Click on the Taskbar Icon to Turn On/Off.'
    '\nAfter closing this Window, App is still running.You can control '
    'It from Taskbar.\nYou can exit the Program Through Taskbar Only.\nEnc'
    'oding Table(परिवर्तन सूची) can be viewed using Taskbar Icon.'
    '\nPress SHIFT+F1 to Quickly Open App.This is the shorcut key for lauching.',
    'option':
    'Option',
    'start_label':
    'Set Default Startup Options',
    'start_win':
    'Open App Window on App Startup',
    'status_main':
    'Turn On the App',
    'lang_mode_text':
    'Typing Language Mode',
    'lang_mode':
    'Typing Script',
    'extra':
    'Setting App Window StartUp to No,\n'
    'will allow the App to open only in Taskbar.',
    'sanskrit':
    'Sanskrit Mode'
}
hn_lng_data = {
    'language':
    '  भाषा  ',
    'about':
    '  ऐप  परिचय   ',
    'app_title':
    'देवनागरी लेखिका',
    'app_description':
    'यह अनुप्रयोग भारतीय लिपियों के लिए परिवर्तनोपकरण है।\nहिन्दी, तमिल, संस्कृत, तेलुगु, मलयालम,कन्नड़\n'
    'ओड़िया, मराठी, बंगाली, गुजराती एवं पंजाबी के लेखन के लिए।',
    'usage_button':
    '  प्रयोग  विधि  ',
    'normal_button':
    '   सामान्य  संस्करण  खोलें   ',
    'on':
    'चालू',
    'off':
    'बन्द',
    'dev_numbers':
    'देवनागरी संख्याएं',
    'turned_on':
    'चालू किया गया',
    'turned_off':
    'बन्द किया गया',
    'dev_num_on':
    'देवनागरी संख्या प्रणाली चालू',
    'dev_num_off':
    'देवनागरी संख्या प्रणाली बन्द',
    'shortcut_instruction':
    'मुख्य को बन्द/चालू करने के लिए Windows + z दबाएं ।'
    '\nदेवनागरी संख्या प्रणाली को बन्द/चालू करने के लिये Shift + F4 दबाएं ।'
    '\nअनुप्रयोग को बन्द/चालू करने के लिए कर्यपट्टी के चित्र को दो बार दबाएं ।'
    '\nआपके द्वारा इस कोष्ठ को बन्द के बाद भी चलता रहेगा।\nआप इसे कार्यपट्टी के'
    ' चिय्रक से नियंत्रित कर सकते हैं।\nआप अनुप्रयोग को चित्रक के द्वारा हि बन्द कर सकते हैं ।'
    '\nइस अनुप्रयोग को सीधा(सहसा, डाइरेक्ट) खोलने के लिए SHIFT+F1 दबाएँ।',
    'option':
    'विकल्प',
    'start_label':
    'प्रारंभकाल के पूर्वनिश्चित विकल्प',
    'start_win':
    'अनुप्रयोग का मुख्य कोष्ठ खोलें',
    'status_main':
    'अनुप्रयोग को चालू रखें',
    'lang_mode_text':
    'लेखन भाषा प्रणाली',
    'lang_mode':
    'लेखन लिपि',
    'extra':
    '',
    'sanskrit':
    'संस्कृत प्रणाली'
}
sn_lng_data = {
    'language':
    '  भाषा  ',
    'about':
    'अनुप्रयोगपरिचय:',
    'app_title':
    'देवनागरीलेखिका',
    'app_description':
    'अयं अनुप्रयोगं भारतीयेभ्यः लिपिभ्यः परिवर्तनोपकरणम् अस्ति।\nहिन्दी-तमिल-तेलुगु-मलयालम-कन्नड़-'
    'ओड़िया-मराठी-बंगाली-गुजराती-पंजाबी-संस्कृतानां लेखनाय।',
    'usage_button':
    'प्रयोगविधिः',
    'normal_button':
    'सामान्यसंस्करणमुद्घाटयतु',
    'dev_numbers':
    'देवनागरीसंख्या',
    'on':
    'चलितम्',
    'off':
    'विचलतिम्',
    'turned_on':
    'चलितं क्रियते',
    'turned_off':
    'विचलितं क्रियते',
    'dev_num_on':
    'देवनागरीसंख्या प्रणाल्याः चलितम्',
    'dev_num_off':
    'देवनागरीसंख्या प्रणाल्याः विचलितम्',
    'shortcut_instruction':
    'मौख्यं चलितं/विचलितं करितुं Windows + z तुदतु ।'
    '\nदेवनागरीसंख्या प्रणालीं चलितं/विचलितं करितुं Shift+F4 तुदतु ।'
    '\nअनुप्रयोगं चलितं/विचलितं करितुं कर्यपट्ट्याः चित्रकं द्विकाले तुदतु ।'
    '\nअनुप्रयोगं सहसा उद्घाटयतुं SHIFT+F1 तुदतु।',
    'option':
    'विकल्पानि',
    'start_label':
    'प्रारंभकालस्य पूर्वनिश्चितविकल्पानि',
    'start_win':
    'अनुप्रयोगस्य मुख्यकोष्टम् उद्घाटयतु',
    'status_main':
    'अनुप्रयोगचलितम्',
    'lang_mode_text':
    'लेखनभाषाप्रणाली',
    'lang_mode':
    'लेखनलिपिः',
    'extra':
    '',
    'sanskrit':
    'संस्कृतप्रणाली'
}


def get_registry(name):
    reg = WinRegistry()
    path = r'HKCU\SOFTWARE\dev_lekhika'
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
    path = r'HKCU\SOFTWARE\dev_lekhika'
    if 'dev_lekhika' not in reg.read_key(r'HKCU\SOFTWARE')['keys']:
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
    path = r'HKCU\SOFTWARE\dev_lekhika'
    try:
        a = reg.read_value(path, name)['data']
        if a not in lang_code[1]:
            raise FileNotFoundError
        return a
    except FileNotFoundError:
        store_str_reg('de', name)
        return get_str_reg(name)


def store_str_reg(value, name):
    reg = WinRegistry()
    path = r'HKCU\SOFTWARE\dev_lekhika'
    if 'dev_lekhika' not in reg.read_key(r'HKCU\SOFTWARE')['keys']:
        reg.create_key(path)
    reg.write_value(path, name, value, 'REG_SZ')

def alert(msg, color=None, lapse=None, geo=None, AkAra=None):
    master = Tk()
    if color == None:
        color = 'green' if 'On' in msg or 'चालू' in msg or \
            ('वि' not in msg and ('चलितम्' in msg or 'चलितं' in msg)) else 'red'
    if AkAra == None:
        AkAra = 16
    Label(master,text=msg,
          font=Font(master, weight='bold', size=AkAra),
          foreground=color).pack()
    if lapse == None:
        lapse = 0 if 'Turn' in msg or 'किया' in msg or 'क्रियते' in msg else 300
    master.title('')
    if geo == None:
        geo = '+0+0'
        master.geometry('+0+0')
    else:
        master.eval('tk::PlaceWindow . center')
    master.iconbitmap(r'resources\Icon.ico')
    master.attributes('-topmost', True)
    master.update()
    master.after(650 + lapse, master.destroy)
    master.mainloop()

class Design:
    def __init__(self, main_obj, master):
        self.main_object = main_obj
        self.ex = False
        self.root_status = True
        self.img_on_top_status=False
        self.advanced_window_data_preperation = False
        self.root = master
        self.language_code = get_registry('language')
        self.img_window_status=False
        self.language = StringVar(self.root, tri_bhASA[self.language_code])
        self.l_data = {
            0: en_lng_data,
            1: hn_lng_data,
            2: sn_lng_data
        }[self.language_code]
        if main_obj.window_start_status == 1:
            self.hide()
            self.root_status = False
        self.root.geometry('520x265+200+100')
        b = lang_code[1][main_obj.lang_mode]
        self.typing_lang_sub = StringVar(self.root, value=b)
        self.advanced_langauge = StringVar(self.root, value=b)
        self.karyAsthiti = IntVar(self.root, main_obj.ks)
        self.dev_saMkyA = IntVar(self.root, main_obj.ds)
        a = main_obj.main.sa_lang
        self.sanskrit_mode = IntVar(self.root, value=a)
        self.sanskrit_mode_sub = IntVar(self.root, value=a)
        self.root.resizable(False, False)
        self.root.iconbitmap(r'resources\Icon.ico')
        self.root.title(self.l_data['app_title'])
        self.typing_lang = StringVar(self.root,
                                     value=lang_code[1][main_obj.lang_mode])
        self.design_top_frame()
        self.design_input_frame()
        self.set_text()
        self.root.bind('<Unmap>', self.hide)
        self.root.protocol('WM_DELETE_WINDOW', self.hide)
        self.startup_window = IntVar(self.root,
                                     value=main_obj.window_start_status)
        self.app_status = IntVar(self.root, value=main_obj.ks)
        self.num_status = IntVar(self.root, value=0)

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
        my_font = Font(size=16, weight='bold', family='Nirmala UI')
        self.On = Radiobutton(self.command_frame,
                              font=my_font,
                              value=1,
                              variable=self.karyAsthiti,
                              command=self.main_object.change)
        self.On.pack(side=LEFT)
        self.Off = Radiobutton(self.command_frame,
                               font=my_font,
                               value=0,
                               variable=self.karyAsthiti,
                               command=self.main_object.change)
        self.Off.pack(side=LEFT)
        seperator1 = Label(self.command_frame, text='         ')
        seperator1.pack(side=LEFT)
        self.num = Checkbutton(self.command_frame,
                               font=Font(size=9,
                                         weight='bold',
                                         family='Nirmala UI'),
                               variable=self.dev_saMkyA,
                               command=self.main_object.change_num)
        if self.karyAsthiti.get() == 1:
            self.num.pack(side=LEFT)
        self.command_frame.grid(row=2, column=0, sticky=NW)
        frame = Frame(self.root)
        self.typ_l_main = Label(frame,
                                font=Font(size=12,
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
        self.sanskrit_button.grid(row=0, column=2)
        frame.grid(row=3, column=0, sticky=NW)
        self.short_lbl = Label(self.root,
                               font=Font(size=10,
                                         weight='bold',
                                         family='Nirmala UI'),
                               fg='purple')
        self.short_lbl.grid(row=4, column=0, sticky=NW)

    def update_sans_mode(self,mannual=0,v=0):
        if mannual == 1:# from lang change
            self.sanskrit_mode.set(v)
        elif mannual == 2:# from taskbar
            self.sanskrit_mode.set(abs(self.sanskrit_mode.get()-1))
        self.main_object.main.sa_lang = int(self.sanskrit_mode.get())
        self.main_object.systray.update(
            hover_text=self.main_object.taskbar_text())
        if mannual != 1:
            alert(msg="Sanskrit Mode Turned "+{0:"Off",1:"On"}[self.sanskrit_mode.get()],
              lapse=300)

    def option_frame(self) -> None:
        self.option_window = Toplevel(self.root)
        self.option_window.title(self.l_data['option'])
        self.option_window.iconbitmap(r'resources\Icon.ico')
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
        self.typ_lang = Label(self.option_window,
                              text=self.l_data['lang_mode'],
                              font=my_font,
                              fg='green')
        self.typ_lang.grid(row=4, column=0, sticky=NW)
        bhASAd = OptionMenu(
            self.option_window,
            self.typing_lang_sub,
            *bhAShAH,
            command=lambda _: store_str_reg(
                lang_code[0][self.typing_lang_sub.get()], 'typ_lang'))
        bhASAd.grid(row=4, column=1, stick=NW)
        self.sa_mode = Checkbutton(
            self.option_window,
            text=self.l_data['sanskrit'],
            font=my_font,
            fg='purple',
            variable=self.sanskrit_mode_sub,
            command=lambda: store_registry(self.sanskrit_mode_sub.get(),
                                           'sa_mode'))
        self.sa_mode.grid(row=5, column=0, sticky=NW)
        self.extra = Label(self.option_window, text=self.l_data['extra'])
        self.extra.grid(row=6, column=0, sticky=NW)
        self.advanced_button = Button(self.option_window,
                                      text='Advanced',
                                      bg='red',
                                      font=Font(root=self.option_window,
                                                size=8,
                                                weight='bold',
                                                family='Nirmala UI'),
                                      command=self.advanced_options)
        self.advanced_button.grid(row=7, column=0, sticky=NW)
        self.option_window.resizable(False, False)
        try:
            self.option_window.mainloop()
        except:
            pass            

    def advanced_options(self):
        self.advanced_window = Toplevel(self.root)
        self.advanced_window.iconbitmap(r'resources\Icon.ico')
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
        for x in bhAShAH:
            self.advanced_window_data[x] = pprint.pformat(
                akSharAH[lang_code[0][x]], indent=7, sort_dicts=False)
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
        self.num.configure(text=self.l_data['dev_numbers'])

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
        self.main_object.main.set_typing_lang(
            lang_code[0][self.typing_lang.get()], 1)

    def about_window(self) -> None:
        about = Tk()
        about.title(self.l_data['about'])
        about.geometry('+140+70')
        about.resizable(False, False)
        about.iconbitmap(r'resources\Icon.ico')
        my_font = Font(root=about, size=13, weight='bold', family='Nirmala UI')
        Label(about,
              text=self.l_data['app_description'],
              font=my_font,
              fg='brown').pack()
        Label(about,
              text='भारतीयेनैव शुभमानन्दगुप्तेन भारतैव विरचिता',
              font=Font(root=about,
                        size=11,
                        weight='bold',
                        family='Nirmala UI'),
              fg='purple').pack()
        Label(about,
              text='Email :- devanagaritool@gmail.com',
              font=my_font,
              fg='green').pack()
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
        self.img_win.geometry('+900+0')
        self.img_win.protocol('WM_DELETE_WINDOW', self.update_img_win)
        self.img_win.iconbitmap(r'resources\Icon.ico')
        self.image_collection={}
        for v in bhAShAH:
            try:
                self.image_collection[v]=PhotoImage(
                    file=("resources\\img\\"+lang_code[0][v]+".gif"))
            except:
                pass
        fr=Frame(self.img_win)
        lang=StringVar(self.img_win,value=self.typing_lang.get())
        bhASAd = OptionMenu(fr,lang,*bhAShAH,
            command=lambda _: 
                    self.canvas.itemconfig(self.image_on_canvas,image=self.image_collection[lang.get()]))
        bhASAd.grid(row=0, column=0, stick=NW)
        Checkbutton(fr,text="Make on Top",command=self.change_img_top).grid(row=0,column=1,sticky=NW)
        fr.grid(row=0,column=0,sticky=NW)
        self.canvas = Canvas(self.img_win, width = 412, height = 548)      
        self.canvas.grid(row=1,column=0,sticky=NW)
        self.image_on_canvas = self.canvas.create_image(5,0, anchor=NW,
                        image=self.image_collection[lang.get()])
        self.img_win.resizable(False, False)
        self.img_window_status=True
        Label(self.img_win,font=Font(weight="bold",size=7,family='Nirmala UI'),
              text="Press ,, (double commaa) after a small Alphabet to produce results of Capital Alphabets"
              "\nFor Example:- n,, would Lead to N\n\t\td,, would be D").grid(row=2,column=0,sticky=NW)
        try:
            self.img_win.mainloop()
        except:
            pass
    
    def change_img_top(self):
        self.img_on_top_status = not self.img_on_top_status
        self.img_win.attributes('-topmost', self.img_on_top_status)
    
    def open_pdf(self):
        path = 'resources\\' + {
            1: 'उपयोगकर्ता पुस्तिका.pdf',
            0: 'User Manual.pdf',
            2: 'उपयोगकर्तृपुस्तिका.pdf'
        }.get(self.language_code)
        try:
            startfile(path)
        except FileNotFoundError:
            alert('File Not Found !')

    def open_exe(self):
        path = 'dev.exe'
        try:
            startfile(path)
        except FileNotFoundError:
            alert('File Not Found !')

    def hide(self, event=None):
        if self.ex:
            self.ex = False
            return
        self.root_status = False
        self.root.wm_withdraw()
        if self.main_object.tk_start_status:
            alert(
                'देवनागरी लेखिका Still running in Background.\nCan be Closed and Operated through Taskbar icon.',
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
            self.root_status = True
