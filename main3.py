# coding: utf-8

import os
import codecs
import sys
import runpy

def read_tr_file(file):
    dosya = open(file,"r")
    read = dosya.readlines()
    print(read)
    return read


def find_spaces(context):
    a = ""
    for x in context:
        if x == "\t":
            a += x
        elif x == "\n":
            a +=x
        elif x == " ":
            a += x
        else:
            break
    return a


def find_word(context,word):
    a = context.find(word)
    if word == context:
        return True
    elif a == 0 and context[a + len(word) + 1].isspace() is True:
        return True
    elif a != 0 and a != -1 and context[a - 1].isspace() is True and context[a + len(word) + 1].isspace() is True:
        return True
    elif a != 0 and a != -1 and context[a - 1] == "=":
        return True

def get_error(error):
  error_dictionary = {"SyntaxError":"Yazım hatası",
"ArithmeticError":"Matematiksel hata",
"LookupError":"Geçersiz yazım",
"AssertionError":"assert ifadesi yanlış kullanılmış",
"AttributeError":"Kullandığınız nitelik yapmak istediğiniz işleme sahip değil",
"EOFEror":"input fonksiyonu herhangi bir değer alamadı",
"ImportError":"Modül çağrılırken bir hata oluştu",
"ModuleNotFoundError":"Çağırmaya çalıştığınız modül bulunamadı",
"IndexError":"Çağırdınız liste elemanı numarası liste eleman sayısından daha fazla",
"KeyError":"Aradığınız elaman sözlükte bulunamadı",
"KeyboardInterrupt":"Kullanıcı yazılımdan istenmeyen bir şekilde ayrıldı",
"MemoryError":"Yeterli hafıza yok",
"NameError":"Ulaşmaya çalıştığınız nitelik bulunamadı",
"NotImplementedError":"Döngü gereğinden uzun süredir çalışıyor",
"OSError":"İşletim sistemine ait bir hata",
"OverflowError":"Yaptığınız aritemetik işlem beklendiğinden çok büyük çıktı",
"RecursionError":"Yazılım ulaşabileceği en fazla tekrar sayısına ulaştı",
"RuntimeError":"Çalışma zamanı hatası",
"StopIteration":"Son elemana ulaşıldı",
"IndentationError":"Boşluk hatası",
"TabError":'Boşluk hatası,Dosyada ilk başta kullandığınız boşluk sistemini değiştirmemelisiniz',
"SystemError":"Derleyici hatası",
"SystemExit":"Kullanıcı yazılımdan sys.exit() kullanarak çıktı",
"TypeError":"Kullandığınız bir veya birden fazla nitelik yapmak istediğiniz işleme sahip değil",
"UnicodeError":"Unicode kodlama hatası,yaptğınız işlemdeki kullandığınız yazı unicode sistemine uygun değil",
"UnicodeEncodeError":"Unicode kodlama sistemine dönüştürmek istediğiniz yazı dönüştürülürken hata oluştu",
"UnicodeDecodeError":"Unicode kodlama sisteminden çevirmek istedğiniz kodlama sistemine çevrilirken hata oluştu",
"ValueError":"Niteliğe verdiğiniz değer uygun değil",
"ZeroDivisionError":"Bir sayıyı sıfıra bölemezsiniz",
"EnvironmentError":"Çevre hatası",
"IOError":"Giriş,Çıkış hatası",
"WindowsError":"Windows hatası",
"BlockingIOError":"Engellenen bir giriş,çıkış işlemi yapıyorsunuz",
"ConnectionError":"Bağlantı hatası",
"BrokenPipeError":"Kırık veri yolu hatası,socket kapalı",
"ConnectionAbortedError":"Bağlantı karşı taraftan kesildi",
"ConnectionRefusedError":"Karşı taraf bağlantıyı reddetti",
"ConnectionResetError":"Karşı taraf bağlantıyı resetledi",
"FileExistsError":"Oluşturmaya çalıştığınız dosya zaten mevcut",
"FileNotFoundError":"Aradığınız dosya bulunamadı",
"IsADirectoryError":"Silmek veya okumak istediğiniz dosya bir klasör",
"NotADirectoryError":"Yaptığınız işlem bu bir klasör olduğundan gerçekleştirilemiyor",
"PermissionError":"Yetki hatası,yapmak istedğiniz işleme ait yetkiye sahip değilsiniz",
"ProcessLookupError":"Ulaşmaya çalıştığınız işlem mevcut değil",
"TimeoutError":"Zaman aşımı hatası,işlem istenilen zamanda gerçekleşmedi",
"Warnig":"Uyarı",
"UserWarning":"Kullanıcı hakkında uyarılar",
#"DeprecationWarning":
"SyntaxWarning":"Yazı dizimi uyarısı",
"RuntimeWarning":"Çalışma zamanı uyarısı",
"FutureWarning":"Gelecekte kullandığınız nitelik/fonksiyon/modül değişebilir",
"ImportWarning":"Çağırılan modül çeşitli hatalar içeriyor olabilir",
"UnicodeWarning":"Unicode kodlama sistemi uyarısı",
"BytesWarning":"Byte sistemi uyarısı"}
  error = str(error)
  print(error_dictionary[error[9:error.find(">")-1]])
  begin_line = error.find("'dosya.py',") + 12
  end_line = error.find(",",begin_line)
  print(error[begin_line:end_line]+".satır")
  begin_line = end_line + 2
  end_line = error.find(",",begin_line)
  print(error[begin_line:end_line]+".sütunda")
  begin_line = end_line + 2
  end_line = error.find(")",begin_line)
  print(error[begin_line:end_line],"bölümünde hata bulundu")


