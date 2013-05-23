from gettext import gettext as _
from gi.repository import Gtk
        
class Home(Gtk.ScrolledWindow):
    def __init__(self, parent):
        Gtk.ScrolledWindow.__init__(self)
        self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add_with_viewport(self.box)
        self.switches = {}
        self.switches['fixJoinedLetters'] = self.create_item('Fix joined letters','bla bla bla\nblablabla')
        self.box.pack_start(Gtk.Separator(), True, False, 0)
        self.switches['firefoxFonts'] = self.create_item('Firefox fonts','bla bla bla')        
        self.box.pack_start(Gtk.Separator(), True, False, 0)
        self.switches['ubuntuDefaultFonts'] = self.create_item('Ubuntu default fonts','bla bla bla')
        self.box.pack_start(Gtk.Separator(), True, False, 0)
        self.switches['centeringWindows'] = self.create_item('Centering windows','bla bla bla')
        self.box.pack_start(Gtk.Separator(), True, False, 0)
        self.switches['videoSubtitlesEnconding'] = self.create_item('Video subtitles encoding','bla bla bla')
        self.box.pack_start(Gtk.Separator(), True, False, 0)
        self.switches['multimediaCodecs'] = self.create_item('Multimedia codecs','bla bla bla')
        self.box.pack_start(Gtk.Separator(), True, False, 0)
        self.switches['ubuntuRestrictedExtras'] = self.create_item('Ubuntu restricted extras','bla bla bla')
        self.box.pack_start(Gtk.Separator(), True, False, 0)
        self.switches['javaBundle'] = self.create_item('Java bundle','bla bla bla')
        self.box.pack_start(Gtk.Separator(), True, False, 0)
        self.switches['libreOffice'] = self.create_item('Libre Office','bla bla bla')
    
    def create_item(self, name, desc):
        box = Gtk.Box()        
        switch = Gtk.Switch()
        expander = ItemExpander(_(name), _(desc))
        box.pack_start(expander, False, False, 0)
        box.pack_start(Gtk.Label(''), True, False, 0)
        box.pack_start(switch, False, False, 0)
        self.box.pack_start(box, True, False, 0)
        return switch
        

class ItemExpander(Gtk.Expander):
    def __init__(self,label,desc):
        Gtk.Expander.__init__(self)
        self.set_resize_toplevel(False)
        self.set_label(label)    
        dsc = Gtk.Label(desc)
        self.add(dsc)
