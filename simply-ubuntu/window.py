from gi.repository import Gtk, Gio, Gdk
from gettext import gettext as _

import utils

class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)
        self.set_title(_('Simply Ubuntu'))
        self.set_default_size(400,500)
        self._setupView()

    def _setupView(self):
        builder = Gtk.Builder()
        builder.add_from_file(utils.getUserInterface())
        layout = builder.get_object('layout')
        self.add(layout)
