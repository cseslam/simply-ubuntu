from gi.repository import Gtk, Gio, Gdk
from gettext import gettext as _

import utils

OPERATIONS = {
    "OP1" : "fix arabic joined letters",
    "OP2" : "improve mozilla firefox fonts",
    "OP3" : "always position windows in center of screen",
    "OP4" : "",
    "OP5" : "install ubuntu restricted extras",
    "OP6" : "install java bundle",
}

class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)
        self.set_title(_('Simply Ubuntu'))
        self.set_default_size(400,500)
        self.operations = utils.Operations()
        self.switches = {}
        self._setupView()

    def _setupView(self):
        builder = Gtk.Builder()
        builder.add_from_file(utils.getUserInterface())
        layout = builder.get_object('layout')
        self.add(layout)
        self.switches['master'] = builder.get_object('switchAll')
        self.switches[1] = builder.get_object('switch1')
        self.switches[2] = builder.get_object('switch2')
        self.switches[3] = builder.get_object('switch3')
        self.switches[4] = builder.get_object('switch4')
        self.switches[5] = builder.get_object('switch5')
        self.switches[6] = builder.get_object('switch6')
        #connect signals
        self.switches['master'].connect("notify::active", self._onMasterActivate)
        self.switches[1].connect("notify::active", self._onSwitch1)
        self.switches[2].connect("notify::active", self._onSwitch2)
        self.switches[3].connect("notify::active", self._onSwitch3)
        self.switches[4].connect("notify::active", self._onSwitch4)
        self.switches[5].connect("notify::active", self._onSwitch5)
        self.switches[6].connect("notify::active", self._onSwitch6)

    def _onMasterActivate(self, switch, active):
        for s in self.switches:
            if s != 'master':
                self.switches[s].set_active(switch.get_active())

    def _onSwitch1(self, switch, active):
        self.operations.setOperation('OP1')

    def _onSwitch2(self, switch, active):
        self.operations.setOperation('OP2')

    def _onSwitch3(self, switch, active):
        self.operations.setOperation('OP3')

    def _onSwitch4(self, switch, active):
        self.operations.setOperation('OP4')

    def _onSwitch5(self, switch, active):
        self.operations.setOperation('OP5')

    def _onSwitch6(self, switch, active):
        self.operations.setOperation('OP6')
