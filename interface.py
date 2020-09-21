import gi
gi.require_version("Gtk","3.0")
gi.require_version("GtkSource","3.0")
import os
import main

from gi.repository import Gtk
from gi.repository import GtkSource
from gi.repository import Gdk


class Notepad2(Gtk.HBox):
    def __init__(self, *args, **kwargs):
        super(Notepad2, self).__init__(*args, **kwargs)

        self.label = Gtk.Label(label="Yeni sayfa")

        self.close_image = Gtk.Image()
        self.close_image.set_from_file("close.png")
        self.close_button = Gtk.Button()
        self.close_button.set_image(self.close_image)

        self.add(self.label)
        self.add(self.close_button)
        self.show_all()


class Notepad(Gtk.VBox):
    def __init__(self, *args, **kwargs):
        super(Notepad, self).__init__(*args, **kwargs)

        self.scrolled = Gtk.ScrolledWindow()
        self.scrolled.set_hexpand(True)
        self.scrolled.set_vexpand(True)
        self.sourceview = GtkSource.View()
        self.sourcebuffer = self.sourceview.get_buffer()
        self.sourceview.set_show_line_numbers(True)
        self.sourceview.set_smart_home_end(0)
        self.sourceview.set_auto_indent(True)
        self.scrolled.add(self.sourceview)
        self.sourcebuffer.set_highlight_syntax(True)
        self.sourcebuffer.set_highlight_matching_brackets(True)
        start, end = self.sourcebuffer.get_bounds()
        self.sourcebuffer.ensure_highlight(start, end)
        self.sourcelanguagemanager = GtkSource.LanguageManager()
        lang = self.sourcelanguagemanager.get_default()
        abc = self.sourcelanguagemanager.get_language("python")
        self.sourcebuffer.set_language(abc)
        self.sourcestyle = GtkSource.Style()
        self.sourcestylescheme = GtkSource.StyleScheme()
        self.sourcestyleschememanager = GtkSource.StyleSchemeManager()
        self.sourcestyleschememanager.append_search_path(os.getcwd())
        style = self.sourcestyleschememanager.get_scheme("oblivion")
        self.sourcebuffer.set_style_scheme(style)
        self.sourcesearch = GtkSource.SearchContext.new(self.sourcebuffer)
        self.sourcesearchsettings = GtkSource.SearchSettings()
        self.sourcesearch.set_settings(self.sourcesearchsettings)
        self.sourcesearch.set_highlight(True)
        self.textiter = Gtk.TextIter()

        self.searchtoolbar = Gtk.Toolbar()



        self.toolitem = Gtk.ToolItem()
        self.search_bar = Gtk.Entry()
        self.search_bar.set_width_chars(30)
        self.toolitem.add(self.search_bar)
        self.searchtoolbar.insert(self.toolitem, -1)

        self.toolitem2 = Gtk.ToolItem()
        self.search_bar_button = Gtk.Button(label="Ara")
        self.search_bar_button.connect("clicked",self.search)
        self.toolitem2.add(self.search_bar_button)
        self.searchtoolbar.insert(self.toolitem2, -1)

        self.toolitem_case_sensitive = Gtk.ToolItem()
        self.case_sensitive_button = Gtk.ToggleButton(label="Büyük küçük ayrımı")
        self.case_sensitive_button.connect("toggled",self.case_sensitive_toogled)
        self.toolitem_case_sensitive.add(self.case_sensitive_button)
        self.searchtoolbar.insert(self.toolitem_case_sensitive, -1)

        self.toolitem3 = Gtk.ToolItem()
        self.search_bar_button = Gtk.Button(label="Çık")
        self.search_bar_button.connect("clicked",self.search_bar_close)
        self.toolitem3.add(self.search_bar_button)
        self.searchtoolbar.insert(self.toolitem3, -1)

        self.replacetoolbar = Gtk.Toolbar()

        self.toolitem4 = Gtk.ToolItem()
        self.replace_entry_1 = Gtk.Entry()
        self.replace_entry_1.set_width_chars(30)
        self.toolitem4.add(self.replace_entry_1)
        self.replacetoolbar.insert(self.toolitem4, 0)

        self.toolitem5 = Gtk.ToolItem()
        self.replace_entry_2 = Gtk.Entry()
        self.replace_entry_2.set_width_chars(30)
        self.toolitem5.add(self.replace_entry_2)
        self.replacetoolbar.insert(self.toolitem5, -1)

        self.toolitem6 = Gtk.ToolItem()
        self.search_bar_button = Gtk.Button(label="Değiştir")
        self.search_bar_button.connect("clicked",self.replace_text)
        self.toolitem6.add(self.search_bar_button)
        self.replacetoolbar.insert(self.toolitem6, -1)

        self.toolitem7 = Gtk.ToolItem()
        self.search_bar_button = Gtk.Button(label="Çık")
        self.search_bar_button.connect("clicked",self.replace_bar_close)
        self.toolitem7.add(self.search_bar_button)
        self.replacetoolbar.insert(self.toolitem7, -1)

        self.pack_start(self.scrolled, True, True, 0)
        self.pack_start(self.searchtoolbar, False, True, 0)
        self.pack_start(self.replacetoolbar, False, True, 0)

        self.show()
        self.searchtoolbar.hide()
        self.replacetoolbar.hide()
        self.scrolled.show_all()

    def search(self, widget):
        a = self.search_bar.get_text()
        self.sourcesearchsettings.set_search_text(a)

    def search_bar_close(self,widget):
        self.searchtoolbar.hide()

    def replace_bar_close(self,widget):
        self.replacetoolbar.hide()

    def replace_text(self,widget):
        replace_text = self.replace_entry_1.get_text()
        replace_text2 = self.replace_entry_2.get_text()
        text = self.sourcebuffer.get_text(self.sourcebuffer.get_start_iter(),self.sourcebuffer.get_end_iter(),True)
        if replace_text in text:
            text = text.replace(replace_text,replace_text2,1)
        self.sourcebuffer.set_text(text)

    def case_sensitive_toogled(self,widget):
        if widget.get_active():
            self.sourcesearchsettings.set_case_sensitive(True)
        else:
            self.sourcesearchsettings.set_case_sensitive(False)



