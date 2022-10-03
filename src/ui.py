# Copyright (C) 2022 Dhanuka Warusadura

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from engine import execute

GLADE_FILE = os.getcwd() + '/gui/gui.glade'

builder = Gtk.Builder()
builder.add_from_file(GLADE_FILE)

def get_file(data):
    file_chooser = builder.get_object('file_chooser')
    file_name = file_chooser.get_filename()
    execute(file_name)

def init():
    handlers = {
        'has_file': get_file,
    }

    builder.connect_signals(handlers)

    window = builder.get_object('window')
    window.connect('destroy', Gtk.main_quit)
    window.show_all()

    Gtk.main()