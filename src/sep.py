import turkishnlp
import re

tool = turkishnlp.detector.TurkishNLP()

class Turkce():
        
    def seperator(self,sozcuk):
        
        self.sayi1 = 0
        self.sayi2 = 0
        self.sayi3 = 0
        self.sayi4 = 0

        self.sorgulanan_kelime = tool.syllabicate_sentence(sozcuk)

        self.kelimenin_harfleri = re.findall("[a-zA-Z]", sozcuk)

        self.yabanci_harfler = re.findall("[q,w,ğ,j,x,Q,W,Ğ,J,X]", sozcuk)   

        if(len(self.yabanci_harfler) == 0):
            self.sayi1 = 1

        else:
            self.sayi1 = 2

        if(self.sayi1 == 2):
            return False

        elif(self.sayi1 == 1):

            for i in self.kelimenin_harfleri:

                aranan_harf = re.search("[r,t,y,p,s,d,f,g,h,k,l,ş,c,v,b,n,m]", i)

                if aranan_harf:
                    self.sayi2 = self.sayi2 + 1

                else:
                    self.sayi2 = 3
            
                if(self.sayi2 == 2 or self.sayi2 == 5):
                    break
            
            if(self.sayi2 == 2 or self.sayi2 == 5):
                return False 

            elif(self.sayi2 == 3):

                for y in self.kelimenin_harfleri:

                    aranan_harf = re.search("[a,e,ı,i,o,ö,u,ü]", y)

                    if aranan_harf:
                        self.sayi3 = self.sayi3 + 1

                    else:
                        self.sayi3 = 3
                
                    if(self.sayi3 == 2 or self.sayi3 == 5):
                        break
                
                if(self.sayi3 == 2 or self.sayi3 == 5):
                    return False 
                
                else:
                    sorgulanan_heceler = []

                    for z in range(1,len(self.sorgulanan_kelime[0]),1):
                        sorgulanan_heceler.append(self.sorgulanan_kelime[0][z])

                    for k in sorgulanan_heceler:
                        sorgu = re.search("[o,ö]",k)
                                            
                        if sorgu:
                            self.sayi4 = 2
                            break

                        else:
                            self.sayi4 = 1

                    if(self.sayi4 == 2):
                        return False

        if(self.sayi4 == 1):
            return True  

        else:
            print("HATA MEYDANA GELDİ!!!")