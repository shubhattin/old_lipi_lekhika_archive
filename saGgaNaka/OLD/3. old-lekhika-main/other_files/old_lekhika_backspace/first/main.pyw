from keyboard import on_press, add_hotkey
from mouse import on_click, on_middle_click, on_right_click
from convert import parivartana
from infi.systray import SysTrayIcon
from tkinter import Frame, Button, IntVar, Label, NW, Toplevel,\
    Tk, Radiobutton, Checkbutton, LEFT, N
from tkinter.font import Font
from winregistry import WinRegistry
from os import startfile


def get_registry(name) -> int:
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


def store_registry(value, name) -> None:
    reg = WinRegistry()
    path = r'HKCU\SOFTWARE\dev_lekhika'
    if 'dev_lekhika' not in reg.read_key(r'HKCU\SOFTWARE')['keys']:
        reg.create_key(path)
    if name == 'language':
        reg.write_value(path, name, {0: b'0', 1: b'1', 2: b'2'}[
                        value], 'REG_BINARY')
    else:
        reg.write_value(path, name, {0: b'0', 1: b'1'}[value], 'REG_BINARY')


en_lng_data = {
    'language': 'Langauage', 'about': 'About',
    'app_title': 'Devanagari Lekhika',
    'app_description': 'Devanagri Script Transliteration Software.\nCan be used for typing Hindi, Sanskrit and Marathi.',
    'usage_button': '  Usage Instructions  ',
    'normal_button': ' Open  Normal Version',
    'on': 'On', 'off': 'Off',
    'dev_numbers': 'Devanagari Numerals',
    'turned_on': 'Turned On',
    'turned_off': 'Turned Off',
    'dev_num_on': 'Devanagari Numeral mode On',
    'dev_num_off': 'Devanagari Numeral mode Off',
    'shubham_nirmAtA': 'Author : Shubham Anand Gupta',
    'shortcut_instruction': 'Press Ctrl+Shift to Turn Main On/Off.\n'
    'Press Shift+Esc to Turn Devanagari Numeral Mode On/off.'
    '\nDouble Click on the Taskbar Icon to Turn On/Off.',
    'option': 'Option',
    'start_label': 'Start Up Options',
    'start_win': 'Open App Window on App Startup',
    'yes': 'Yes',
    'no': 'No',
    'status_main': 'Default App Status',
    'status_num': 'Default Number Format',
    'roman': 'Normal',
    'devanagari': 'Devanagari',
    'extra': 'Setting App Window StartUp to No,\n'
    'will allow the App to open only in Taskbar.'
}
hn_lng_data = {
    'language': '  भाषा  ', 'about': '  ऐप  परिचय   ',
    'app_title': 'देवनागरी लेखिका',
    'app_description': 'देवनागरी लिपि परिवतर्तनोपकरण ।\nहिन्दी, संस्कृत एवं  मराठी लेखन कार्य मे सक्षम ।',
    'usage_button': '  प्रयोग  विधि  ',
    'normal_button': '   सामान्य  संस्करण  खोलें   ',
    'on': 'चालू', 'off': 'बन्द',
    'dev_numbers': 'देवनागरी संख्याएं',
    'turned_on': 'चालू किया गया',
    'turned_off': 'बन्द किया गया',
    'dev_num_on': 'देवनागरी संख्या प्रणाली चालू',
    'dev_num_off': 'देवनागरी संख्या प्रणाली बन्द',
    'shubham_nirmAtA': 'ऐप लेखक : शुभम आनन्द गुप्ता',
    'shortcut_instruction': 'मुख्य को बन्द/चालू करने के लिए Ctrl+Shift दबाएं ।'
    '\nदेवनागरी संख्या प्रणाली को बन्द/चालू करने के लिये Shift+Esc दबाएं ।'
    '\nऐप को बन्द/चालू करने के लिए कर्यपट्टी के चित्र को दो बार दबाएं ।',
    'option': 'विकल्प',
    'start_label': 'प्रारंभकाले विकल्पाः',
    'start_win': 'ऐप के प्रारंभ मे ऐप विण्डो खोलें',
    'yes': 'हाँ',
    'no': 'नहीं',
    'status_main': 'पीर्वनिश्चित ऐप स्थिति',
    'status_num': 'पूर्वनिश्चित संख्या प्रणाली',
    'roman': 'सामान्य',
    'devanagari': 'देवनागरी',
    'extra': 'यदि आप \' प्रारंभ मे विंडो खोलने \' को\n'
    'नहीं पर कर देंगे तो केवल कार्यपट्टी मे ही ऐप खुलेगा ।'
}
sn_lng_data = {
    'language': '  भाषा  ', 'about': 'अनुप्रयोगपरिचय:',
    'app_title': 'देवनागरीलेखिका',
    'app_description': 'देवनागरीलिपये परिवतर्तनोपकरणं ।\nहिन्दीसंस्कृतमराठी लेखनकार्ये अति सक्षमः ।',
    'usage_button': 'प्रयोगविधिः',
    'normal_button': 'सामान्यसंस्करणं  उद्घाटयति',
    'on': 'चलितं', 'off': 'विचलितम्',
    'dev_numbers': 'देवनागरीसंख्या',
    'turned_on': 'चलितंकृत्वा',
    'turned_off': 'विचलितंकृत्वा',
    'dev_num_on': 'देवनागरीसंख्या प्रणाल्याः चलितम्',
    'dev_num_off': 'देवनागरीसंख्या प्रणाल्याः विचलितम्',
    'shubham_nirmAtA': 'अनुप्रगस्य लेखकः : शुभमानन्दगुप्ता',
    'shortcut_instruction': 'मुख्यस्य चलितं/विचलितं कुर्वते Ctrl+Shift नोदयतु ।'
    '\nदेवनागरीसंख्या प्रणालीम् चलितं/विचलितं कुर्वते Shift+Esc नोदयतु ।'
    '\nअनुप्रयोगं चलितं/विचलितं कुर्वते कर्यपट्ट्या चित्रकं द्विनोदयतु ।',
    'option': 'विकल्पाः',
    'start_label': 'प्रारंभकालस्य विकल्पाः',
    'start_win': 'अनुप्रयोगस्य प्रारंभं अनुप्रयोगकोष्टं उद्घाटयतु',
    'yes': 'अस्तु',
    'no': 'नास्तु',
    'status_main': 'पीर्वनिश्चितः अनुप्रयोगस्थितिः',
    'status_num': 'पूर्वनिश्चितः संख्यास्थिति:',
    'roman': 'सामान्य:',
    'devanagari': 'देवनागरी',
    'extra': 'यदित्वं प्ररम्भे अनुप्रयोग उद्घाटयतं\n'
    'नास्तु कुर्वतः तदा केवलं कार्यपट्ट्यामेव अनुप्रयोगः उदघाटयतु।'
}