class Editor(Gtk.VBox):
    def __init__(self, *args, **kwargs):
        super(Editor, self).__init__(*args, **kwargs)
        self.header_bar = Gtk.HeaderBar()
        self.header_bar.set_show_close_button(False)

        self.new_page_button = Gtk.ToolButton()
        self.new_page_button.set_label("Yeni sayfa")
        self.new_page_button.connect("clicked", self.new_page)
        self.new_page_button.set_tooltip_text("Boş bir sayfa aç")
        self.header_bar.add(self.new_page_button)

        self.open_page_button = Gtk.ToolButton()
        self.open_page_button.set_label("Oku")
        self.open_page_button.connect("clicked", self.open_page)
        self.open_page_button.set_tooltip_text("Bir dosyayı içe aktar")
        self.header_bar.add(self.open_page_button)

        self.save_page_button = Gtk.ToolButton()
        self.save_page_button.set_label("Kaydet")
        self.save_page_button.connect("clicked", self.save_page)
        self.save_page_button.set_tooltip_text("Dosyayı kaydet")
        self.header_bar.add(self.save_page_button)

        self.undo_page_button = Gtk.ToolButton()
        self.undo_page_button.set_label("Geri al")
        self.undo_page_button.connect("clicked", self.undo_page)
        self.undo_page_button.set_tooltip_text("Yapılan işlemi geri al")
        self.header_bar.add(self.undo_page_button)

        self.redo_page_button = Gtk.ToolButton()
        self.redo_page_button.set_label("İleri al")
        self.redo_page_button.connect("clicked", self.redo_page)
        self.redo_page_button.set_tooltip_text("Geri alınan işlemi tekrar yap")
        self.header_bar.add(self.redo_page_button)

        self.separator = Gtk.SeparatorToolItem()
        self.header_bar.add(self.separator)

        self.search_page_button = Gtk.ToolButton()
        self.search_page_button.set_label("Arama")
        self.search_page_button.connect("clicked", self.search_page)
        self.search_page_button.set_tooltip_text("Sayfada arama yap")
        self.header_bar.add(self.search_page_button)

        self.replace_page_button = Gtk.ToolButton()
        self.replace_page_button.set_label("Değiştir")
        self.replace_page_button.connect("clicked", self.replace_page)
        self.replace_page_button.set_tooltip_text("Sayfada arama yap")
        self.header_bar.add(self.replace_page_button)

        self.run_software_button = Gtk.ToolButton()
        self.run_software_button.set_label("Çalıştır")
        self.run_software_button.connect("clicked",self.run_software)
        self.run_software_button.set_tooltip_text("Yazılımı çalıştır")
        self.header_bar.add(self.run_software_button)

        self.header_bar.show_all()

        self.notebook = Gtk.Notebook()

        self.notebook.set_scrollable(True)
        self.notebook.set_show_tabs(True)
        self.notebook.set_show_border(True)

        self.tabs = []
        page = self.create_page()
        header = self.create_title()
        header.close_button.connect("clicked",self.close_page,page)

        self.tabs.append((page, header))

        self.notebook.append_page(*self.tabs[0])


        self.pack_start(self.header_bar, False, True, 0)
        self.pack_start(self.notebook, True, True, 0)
        self.notebook.show()


        self.show()


    def create_page(self):
        notepad = Notepad()
        notepad.searchtoolbar.hide()
        notepad.replacetoolbar.hide()
        return notepad


    def create_title(self):
        notepad2 = Notepad2()
        return notepad2

    def new_page(self, widget):
        current_page = self.notebook.get_current_page()
        page = self.create_page()
        header = self.create_title()
        header.close_button.connect("clicked",self.close_page,page)
        page_tuple = (page, header)
        self.tabs.insert(current_page + 1, page_tuple)
        self.notebook.insert_page(page_tuple[0], page_tuple[1], current_page + 1)
        self.notebook.set_current_page(current_page + 1)

    def new_page2(self, *args):
        current_page = self.notebook.get_current_page()
        page = self.create_page()
        header = self.create_title()
        header.close_button.connect("clicked",self.close_page,page)
        page_tuple = (page, header)
        self.tabs.insert(current_page + 1, page_tuple)
        self.notebook.insert_page(page_tuple[0], page_tuple[1], current_page + 1)
        self.notebook.set_current_page(current_page + 1)

    def close_page(self, widget,page):
        a = self.notebook.get_n_pages()
        if a == 1:
            Gtk.main_quit()
        else:
            delete_page = self.notebook.page_num(page)
            self.notebook.remove_page(delete_page)

    def close_current_page(self, *args):
        delete_page = self.notebook.get_current_page()
        self.notebook.remove_page(delete_page)

    def open_page(self, widget):
        self.new_page(self)
        filechooserdialog = Gtk.FileChooserDialog(title="Dosya aç")

        filechooserdialog.add_button("İptal", Gtk.ResponseType.CANCEL)
        filechooserdialog.add_button("Aç", Gtk.ResponseType.OK)

        response = filechooserdialog.run()

        if response == Gtk.ResponseType.OK:
            file_chooser_path = filechooserdialog.get_filename()
            global file_chooser_path
            current_page = self.notebook.get_current_page()
            self.tabs[current_page][1].label.set_text(file_chooser_path)
            dosya = open(file_chooser_path)
            b = dosya.read()
            current_page = self.notebook.get_current_page()
            self.tabs[current_page][0].sourcebuffer.set_text(b)
            self.notebook.set_current_page(current_page + 1)

        filechooserdialog.destroy()

    def save_page(self, widget):
        current_page = self.notebook.get_current_page()
        start, end = self.tabs[current_page][0].sourcebuffer.get_bounds()
        text = self.tabs[current_page][0].sourcebuffer.get_text(start, end, False)
        filename = self.tabs[current_page][1].label.get_text()
        if filename == "Yeni sayfa":
            filechooserdialog = Gtk.FileChooserDialog("Dosyayı Kaydet",None,Gtk.FileChooserAction.SAVE)
            filechooserdialog.add_button("İptal", Gtk.ResponseType.CANCEL)
            filechooserdialog.add_button("Kaydet", Gtk.ResponseType.OK)
            response = filechooserdialog.run()
            if response == Gtk.ResponseType.OK:
                file_chooser_path = filechooserdialog.get_filename()
                dosya = open(file_chooser_path, "w")
                self.tabs[current_page][1].label.set_text(file_chooser_path)
                dosya.write(text)
                dosya.close()
            filechooserdialog.destroy()
        else:
            dosya = open(filename,"w")
            dosya.write(text)
            dosya.close()

    def save_current_page(self, *args):
        current_page = self.notebook.get_current_page()
        start, end = self.tabs[current_page][0].sourcebuffer.get_bounds()
        text = self.tabs[current_page][0].sourcebuffer.get_text(start, end, False)
        filename = self.tabs[current_page][1].label.get_text()
        if filename == "Yeni sayfa":
            filechooserdialog = Gtk.FileChooserDialog("Dosyayı Kaydet",None,Gtk.FileChooserAction.SAVE)
            filechooserdialog.add_button("İptal", Gtk.ResponseType.CANCEL)
            filechooserdialog.add_button("Kaydet", Gtk.ResponseType.OK)
            response = filechooserdialog.run()
            if response == Gtk.ResponseType.OK:
                file_chooser_path = filechooserdialog.get_filename()
                dosya = open(file_chooser_path, "w")
                self.tabs[current_page][1].label.set_text(file_chooser_path)
                dosya.write(text)
                dosya.close()
            filechooserdialog.destroy()
        else:
            dosya = open(filename,"w")
            dosya.write(text)
            dosya.close()

    def undo_page(self, widget):
        current_page = self.notebook.get_current_page()
        a = self.tabs[current_page][0].sourcebuffer.can_undo()
        if a == True:
            self.tabs[current_page][0].sourcebuffer.undo()
        else:
            pass

    def undo_current_page(self, *args):
        current_page = self.notebook.get_current_page()
        a = self.tabs[current_page][0].sourcebuffer.can_undo()
        if a == True:
            self.tabs[current_page][0].sourcebuffer.undo()
        else:
            pass

    def redo_page(self, widget):
        current_page = self.notebook.get_current_page()
        a = self.tabs[current_page][0].sourcebuffer.can_redo()
        if a == True:
            self.tabs[current_page][0].sourcebuffer.redo()
        else:
            pass

    def redo_current_page(self, *args):
        current_page = self.notebook.get_current_page()
        a = self.tabs[current_page][0].sourcebuffer.can_redo()
        if a == True:
            self.tabs[current_page][0].sourcebuffer.redo()
        else:
            pass

    def search_page(self, widget):
        current_page = self.notebook.get_current_page()
        self.tabs[current_page][0].replacetoolbar.hide()
        self.tabs[current_page][0].searchtoolbar.show_all()

    def search_page2(self, *args):
        current_page = self.notebook.get_current_page()
        self.tabs[current_page][0].replacetoolbar.hide()
        self.tabs[current_page][0].searchtoolbar.show_all()

    def replace_page(self, widget):
        current_page = self.notebook.get_current_page()
        self.tabs[current_page][0].searchtoolbar.hide()
        self.tabs[current_page][0].replacetoolbar.show_all()

    def replace_page2(self, *args):
        current_page = self.notebook.get_current_page()
        self.tabs[current_page][0].searchtoolbar.hide()
        self.tabs[current_page][0].replacetoolbar.show_all()

    def run_software(self,button):
        current_page = self.notebook.get_current_page()
        temp_file = open("temp_file.py","w")
        start = self.tabs[current_page][0].sourcebuffer.get_start_iter()
        end = self.tabs[current_page][0].sourcebuffer.get_end_iter()
        text = self.tabs[current_page][0].sourcebuffer.get_text(start,end,False)
        temp_file.write(text)
        temp_file.close()
        main.build_from_software("temp_file.tr")

