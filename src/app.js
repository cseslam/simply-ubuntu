const Lang = imports.lang;
const Gtk = imports.gi.Gtk;
const GLib = imports.gi.GLib;

const Gettext = imports.gettext;
const _ = imports.gettext.gettext;

const Window = imports.window;

const SimplyUbuntu = new Lang.Class({
    Name: "SimplyUbuntuApplication",
    Extends: Gtk.Application,

    _init: function () {
        this.parent({
            application_id: 'org.gnome.Music',
            flags: Gio.ApplicationFlags.FLAGS_NONE,
            inactivity_timeout: 12000
        });

        GLib.set_application_name(_("Music"));
    }

    vfunc_startup: function () {
        this.parent();
    }

    vfunc_activate: function () {
        this._window = new Window.Window();
    }
});



