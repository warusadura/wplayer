# Copyright (C) 2022 Dhanuka Warusadura

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

GLADE_FILE = os.getcwd() + '/gui/gui.glade'

def init():
    builder = Gtk.Builder()
    builder.add_from_file(GLADE_FILE)
    window = window = builder.get_object('window')
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    Gtk.main()
