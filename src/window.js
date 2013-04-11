/*
 * Copyright (c) 2013 Eslam Mostafa.
 *
 * Simply Ubuntu is free software; you can Public License as published by the
 * Free Software Foundation; either version 2 of the License, or (at your
 * option) any later version.
 *
 * Simply Ubuntu is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with Gnome Music; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 *
 * Author: Eslam Mostafa <cseslam@gmail.com>
 *
 */

const Lang = imports.lang;
const Gtk = imports.gi.Gtk;
const GLib = imports.gi.GLib;

const Gettext = imports.gettext;
const _ = imports.gettext.gettext;

const MainWindow = new Lang.Class({
    Name: "MainWindow",
    Extends: Gtk.ApplicationWindow,

    _init: function (app) {
        this.parent({
            application: app,
            title: _('Music'),
            window_position: Gtk.WindowPosition.CENTER,
            hide_titlebar_when_maximized: true
        });

        this.set_default_size(640, 400);
        this._setupView();
    },

    _setupView: function () {
        this._grid = new Gtk.Grid();
        this.add(this._grid);
        this.show_all();
    }
});
