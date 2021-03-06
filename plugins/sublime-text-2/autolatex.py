#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# autolatex/autolatex.py
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

import sublime, sublime_plugin
from utils import runner_command


class AutolatexCommand(sublime_plugin.WindowCommand, runner_command.AbstractRunnerCommand):

	def run(	self,
			cmd = [], file_regex = "", line_regex = "", working_dir = "",
			encoding = "utf-8", env = {}, quiet = False, kill = False,
			# Catches "path" and "shell"
			**kwargs):
		if kill:
			self.cancel_task()
		else:
			self.start_task(
				not quiet,
				encoding,
				working_dir,
				'all',
				['--noview'])


