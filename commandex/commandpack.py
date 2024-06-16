# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------


class Pack:
    def __init__(self, name, commands=None):
        self._commands = [] if commands is None or not isinstance(commands, list) else commands
        self._name = str(name)

    def add(self, command):
        self._commands.append(str(command))

    def remove(self, command):
        if command in self._commands:
            index = self._commands.index(command)
            del self._commands[index]

    @property
    def commands(self):
        return self._commands

    @property
    def name(self):
        return self._name

    @property
    def command_count(self):
        return len(self._commands)

    def __repr__(self):
        return f'<Pack {self._name}>'
