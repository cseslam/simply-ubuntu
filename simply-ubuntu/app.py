import os
import sys
from gi.repository import Gtk, Gio, Gdk

from window import Window

class SimplyUbuntuApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        self._win = Window(self)
        self._win.present()

if __name__ == '__main__':
    app = SimplyUbuntuApplication()
    sys.exit(app.run(sys.argv))
