import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk


def pencere_oluştur(değerler):
    pencere = Gtk.Window()
    pencere.connect("destroy",Gtk.main_quit)
    try:
        pencere.resize(değerler["boyut"][0],değerler["boyut"][1])
    except:
        pencere.maximize()
    try:
        pencere.set_title(değerler["başlık"])
    except:
        pencere.set_title("Başlıksız yazılım")
    try:
        pencere.move(değerler["bölge"])
    except:
        pencere.set_position(Gtk.WindowPosition.CENTER)
    return pencere

def pencere_ekle(pencere,kutu):
    pencere.add(kutu)

def düğme_oluştur(yazı,komut):
    button = Gtk.Button(label=yazı)
    button.connect("clicked",komut)
    return button

def etiket_oluştur(yazı):
    label =  Gtk.Label(label=yazı)
    return label

def etiketi_yenile(etiket,yazı):
    etiket.set_text(yazı)

def satır_oluştur():
    satır = Gtk.Entry()
    return satır

def satır_oku(satır):
    return satır.get_text()

def anahtar_düğmesi_oluştur(yazı,aktif):
    toggle = Gtk.ToggleButton(label=yazı,active=aktif)

def kontrol_düğmesi_oluştur(yazı):
    check = Gtk.CheckButton(label=yazı)

def dikey_kutu_oluştur():
    a = Gtk.VBox()
    a.show_all()
    return a

def yatay_kutu_oluştur():
    a = Gtk.HBox()
    a.show_all()
    return a

def kutuya_ekle(kutu,araç):
    kutu.add(araç)

def çalıştır(pencere):
    pencere.show_all()
    Gtk.main()
