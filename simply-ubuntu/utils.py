import os
from subprocess import call

def getUserInterface():
    path = '/usr/share/layout.ui'
    if os.path.exists(path):
        return path
    else:
        return '../data/layout.ui'

class Operations():
    def __init__(self):
        pass

    def _installPackage(self, pkgName):
        call([""], shell=True)

    def getOperation(self, op):
        if op == "OP1":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP2":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP3":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP4":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP5":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP5":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        return boolean

    def setOperation(self, op):
        if op == "OP1":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP2":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP3":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP4":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP5":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]
        elif op == "OP5":
            call['sudo update-alternatives --set xinput-all_ALL /etc/X11/xinit/xinput.d/default-xim', shell=True]


"""
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
"""