def alert(msg):
    master = Tk()
    color = 'green' if 'On' in msg or 'चालू' in msg or \
        ('वि' not in msg and ('चलितम्' in msg or 'चलितं' in msg)) else 'red'
    Label(master, text=msg, font=Font(master, weight='bold', size=16),
          foreground=color).pack()
    lapse = 0 if 'Turn' in msg or 'किया' in msg else 300
    master.title('')
    master.geometry('+0+0')
    master.iconbitmap(r'assets\Icon.ico')
    master.attributes('-topmost', True)
    master.update()
    master.after(650 + lapse, master.destroy)
    master.mainloop()


class Design:
    def __init__(self, main_obj, master):
        self.ex = False
        self.root_status = True
        self.__root = master
        self.__language = IntVar(self.__root, get_registry('language'))
        self.l_data = {0: en_lng_data, 1: hn_lng_data,
                       2: sn_lng_data}[self.__language.get()]
        if main_obj.window_start_status == 1:
            self.__hide()
            self.root_status = False
        self.__main_object = main_obj
        self.__root.geometry('614x194+200+100')
        self.karyAsthiti = IntVar(self.__root, main_obj.ks)
        self.dev_saMkyA = IntVar(self.__root, main_obj.ds)
        self.__root.resizable(False, False)
        self.__root.iconbitmap(r'assets\Icon.ico')
        self.__root.title(self.l_data['app_title'])
        self.__design_top_frame()
        self.__design_input_frame()
        self.__set_text()
        self.__root.bind('<Unmap>', self.__hide)
        self.__root.protocol('WM_DELETE_WINDOW', self.__hide)
        self.__startup_window = IntVar(
            self.__root, value=main_obj.window_start_status)
        self.__app_status = IntVar(self.__root, value=main_obj.ks)
        self.__num_status = IntVar(self.__root, value=main_obj.ds)

    def __design_top_frame(self) -> None:
        self.__top_frame = Frame(self.__root)
        my_font = Font(size=15, weight='bold')
        self.__option_button = Button(self.__top_frame, font=my_font,
                                      fg='blue', bg='yellow', relief='ridge',
                                      command=self.option_frame)
        self.__option_button.grid(row=0, column=1, sticky=NW)
        self.__usage_button = Button(self.__top_frame, font=my_font,
                                     fg='green', bg='yellow', relief='ridge',
                                     command=self.__open_pdf)
        self.__usage_button.grid(row=0, column=2, sticky=NW)
        self.__launch_button = Button(self.__top_frame, font=my_font,
                                      fg='red', bg='yellow', relief='ridge',
                                      command=self.__open_exe)
        self.__launch_button.grid(row=0, column=3, sticky=NW)
        self.__about_button = Button(self.__top_frame, font=my_font,
                                     fg='brown', bg='yellow', relief='ridge',
                                     command=self.__about_window)
        self.__about_button.grid(row=0, column=4, sticky=NW)
        self.__top_frame.grid(row=0, sticky=NW)
        seperator = Label(self.__root, text=' ' * 20)
        seperator.grid(row=1, sticky=NW)

    def __design_input_frame(self) -> None:
        self.__command_frame = Frame(self.__root)
        my_font = Font(size=20, weight='bold')
        self.__On = Radiobutton(self.__command_frame, font=my_font,
                                value=1, variable=self.karyAsthiti,
                                command=self.__main_object.change)
        self.__On.pack(side=LEFT)
        self.__Off = Radiobutton(self.__command_frame, font=my_font,
                                 value=0, variable=self.karyAsthiti,
                                 command=self.__main_object.change)
        self.__Off.pack(side=LEFT)
        seperator1 = Label(self.__command_frame, text='         ')
        seperator1.pack(side=LEFT)
        self.num = Checkbutton(self.__command_frame,
                               font=Font(size=18, weight='bold'),
                               variable=self.dev_saMkyA, command=self.__main_object.change_num)
        if self.karyAsthiti.get() == 1:
            self.num.pack(side=LEFT)
        self.__command_frame.grid(row=2, column=0, sticky=NW)
        seperator = Label(self.__root, text=' ' * 20)
        seperator.grid(row=3, sticky=NW)
        self.__short_lbl = Label(self.__root,
                                 font=Font(size=12, weight='bold'), fg='purple')
        self.__short_lbl.grid(row=4, column=0, sticky=NW)

    def option_frame(self) -> None:
        self.__option_window = Toplevel(self.__root)
        self.__option_window.title(self.l_data['option'])
        self.__option_window.iconbitmap(r'assets\Icon.ico')
        self.__option_window.geometry('+180+80')
        my_font = Font(root=self.__option_window, size=13, weight='bold')
        self.__lbl = Label(self.__option_window, text=self.l_data['language'],
                           font=my_font, fg='green')
        self.__lbl.grid(row=0, column=0, sticky=NW)
        l_chooser2 = Radiobutton(self.__option_window, text='हिन्दी', font=my_font,
                                 value=1, variable=self.__language,
                                 command=self.__update_lang_data)
        l_chooser2.grid(row=0, column=1, sticky=NW)
        l_chooser1 = Radiobutton(self.__option_window, text='English', font=my_font,
                                 value=0, variable=self.__language,
                                 command=self.__update_lang_data)
        l_chooser1.grid(row=0, column=2, sticky=NW)
        l_chooser3 = Radiobutton(self.__option_window, text='संस्कृतम्', font=my_font,
                                 value=2, variable=self.__language,
                                 command=self.__update_lang_data)
        l_chooser3.grid(row=0, column=3, sticky=NW)
        self.__startup_message = Label(self.__option_window, text=self.l_data['start_label'],
                                       font=Font(root=self.__option_window,
                                                 size=14, weight='bold', underline=1),
                                       fg='brown')
        self.__startup_message.grid(row=1, column=0, sticky=N)
        self.__startup = Label(self.__option_window, text=self.l_data['start_win'],
                               font=my_font, fg='purple')
        self.__startup.grid(row=2, column=0, sticky=NW)
        self.__start1 = Radiobutton(self.__option_window, text=self.l_data['yes'], font=my_font,
                                    variable=self.__startup_window, value=0,
                                    command=lambda: store_registry(0, 'window_start'))
        self.__start1.grid(row=2, column=1, sticky=NW)
        self.__start2 = Radiobutton(self.__option_window, text=self.l_data['no'], font=my_font,
                                    value=1, variable=self.__startup_window,
                                    command=lambda: store_registry(1, 'window_start'))
        self.__start2.grid(row=2, column=2, sticky=NW)
        self.__app_Status = Label(self.__option_window, text=self.l_data['status_main'],
                                  font=my_font, fg='red')
        self.__app_Status.grid(row=3, column=0, sticky=NW)
        self.__def_app1 = Radiobutton(self.__option_window, text=self.l_data['on'], font=my_font,
                                      variable=self.__app_status, value=1,
                                      command=lambda: store_registry(1, 'app_status'))
        self.__def_app1.grid(row=3, column=1, sticky=NW)
        self.__def_app2 = Radiobutton(self.__option_window, text=self.l_data['off'], font=my_font,
                                      value=0, variable=self.__app_status,
                                      command=lambda: store_registry(0, 'app_status'))
        self.__def_app2.grid(row=3, column=2, sticky=NW)
        self.__numStatus = Label(self.__option_window, text=self.l_data['status_num'],
                                 font=my_font, fg='blue')
        self.__numStatus.grid(row=4, column=0, sticky=NW)
        self.__num_app1 = Radiobutton(self.__option_window, text=self.l_data['devanagari'], font=my_font,
                                      variable=self.__num_status, value=1,
                                      command=lambda: store_registry(1, 'num_status'))
        self.__num_app1.grid(row=4, column=1, sticky=NW)
        self.__num_app2 = Radiobutton(self.__option_window, text=self.l_data['roman'], font=my_font,
                                      value=0, variable=self.__num_status,
                                      command=lambda: store_registry(0, 'num_status'))
        self.__num_app2.grid(row=4, column=2, sticky=NW)
        self.__extra = Label(self.__option_window, text=self.l_data['extra'])
        self.__extra.grid(row=5, column=0, sticky=NW)
        self.__option_window.resizable(False, False)
        self.__option_window.mainloop()

    def __set_text(self, c=False):
        if c:
            self.__root.title(self.l_data['app_title'])
            self.__option_window.title(self.l_data['option'])
            self.__lbl.configure(text=self.l_data['language'])
            self.__startup_message.configure(text=self.l_data['start_label'])
            self.__startup.configure(text=self.l_data['start_win'])
            self.__startup_message.configure(text=self.l_data['start_label'])
            self.__start1.configure(text=self.l_data['yes'])
            self.__start2.configure(text=self.l_data['no'])
            self.__app_Status.configure(text=self.l_data['status_main'])
            self.__def_app1.configure(text=self.l_data['on'])
            self.__def_app2.configure(text=self.l_data['off'])
            self.__numStatus.configure(text=self.l_data['status_num'])
            self.__num_app1.configure(text=self.l_data['devanagari'])
            self.__num_app2.configure(text=self.l_data['roman'])
            self.__extra.configure(text=self.l_data['extra'])
        self.__option_button.configure(text=self.l_data['option'])
        self.__usage_button.configure(text=self.l_data['usage_button'])
        self.__launch_button.configure(text=self.l_data['normal_button'])
        self.__about_button.configure(text=self.l_data['about'])
        self.__On.configure(text=self.l_data['on'])
        self.__Off.configure(text=self.l_data['off'])
        self.__short_lbl.configure(text=self.l_data['shortcut_instruction'])
        self.num.configure(text=self.l_data['dev_numbers'])

    def __update_lang_data(self) -> None:
        self.ex = True
        self.l_data = {
            0: en_lng_data, 1: hn_lng_data, 2: sn_lng_data}[self.__language.get()]
        store_registry(self.__language.get(), 'language')
        self.__set_text(True)

    def __about_window(self) -> None:
        about = Tk()
        about.title(self.l_data['about'])
        about.geometry('+140+70')
        about.resizable(False, False)
        about.iconbitmap(r'assets\Icon.ico')
        my_font = Font(root=about, size=16, weight='bold')
        Label(about, text=self.l_data['app_description'],
              font=my_font, fg='brown').pack()
        Label(about, text=self.l_data['shubham_nirmAtA'],
              font=my_font, fg='purple').pack()
        Label(about, text='Email :- devanagaritool@gmail.com',
              font=my_font, fg='blue').pack()
        Label(about, text='© Devanagari Typing Tools',
              font=my_font, fg='green').pack()
        about.mainloop()

    def __open_pdf(self):
        path = 'assets\\' + {1: 'उपयोगकर्ता पुस्तिका.pdf',
                             0: 'User Manual.pdf',
                             2: 'उपयोगकर्तायै पुस्तिका.pdf'}.get(self.__language.get())
        try:
            startfile(path)
        except FileNotFoundError:
            alert('Error! Repair the program from control panel')

    def __open_exe(self):
        path = 'dev.exe'
        try:
            startfile(path)
        except FileNotFoundError:
            alert('Error! Repair the program from control panel')

    def __hide(self, event=None):
        if self.ex:
            self.ex = False
            return
        self.root_status = False
        self.__root.wm_withdraw()

    def close(self, sy=None):
        self.__root.after(80, self.__root.destroy)

    def display(self, t):
        if t == 'about':
            self.__about_window()
        elif t == 'options':
            self.option_frame()
        elif t == 'show':
            self.__root.wm_deiconify()
            self.root_status = True


