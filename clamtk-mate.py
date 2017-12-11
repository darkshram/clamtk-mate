#!/usr/bin/python
# clamtk-mate version 0.02.01
#
# ClamTk, copyright (C) 2004-2017 Dave M
# clamtk-mate, copyright (C) 2017-2018 Joel Barrios
#
# This file was part of ClamTk (https://dave-theunsub.github.io/clamtk/).
#
# ClamTk is free software; you can redistribute it and/or modify it
# under the terms of either:
#
# a) the GNU General Public License as published by the Free Software
# Foundation; either version 1, or (at your option) any later version, or
#
# b) the "Artistic License".

import os
import pipes

import locale
locale.setlocale(locale.LC_ALL, '')

import gettext
_ = lambda x: gettext.ldgettext("clamtk-mate", x)

from gi.repository import Caja, GObject


class OpenTerminalExtension(GObject.GObject, Caja.MenuProvider):
    def __init__(self):
        print("Initializing clamtk-mate")

    def _open_scanner(self, file):
        filename = file.get_location().get_path()
        #- file is of type caja-vsf-file
        # https://github.com/GNOME/nautilus/blob/master/src/nautilus-file.h
        # which inherits from caja-file
        # https://github.com/GNOME/nautilus/blob/master/src/nautilus-vfs-file.h
        #- get_location returns a GFile
        # https://developer.gnome.org/gio/stable/GFile.html
        # which has the get_path function which returns the absolute path as a string
        filename = pipes.quote(filename)
        # - when switching to Python 3 we can use shlex.quote() instead

        os.system('clamtk %s &' % filename)

    def menu_activate_cb(self, menu, file):
        self._open_scanner(file)

    def menu_background_activate_cb(self, menu, file): 
        self._open_scanner(file)

    def get_file_items(self, window, files):
        if len(files) != 1:
            return
        file = files[0]

        item = Caja.MenuItem(
            name='CajaPython::openscanner',
            label=_('Scan for threats...') ,
            tip=_('Scan %s for threats...') % file.get_name(),
            icon='clamtk')
        # - the tooltips are not shown any longer in Caja
        # (the code is kept here in case this changes again for Caja
        item.connect('activate', self.menu_activate_cb, file)

        return [item]

    def get_background_items(self, window, file):
        item = Caja.MenuItem(
            name='CajaPython::openscanner_directory',
            label=_('Scan directory for threats...'),
            tip=_('Scan this directory for threats...'),
            icon='clamtk')
        # - the tooltips are not shown any longer in Caja
        # (the code is kept here in case this changes again for Caja
        item.connect('activate', self.menu_background_activate_cb, file)

        return [item]
