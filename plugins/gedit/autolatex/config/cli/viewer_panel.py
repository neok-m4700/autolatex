# autolatex/config/cli/viewer_panel.py
# Copyright (C) 2013  Stephane Galland <galland@arakhne.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

#---------------------------------
# IMPORTS
#---------------------------------

# Include the Glib, Gtk and Gedit libraries
from gi.repository import GObject, Gdk, Gtk, GdkPixbuf
# AutoLaTeX internal libs
from ...utils import utils
from . import abstract_panel

#---------------------------------
# INTERNATIONALIZATION
#---------------------------------

import gettext
_T = gettext.gettext

#---------------------------------
# CLASS Panel
#---------------------------------

# Gtk panel that is managing the configuration of the viewer
class Panel(abstract_panel.AbstractPanel):
	__gtype_name__ = "AutoLaTeXViewerPanel"

	def __init__(self, is_document_level, directory, window):
		abstract_panel.AbstractPanel.__init__(self, is_document_level, directory, window)

	#
	# Fill the grid
	#
	def _init_widgets(self):
		# Launch the viewer
		self._ui_launch_viewer_checkbox = self._create_switch(
				_T("Launch a viewer after compilation"))[1]
		# Viewer command line
		tab = self._create_entry(
				_T("Command for launching the viewer (optional)"))
		self._ui_viewer_command_label = tab[0]
		self._ui_viewer_command_field = tab[1]


	#
	# Initialize the content
	#
	def _init_content(self):
		self._read_settings('viewer')
		self._ui_launch_viewer_checkbox.set_active(self._get_settings_bool('view', True))
		self._ui_viewer_command_field.set_text(self._get_settings_str('viewer'))
		self._update_widget_states()


	#
	# Connect signals
	#
	def _connect_signals(self):
		self._ui_launch_viewer_checkbox.connect('notify::active',self.on_launch_viewer_toggled)




	# Change the state of the widgets according to the state of other widgets
	def _update_widget_states(self):
		if self._ui_launch_viewer_checkbox.get_active():
			self._ui_viewer_command_label.set_sensitive(True)
			self._ui_viewer_command_field.set_sensitive(True)
		else:
			self._ui_viewer_command_label.set_sensitive(False)
			self._ui_viewer_command_field.set_sensitive(False)

	# Invoke when the flag 'launch viewer' has changed
	def on_launch_viewer_toggled(self, widget, data=None):
		self._update_widget_states()

	# Invoked when the changes in the panel must be saved
	def save(self):
		self._reset_settings_section()
		self._set_settings_bool('view', self._ui_launch_viewer_checkbox.get_active())
		self._set_settings_str('viewer', self._ui_viewer_command_field.get_text())
		return utils.backend_set_configuration(self._directory, 'project' if self._is_document_level else 'user', self._settings)