class About_Screen(Gtk.AboutDialog):
    def __init__(self, *args, **kwargs):
        super(About_Screen, self).__init__(*args, **kwargs)

        self.set_program_name("Python3Tr programlama dili")
        self.set_version(str(0.9))
        self.set_comments(
            "Türk insanın daha kolay programlama öğrenebilmesi için python dilinin türkçelendirme çalışmasıdır")
        self.set_authors(["Samet Burgazoğlu"])

        image = Gtk.Image()
        image.set_from_file("gezgin.png")
        image2 = image.get_pixbuf()
        self.set_logo(image2)

        self.run()
        self.destroy()

class Interface(object):
    def __init__(self,widget):
        self.widget = widget
        self.project_path = ""
        self.project_name = ""
        self.ana_ekran = Gtk.VBox()

        self.new_project_screen = Gtk.VBox()
        self.new_project_name_box = Gtk.HBox()
        self.new_project_path_box = Gtk.HBox()
        self.new_project_name_entry = Gtk.Entry()
        self.new_project_name_entry.set_width_chars(50)
        self.new_project_name_label = Gtk.Label(label="proje adı")
        self.new_project_name_label.set_name('label')
        self.new_project_name_box.pack_start(self.new_project_name_label,False,False,0)
        self.new_project_name_box.pack_start(self.new_project_name_entry,False,False,0)
        self.new_project_path_entry = Gtk.Entry()
        self.new_project_path_entry.set_width_chars(50)
        self.new_project_path_entry.set_text(os.environ['HOME']+"/")
        self.new_project_path_label = Gtk.Label(label="proje yolu")
        self.new_project_path_label.set_name('label')
        self.new_project_path_box.pack_start(self.new_project_path_label,False,False,0)
        self.new_project_path_box.pack_start(self.new_project_path_entry,False,False,0)
        self.new_project_create_button = Gtk.Button(label="oluştur")
        self.new_project_create_button.set_name('button')
        self.new_project_create_button.connect("clicked",self.start_editor)
        self.new_project_screen.pack_start(self.new_project_name_box,False,False,0)
        self.new_project_screen.pack_start(self.new_project_path_box,False,False,0)
        self.new_project_screen.pack_start(self.new_project_create_button,False,False,0)
        self.new_project_screen.show_all()

        self.giris_ekran = Gtk.VBox()
        self.image = Gtk.Image()
        self.image.set_from_file("gezgin.png")
        self.name_application = Gtk.Label(label="TrProg")
        self.version_application = Gtk.Label(label="0.9 BETA")
        self.new_project = Gtk.Button(label="Yeni proje oluştur")
        self.open_project = Gtk.Button(label="Yeni proje aç")
        self.settings = Gtk.Button(label="Ayarlar")
        self.about_us = Gtk.Button(label="Hakkımızda")
        self.exit = Gtk.Button(label="Çıkış")

        self.name_application.set_name('button')
        self.version_application.set_name('button')
        self.new_project.set_name('button')
        self.open_project.set_name('button')
        self.settings.set_name('button')
        self.about_us.set_name('button')
        self.exit.set_name('button')

        self.exit.connect("pressed",self.kapat)
        self.about_us.connect("pressed",About_Screen)
        self.new_project.connect("pressed",self.create_new_project)
        self.open_project.connect("pressed",self.open_new_project)

        self.giris_ekran.pack_start(self.image,False,False,0)
        self.giris_ekran.pack_start(self.new_project,False,False,0)
        self.giris_ekran.pack_start(self.open_project,False,False,0)
        self.giris_ekran.pack_start(self.settings,False,False,0)
        self.giris_ekran.pack_start(self.about_us,False,False,0)
        self.giris_ekran.pack_start(self.exit,False,False,0)
        self.giris_ekran.pack_start(self.name_application,False,False,0)
        self.giris_ekran.pack_start(self.version_application,False,False,0)

        self.editor_screen = Editor()
        self.ana_ekran.add(self.giris_ekran)

        self.accel = Gtk.AccelGroup()
        self.accel.connect(Gdk.keyval_from_name('z'), Gdk.ModifierType.CONTROL_MASK, 0, self.editor_screen.undo_current_page)
        self.accel.connect(Gdk.keyval_from_name('x'), Gdk.ModifierType.CONTROL_MASK, 0, self.editor_screen.redo_current_page)
        self.accel.connect(Gdk.keyval_from_name('c'), Gdk.ModifierType.CONTROL_MASK, 0, self.editor_screen.close_current_page)
        self.accel.connect(Gdk.keyval_from_name('s'), Gdk.ModifierType.CONTROL_MASK, 0, self.editor_screen.save_current_page)
        self.accel.connect(Gdk.keyval_from_name('n'), Gdk.ModifierType.CONTROL_MASK, 0, self.editor_screen.new_page2)
        self.accel.connect(Gdk.keyval_from_name('f'), Gdk.ModifierType.CONTROL_MASK, 0, self.editor_screen.search_page2)
        self.accel.connect(Gdk.keyval_from_name('r'), Gdk.ModifierType.CONTROL_MASK, 0, self.editor_screen.replace_page2)
        self.widget.add_accel_group(self.accel)

        ###Tema düzenleme
        style_provider = Gtk.CssProvider()

        style_provider.load_from_path("theme.css")

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        ###


        self.widget.add(self.ana_ekran)
        self.ana_ekran.show_all()

    def kapat(self,widget):
        Gtk.main_quit()
        exit()

    def create_new_project(self,widget):
        self.ana_ekran.remove(self.giris_ekran)
        self.ana_ekran.add(self.new_project_screen)


    def start_editor(self,widget):
        path = self.new_project_path_entry.get_text()
        name = self.new_project_name_entry.get_text()
        project_path = path+name
        os.mkdir(project_path)
        current_path = os.getcwd()
        os.chdir(project_path)
        os.system("touch main.py")
        os.chdir(current_path)
        current_page = self.editor_screen.notebook.get_current_page()
        self.editor_screen.tabs[current_page][1].label.set_text(project_path+"/"+"main.py")
        self.ana_ekran.remove(self.new_project_screen)
        self.ana_ekran.add(self.editor_screen)
        self.widget.maximize()

    def open_new_project(self,widget):

        filechooserdialog = Gtk.FileChooserDialog(title="Yeni proje aç")

        filechooserdialog.add_button("İptal", Gtk.ResponseType.CANCEL)
        filechooserdialog.add_button("Aç", Gtk.ResponseType.OK)

        response = filechooserdialog.run()

        if response == Gtk.ResponseType.OK:
            file_chooser_path = filechooserdialog.get_filename()
            self.project_path = file_chooser_path
            current_page = self.editor_screen.notebook.get_current_page()
            self.editor_screen.tabs[current_page][1].label.set_text(file_chooser_path)
            dosya = open(file_chooser_path)
            b = dosya.read()
            current_page = self.editor_screen.notebook.get_current_page()
            self.editor_screen.tabs[current_page][0].sourcebuffer.set_text(b)
            self.editor_screen.notebook.set_current_page(current_page + 1)
            self.ana_ekran.remove(self.giris_ekran)
            self.ana_ekran.add(self.editor_screen)
            self.widget.maximize()
        filechooserdialog.destroy()


if __name__=='__main__':
    win = Gtk.Window()
    win.set_default_size(300,50)
    win.set_name('interface')
    win.connect("destroy", Gtk.main_quit)
    win.set_size_request(500, 500)
    win.move(300,100)
    bar=Interface(win)
    win.show()
    Gtk.main()