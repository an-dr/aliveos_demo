#!/usr/bin/env python3
# *************************************************************************
#
# Copyright (c) 2021 Andrei Gramakov. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# site:    https://agramakov.me
# e-mail:  mail@agramakov.me
#
# *************************************************************************

from aliveos_app import ReflexNode
from os.path import dirname


class ReflexSimple(ReflexNode):
    def callback_perception_concept(self, symbol, modifier):
        if symbol == "simple_reflex_shiver":
            self.send_cmd("simple_reflex_shiver")


node = ReflexSimple("simple_reflex", [f"{dirname(__file__)}/simple_reflex_cc_dsc.json"])
node()