def exec_file(file):
    try:
        runpy.run_path(file)
        print("dosya başarıyla çalıştırıldı")
    except:
        get_error(sys.exc_info())
        print("dosya çalıştırılamadı")

def get_file_parameter():
    return sys.argv[1]

class yorumlayıcı(object):


    def find_character(self,context):
        a = 0
        for x in context:
            if x.isspace() == True:
                a += 1
            else:
                break
        return a * "\t"

    def trans_false(self,context):
        a = context.split()
        if " Yanlış " in a:
            return True
        elif context.find("=Yanlış") != -1:
            return True
        elif context.find("==Yanlış") != -1:
            return True
        else:
            return False

    def trans_true(self,context):
        a = context.split()
        if " Doğru " in a:
            return True
        elif context.find("=Doğru") != -1:
            return True
        elif context.find("==Doğru") != -1:
            return True
        else:
            return False

    def trans_word(self, context, word):
        b = context.find(word)
        if word == context:
            return True
        if b == 0 and context[b+len(word)+1].isspace() == True:
            return True
        if b != 0 and b != -1 and context[b-1].isspace() == True and context[b+len(word)+1].isspace() == True:
            return True


    def execfile(self):
        try:
            runpy.run_path("dosya.py")
            print("dosya başarıyla çalıştırıldı")
        except:
            print(sys.exc_info())
            print("dosya çalıştırılamadı")

    def build(self,dosya):
        self.dosya2=open("dosya.py","w")
        context = read_tr_file(dosya)
        for x in context:
            bn = find_spaces(x)
            x = x.lstrip()
            if x.startswith("içeri_aktar")==True:
                x = x.replace("içeri_aktar","import",1)
            elif x.startswith("herşeyiyle_aktar")== True:
                a = x.split()[1]
                x = "from "+a+" import *"
            elif x.startswith("sınıf("):
                a = x.find("isim=")+5
                b = x[a:].find(")")
                c = x[a:a+b]
                x = "class "+c+"():\n\tdef __init__(self):"
            elif x.startswith("tanımla")==True:
                x = x.replace("tanımla ","def ",1)
                a = x.find("isim=")+5
                b = x[a:].find(",")
                isim = x[a:a+b]
                c = x.find("parametreler=[")+14
                d = x[c:].find("]")
                parametreler = x[c:c+d]
                x = "def "+isim+"(self,"+parametreler+"):"
                if "arayüz_araç" in x:
                    x = x.replace("arayüz_araç","widget",1)
            elif "./ilk_harf_büyüt(" in x:
                x = x.replace("./ilk_harf_büyüt",".capitalize(")
            elif "./kendi" in x:
                x = x.replace("./kendi.","self.")
            elif "./yanlarına_ekle(" in x:
                x = x.replace("./yanlarına_ekle",".center(")
            elif "./yazdır(" in x:
                x = x.replace("./yazdır(","print(",1)
            elif "./giriş" in x:
                x =  x.replace("./giriş","input(",1)
            elif "./say(" in x:
                x = x.replace("./say(",".count(")
            elif "./tür(" in x:
                x = x.replace("./tür(","type(")
            elif "./mutlak(" in x: ##değiştirilecek_kısım_başlangıç
                x = x.replace("./mutlak(","abs(")
            elif "./hepsi(" in x:
                x = x.replace("./hepsi","all(")
            elif "./herhangi(" in x:
                x = x.replace("./herhangi(","any(")
            elif "./mantık(" in x:
                x = x.replace("./mantık(","bool(")
            elif "./çağrılabilir(" in x:
                x = x.replace("./çağırabilir","callable(")
            elif "./kar(" in x:
                x = x.replace("./kar(","chr(")
            elif "./derle(" in x:
                x = x.replace("./derle(","compile(")
                if "kaynak=" in x:
                    x = x.replace("kaynak=","source=")
                if "dosya=" in x:
                    x = x.replace("dosya=","file=")
                if "mod=" in x:
                    x = x.replace("mod=","mode=")
            elif "./karışık(" in x:
                x = x.replace("./karışık(","complex(")
            elif "./nitelik_sil(" in x:
                x = x.replace("./nitelik_sil(","delattr(")
                if "nesne=" in x:
                    x = x.replace("nesne=","object=")
                if "isim=" in x:
                    x = x.replace("isim=","name=")
            elif "./dizin(" in x:
                x = x.replace("./dizin(","dir(")
            elif "./sözlük(" in x:
                x = x.replace("./sözlük(","dict(")
            elif "./bölmod(" in x:
                x = x.replace("bölmod(","divmod(")
            elif "./sayı(" in x:
                x = x.replace("./sayı(","int(")
            elif "./uzunluk(" in x:
                x = x.replace("./uzunluk","len(")
            elif "./sıra(" in x:
                x = x.replace("./sıra(","range(")
            elif "./dizi(" in x:
                x = x.replace("./dizi(","str(")
            elif "./sıkıştır(" in  x:
                x = x.replace("./sıkıştır(","zip(")
            #if bytearray,byte ekle
            elif find_word(x,"Yanlış") ==  True:
                x = x.replace("Yanlış","False")
            elif find_word(x,"Doğru") == True:
                x = x.replace("Doğru","True")
            elif find_word(x.strip(),"devam"):
                x = x.replace("devam","countinue",1)
            elif find_word(x.strip(),"kapat"):
                x = x.replace("kapat","break",1)
            elif find_word(x.strip(),"eğer"):
                x = x.replace("eğer","if")
            elif find_word(x.strip(),"diğer"):
                x = x.replace("diğer","elif")
            elif find_word(x.strip(),"başka"):
                x = x.replace("başka","else",1)
            elif find_word(x.strip(),"küresel"):
                x = x.replace("küresel","global")
            elif find_word(x.strip(),"ise"): #tekrar bakılacak
                x = x.replace("ise","is")
            elif find_word(x.strip(),"değil"): #tekrar bakılacak
                x = x.replace("değil","not")
            elif find_word(x.strip(),"veya"):
                x = x.replace("veya","or")
            elif find_word(x.strip(),"geç"):
                x = x.replace("geç","pass",1)
            elif find_word(x.strip(),"ata"):
                x = x.replace("ata","return",1)
            elif find_word(x.strip(),"ile"):
                x = x.replace("ile"," with ")
            elif find_word(x.strip(),"olarak"):
                x = x.replace("olarak"," as ")
            elif find_word(x.strip(),"hiç"):
                x = x.replace("hiç","None")
            elif find_word(x.strip(),"sil"):
                x = x.replace("sil","del")
            elif find_word(x.strip(),"sonunda"):
                x = x.replace("sonunda","finally",1)
            elif x.startswith("her "):
                a = x.find("için")+5
                b = x.split()
                c = x[a:-1]
                x = "for "+b[1]+" in "+c
            elif "./sona_ekle" in x.strip():
                x = x.replace("./sona_ekle(", ".append(", 1)
            elif "./sondan_çıkart" in x.strip():
                x = x.replace("./sondan_çıkart(", ".pop(", 1)
            elif "./birleştir" in x.strip():
                x = x.replace("./birleştir(",".expand(", 1)
            elif "./hesapla" in x.strip():
                x = x.replace("./hesapla(", ".count(", 1)
            elif "./ekle" in x.strip():
                x = x.replace("./ekle(", ".insert(", 1)
            elif "./dizinle" in x.strip():
                x = x.replace("./dizinle(", ".index(", 1)
            elif "./kaldır" in x.strip():
                x = x.replace("./kaldır(", ".remove(", 1)
            elif "./ters_döndür" in x.strip():
                x = x.replace("./ters_döndür(", ".reverse(", 1)
            elif "./boşluk_kaldır" in x.strip():
                x = x.replace("./boşluk_kaldır(",".strip(")
            elif "./sağ_boşluk_kaldır" in x.strip():
                x = x.replace("./sağ_boşluk_kaldır(",".rstrip(")
            elif "./sol_soy" in x.strip():
                x = x.replace("./sol_boşluk_kaldır(","lstrip(")
            elif "./boşluk_gör" in x.strip():
                x = x.replace("./boşluk_gör(",".isspace(")
            elif  "./ayrıştır" in x.strip():
                x = x.replace("./ayrıştır(",".split(")
            elif "./hepsi" in x.strip():
                x = x.replace("./hepsi(","all(")
            elif "./dosya_oku(" in x.strip():
                a = x.find("./dosya_oku(")+12
                b = x[a:].find(")")
                isim = x[a:a+b]
                x = "open("+isim+'"r").read()'
            else:
                self.dosya2.write("\n")
            self.dosya2.write(bn+x.rstrip())
        self.dosya2.write("\nYazilim()")
        self.dosya2.close()
        exec_file("dosya.py")

def build_from_software(path):
    yorumlayıcı().build(dosya=path)



if __name__ == "__main__":
    yorumlayıcı().build(dosya=get_file_parameter())
