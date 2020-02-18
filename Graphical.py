#!/usr/bin/python3

import ChordPicker
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

numbertoggle = False

class Handler:
    def quit(self, *args):
        Gtk.main_quit()

    def random(self):
        if number.get_active():
            if MmSwitch.get_active():
                buffer.set_text(ChordPicker.NumberPkr("m"), 3)
            else:
                buffer.set_text(ChordPicker.NumberPkr(""), 3)
        else:
            buffer.set_text(ChordPicker.CheckChord(ChordPicker.PickChord()), 3)

if __name__ == "__main__":
    builder = Gtk.Builder()
    builder.add_from_file("gui.glade")
    builder.connect_signals(Handler)
    window = builder.get_object("window")
    buffer = builder.get_object("entrybuffer1")
    pick = builder.get_object("pickbutton")
    entry = builder.get_object("entry")
    entry.modify_font(Pango.FontDescription("glass gauge 30"))
    number = builder.get_object("number")
    MmSwitch = builder.get_object("MmSwitch")

    window.show_all()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()
