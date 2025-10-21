import sys
class spojak:
    def __init__(self,hod,next=None):
        self.hod=hod
        self.next=next

class spojs:
    def __init__(self):
        self.zacatek=None
        self.konec=None

    def pridej_na_zacatek(self,co):
        self.zacatek=spojak(co,self.zacatek)
        if(self.konec==None):
            self.konec=self.zacatek

    def pridej_na_konec(self,co):
        if self.konec!=None:
            self.konec.next=spojak(co)
            self.konec=self.konec.next
        else:   
            self.pridej_na_zacatek(co)

    def smaz_prvni_prvek(self):
        if(self.zacatek!=None):
            hod=self.zacatek.hod
            self.zacatek=self.zacatek.next
            if(self.zacatek==None):
                self.konec=None
            return hod
        else:
            return 
        
    def mazej_kulisaku(self):
        if self.zacatek:
            self.zacatek = self.zacatek.next
        
    def dej_mi_prvniho(self):
        if self.zacatek:
            return self.zacatek.hod
        else:
            return None

    def dej_mi_druhyho(self):
        if self.zacatek and self.zacatek.next:
            return self.zacatek.next.hod
        else:
            return None
    
    def vypis(self):
        tenhle = self.zacatek
        while tenhle != None:
            print(tenhle.hod,end="")
            tenhle = tenhle.next

    def vice_cisel_na_vysledek(self):
        if self.zacatek and self.zacatek.next:
            print("Chyba!")
        if not self.zacatek.next:
            s.vypis()

s = spojs()

while True:
    i = sys.stdin.read(1)
    if not i or (i=="\n" and sys.stdin.read(1)=="\n"):
        break
    else:
        if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
            zatim = 0
            while ord(i)>=48 and ord(i)<=57:
                zatim = 10*zatim + ord(i)-48
                i = sys.stdin.read(1)
            s.pridej_na_zacatek(zatim)
        elif i=="+" or i=="-" or i=="*" or i=="/":
            if i=="+":
                try:
                    s.dej_mi_druhyho() + s.dej_mi_prvniho()
                except:
                    print("Chyba!")
                    sys.exit()
                novy = s.dej_mi_druhyho() + s.dej_mi_prvniho()
                s.mazej_kulisaku(), s.mazej_kulisaku()
                s.pridej_na_zacatek(novy)
            elif i=="-":
                try:
                    s.dej_mi_druhyho() - s.dej_mi_prvniho()
                except:
                    print("Chyba!")
                    sys.exit()
                novy = s.dej_mi_druhyho() - s.dej_mi_prvniho()
                s.mazej_kulisaku(), s.mazej_kulisaku()
                s.pridej_na_zacatek(novy)
            elif i=="*":
                try:
                    s.dej_mi_druhyho() * s.dej_mi_prvniho()
                except:
                    print("Chyba!")
                    sys.exit()
                novy = s.dej_mi_druhyho() * s.dej_mi_prvniho()
                s.mazej_kulisaku(), s.mazej_kulisaku()
                s.pridej_na_zacatek(novy)
            elif i=="/":
                try:
                    s.dej_mi_druhyho() // s.dej_mi_prvniho()
                except:
                    print("Chyba!")
                    sys.exit()
                if s.dej_mi_prvniho() == 0:
                    print("Chyba!"), sys.exit()
                novy = s.dej_mi_druhyho() // s.dej_mi_prvniho()
                s.mazej_kulisaku(), s.mazej_kulisaku()
                s.pridej_na_zacatek(novy)
       
s.vice_cisel_na_vysledek()
