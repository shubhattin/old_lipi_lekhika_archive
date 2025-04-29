from keyboard import press_and_release, write
from math import ceil
swara = 'अआइ़ईउऊएऔओःॅ'
mAtrA = {
    'a': '',
    "ाW": "ॉ",
    'A': 'ा',
    'i': 'ि',
    'I': 'ी',
    'u': 'ु',
    'U': 'ू',
    'e': 'े',
    'E': 'ै',
    'o': 'ो',
    'O': 'ौ',
    'ृR': 'ॄ',
    'R': 'ृ',
    "ॢR": "ॣ",
    "X": "ॢ"
}

saMkhyA = {
    '0': '०',
    '1': '१',
    '2': '२',
    '3': '३',
    '4': '४',
    '5': '५',
    '6': '६',
    '7': '७',
    '8': '८',
    '9': '९'
}

eka_varNAH = {
    '₹': '&',
    '॒': 'q',
    'c': 'c',
    'S': 'S',
    'w': 'w',
    'x': 'x',
    'ग्': 'g',
    'ङ्': 'G',
    'ज्': 'j',
    'ञ्': 'Y',
    'ट्': 'T',
    'ड्': 'D',
    'ण्': 'N',
    'त्': 't',
    'द्': 'd',
    'न्': 'n',
    'प्': 'p',
    'ब्': 'b',
    'म्': 'm',
    'य्': 'y',
    'र्': 'r',
    'ल्': 'l',
    'व्': 'v',
    'क्': 'k',
    'स्': 's',
    'ह्': 'h',
    'ळ्': 'L',
    '।': '.',
    'अ': 'a',
    'आ': 'A',
    'इ': 'i',
    'ई': 'I',
    'उ': 'u',
    'ऊ': 'U',
    'ए': 'e',
    'ऐ': 'E',
    'ओ': 'o',
    'औ': 'O',
    'ं': 'M',
    'ॅ': 'W',
    'ः': 'H',
    'ऋ': 'R',
    'ऌ': 'X',
}

dvi_varNAH = {
    "ऑ": "आW",
    "आऊ": "आU",
    'ॡ': 'ऌR',
    "ऍ": "एW",
    'ॠ': 'ऋR',
    'ऽ': 'आw',
    'ख्': 'क्h',
    'घ्': 'ग्h',
    'च्': 'ch',
    'झ्': 'ज्h',
    'ठ्': 'ट्h',
    'ढ्': 'ड्h',
    'थ्': 'त्h',
    'फ्': 'प्h',
    'भ्': 'ब्h',
    'श्': 'स्h',
    'ष्': 'Sh',
    'ध्': 'द्h',
    'ड़्': 'ड्x',
    'ढ़्': 'ढ्x',
    'ँ': 'ंM',
    '॥': '।.'
}

tri_varNAH = {
    'छ्': 'च्h',
    'ॐ': 'आऊM',
}


def antaH_parivartan(js):
    ret = {}
    for k in js:
        ret[js[k]] = k
    return ret

eka_varNAH = antaH_parivartan(eka_varNAH)
dvi_varNAH = antaH_parivartan(dvi_varNAH)
tri_varNAH = antaH_parivartan(tri_varNAH)

class parivartana:
    def __init__(self):
        self.devanAgari_saMkhyA = False
        self.__varNAH = ''
        self.__varNAH_count = 0
        self.__nuktA_sthiti = 0
        self.__mAtrA_sthiti = 0
        self.__break_status = False
        self.__mAtrA_add_status = False

    def vitaraNa(self, k):
        if self.__mAtrA_add_status:
            self.clear_all_val()
            if k in 'AiIuUeEoORX':
                self.__back(1)
                write(mAtrA.get(k))
                return
            elif k == '$':
                self.__back(1)
                write('्')
                return
        if self.__mAtrA_sthiti >= 1 and k not in 'RW' :
            self.clear_all_val() 
        if k in eka_varNAH and self.__varNAH_count == 0:
            self.__varNAH_count = 1
            self.__nuktA_sthiti = 0
            self.__mAtrA_sthiti = 0
            a = eka_varNAH.get(k)               
            if self.__varNAH != '' and self.__varNAH[-1] == '्' and k in mAtrA:
                a = mAtrA.get(k)
                self.__varNAH += a
                self.__mAtrA_sthiti = 1
            else:
                self.__varNAH = a
            if a in swara and a != 'आ' or k in 'GYnNmyrlvh':
                self.__varNAH_count = 0
            self.__back(1 if self.__break_status else 0)
            self.__break_status = False
            write(a)
        elif k in eka_varNAH and self.__varNAH_count == 1:
            if self.__mAtrA_sthiti == 1:
                a = mAtrA.get(self.__varNAH[-1]+k)
                if a == None:
                    self.clear_all_val()
                    self.vitaraNa(k)
                    return
                self.clear_all_val()
                self.__back(1)                
                write(a)  
                return
            a = dvi_varNAH.get(self.__varNAH+k)              
            if a == None:
                self.__varNAH_count = 0
                self.vitaraNa(k)
                return                                                      
            self.__varNAH = a
            self.__back(2 - (1 if  a == 'च्' or a == 'ष्' or k in 'UMR.w' else 0))
            self.__varNAH_count = 2
            if a == 'ढ्':
                self.__varNAH_count = 1
            write(a)
        elif k in eka_varNAH and self.__varNAH_count == 2:
            a = tri_varNAH.get(self.__varNAH + k)
            if a == None:
                self.__varNAH_count = 0
                self.vitaraNa(k)
                return
            self.__back(2)
            self.__varNAH_count = 0
            write(a)
        elif k == 'z' and self.__varNAH != '' and self.__varNAH[-1] == '्':
            self.__back(1)
            write('़्')
            self.__nuktA_sthiti = 1
        elif k == ';':
            self.clear_all_val()
            self.__break_status = True
        elif k == '$':
            self.clear_all_val()
            self.__mAtrA_add_status = True
        elif k in saMkhyA and self.devanAgari_saMkhyA:
            self.__back()
            write(saMkhyA.get(k))
    
    def clear_all_val(self):
        self.__varNAH = ''
        self.__varNAH_count = 0
        self.__nuktA_sthiti = 0
        self.__mAtrA_sthiti = 0
        self.__break_status = False
        self.__mAtrA_add_status = False

    def __back(self, n = 0):
        n += ceil((self.__mAtrA_sthiti + self.__nuktA_sthiti) / 2)
        for v in range(0, n + 1):                                    
            press_and_release('backspace')