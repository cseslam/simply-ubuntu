import os
import sys
from subprocess import call
from gettext import gettext as _
from gi.repository import Gtk, Gio, Gdk
from widgets import *

class Window(Gtk.ApplicationWindow):
    def __init__(self, app, data_dir):
        Gtk.ApplicationWindow.__init__(self, application=app)
        self.set_title(_('Simply Ubuntu'))
        self.set_default_size(640,480)
        self.set_hide_titlebar_when_maximized(True)            
        
        self.data_dir = data_dir
        cssProvider = Gtk.CssProvider()
        #print(os.path.join(data_dir,'simply-ubuntu.css'))
        cssProvider.load_from_path(os.path.join(data_dir,'simply-ubuntu.css'))
        context = Gtk.StyleContext()
        context.add_provider_for_screen(Gdk.Screen.get_default(),
                                        cssProvider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.gsettings = Gio.Settings.new('simply-ubuntu')
        self.layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)        
        self.add(self.layout)
        self.toolbar = toolbar = Toolbar()
        self.home = home = Home(self)
        self.get_settings()
        self.layout.pack_start(toolbar, False, False, 0)
        self.layout.pack_start(home, True, True, 6)
        self.show_all()
        
    def get_settings(self):
        settings = {}
        settings['fixJoinedLetters'] = self.gsettings.get_boolean('fix-joined-letters')
#        self.home.switches['fixLa'].set_active(settings['fixLa'])
        settings['centeringWindows'] = self.gsettings.get_boolean('centering-windows')
        self.home.switches['centeringWindows'].set_active(settings['centeringWindows'])

    def fix_la(self):
        call(['gksu', 'update-alternatives', 'set', 'xinput-all_ALL', '/etc/X11/xinit/xinput.d/default-xim'])
        self.gsettings.set_boolean('fix_la', True)

    def center_windows(self):
        call(['dconf', 'write', '/org/compiz/profiles/unity/plugins/place/mode', '1'])
        self.gsettings.set_boolean('center-windows', True)

    def default_font(self):
        call(['gksu', 'cp', self.data_dir+'69-language-selector-ar.conf', '/etc/fonts/conf.avail'])
        call(['gksu', 'ln', '-s', '/etc/fonts/conf.avail/69-language-selector-ar.conf', '/etc/fonts/conf.d'])

    def ubuntu_restricted_extras(self):
        call(['gksu', 'apt-get', 'install', 'ubuntu-restricted-extras'])

    def install_java(self):
        call(['gksu', 'apt-get', 'install', 'icedtea-plugin'])


class Toolbar(Gtk.Toolbar):
    def __init__(self):
        Gtk.Toolbar.__init__(self)
        self.set_size_request(-1, 42)
        self.get_style_context().add_class('primary-toolbar')
        leftItem = Gtk.ToolItem()
        spacer = Gtk.ToolItem()
        spacer.set_expand(True)
        rightItem = Gtk.ToolItem()
        leftBox = Gtk.Box()
        rightBox = Gtk.Box()
        
        titlebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)        
        title = Gtk.Label(_('Simply Ubuntu'))     
        title.set_property('justify',Gtk.Justification.LEFT)
        title.set_markup('<b>Simply Ubuntu</b>')
        desc = Gtk.Label(_('Simply Ubuntu is an application that aims to ...'))        
        desc.get_style_context().add_class('app-desc')
        desc.set_markup('<small>    Simply Ubuntu is an application that aims to ...</small>')
        titlebox.pack_start(title, False, False, 0)        
        titlebox.pack_end(desc, False, False, 0)        
        
        self.switch = switch = Gtk.Switch()
        switch.connect('notify::active', self.switch_activated)
        leftBox.pack_start(titlebox, False, False, 3)
        rightBox.pack_start(switch, False, False, 3)
        
        leftItem.add(leftBox)
        rightItem.add(rightBox)
        self.insert(leftItem, -1)
        self.insert(spacer,-1)
        self.insert(rightItem, -1)        
                
    def switch_activated(self, switch, active):                        
        parent = self.get_parent().get_parent()        
        for s in parent.home.switches:
            parent.home.switches[s].set_active(switch.get_active())            
   
        
class SimplyUbuntuApplication(Gtk.Application):
    def __init__(self, data_dir):
        Gtk.Application.__init__(self)
        self.data_dir = data_dir
    
    def do_startup(self):
        Gtk.Application.do_startup(self)
        
    def do_activate(self):
        self.win = Window(self, self.data_dir)
        self.win.present()    
