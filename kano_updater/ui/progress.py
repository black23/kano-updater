
# progress.py
#
# Copyright (C) 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Thread-safe progress reporting for Gtk
#

from gi.repository import GLib

from kano_updater.progress import Progress

class GtkProgress(Progress):

    def __init__(self, window):
        super(GtkProgress, self).__init__()
        self._window = window

    def _change(self, percent, msg):
        GLib.idle_add(self._window.update_progress, percent, msg)

    def _change_per_phase(self, percent, phase, msg):
        pass