class Main():
    def __init__(self):
        self.ks = get_registry('app_status')
        self.ds = get_registry('num_status')
        self.window_start_status = get_registry('window_start')
        self.__master = Tk()
        self.__r = Design(self, self.__master)
        self.__ctrl_press_status = False
        self.__main = parivartana()
        self.__main.devanAgari_saMkhyA = bool(self.ds)
        on_press(self.__detect_key)
        add_hotkey('ctrl+shift', lambda: self.change(True))
        add_hotkey('shift+esc', lambda: self.change_num(True))
        on_click(self.__main.clear_all_val)
        on_middle_click(self.__main.clear_all_val)
        on_right_click(self.__main.clear_all_val)
        self.__temp = 10
        menu_options = (
            ('Show Window', None, lambda _: self.__r.display('show')),
            ("Turn On/Off", None, lambda _: self.change(True)),
            ("Change Numeral Mode", None, lambda _: self.change_num(True)),
            ('Options', None, lambda _: self.__r.display('options')),
            ('About', None, lambda _: self.__r.display('about'))
        )
        self.__systray = SysTrayIcon(
            r'assets\Icon.ico', self.__taskbar_text(),
            menu_options, self.__r.close, default_menu_index=1)
        self.__systray.start()
        self.__master.mainloop()

    def __detect_key(self, k):
        if self.ks == 0:
            return
        key = ''
        c = -7
        k = str(k)
        while True:
            if k[c] == '(':
                break
            else:
                key += k[c]
                c -= 1
        key = key[::-1]
        if self.__ctrl_press_status and 'ctrl' not in key:
            self.__ctrl_press_status = False
            return
        if 'shift' in key or 'caps' in key:
            return
        elif 'ctrl' in key:
            self.__ctrl_press_status = True
            return
        if key in '0123456789;$cWweErtTyuqUiIoOpaAsSd&DgGYhHRXjkLlvzxnbNmM.':
            self.__main.vitaraNa(key)
        else:
            self.__main.clear_all_val()

    def change(self, n=None):
        if n:
            self.ks = abs(self.ks-1)
            self.__r.karyAsthiti.set(self.ks)
        else:
            self.ks = self.__r.karyAsthiti.get()
        if self.__temp == self.ks:
            return
        if self.ks == 0:
            self.__r.ex = True
            self.__r.num.pack_forget()
        else:
            self.__r.num.pack(side=LEFT)
        self.__temp = self.ks
        self.__systray.update(hover_text=self.__taskbar_text())
        alert({1: self.__r.l_data['turned_on'],
               0: self.__r.l_data['turned_off']}.get(self.ks))

    def change_num(self, n=None):
        if n:
            self.ds = abs(self.ds-1)
            self.__r.dev_saMkyA.set(self.ds)
        else:
            self.ds = self.__r.dev_saMkyA.get()
        self.__main.devanAgari_saMkhyA = bool(self.ds)
        self.__systray.update(hover_text=self.__taskbar_text())
        alert({1: self.__r.l_data['dev_num_on'],
               0: self.__r.l_data['dev_num_off']}.get(self.ds))

    def __taskbar_text(self) -> str:
        return 'Devanagari Lekhika is '+{1: 'On', 0: 'Off'}.get(self.ks)+'\n' \
            'Numeral Mode is '+{1: 'Devanagari', 0: 'Normal'}.get(self.ds)


if __name__ == '__main__':
    App = Main()
