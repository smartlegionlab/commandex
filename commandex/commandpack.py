# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class Command:
    """Command"""
    def __init__(self, name):
        self._name = str(name)

    @property
    def name(self):
        """Command as a string"""
        return self._name

    def __repr__(self):
        return f'<Command {self._name}>'


class Pack:
    """Command Package"""
    def __init__(self, name):
        self._commands = []
        self._name = str(name)

    def add(self, command: Command):
        """
        Add a command.

        :param command: - Command object.
        :return: None.

        """
        if not isinstance(command, Command):
            raise TypeError
        self._commands.append(command)

    def add_commands(self, commands):
        """
        Add Commands.

        :param commands: iterator with Command objects.
        :return: None

        """
        for command in commands:
            if isinstance(command, Command):
                self.add(command)

    def remove(self, command: Command):
        """
        Remove command.

        :param command: - Command object.
        :return: None

        """
        if command in self._commands:
            index = self._commands.index(command)
            del self._commands[index]

    def get_commands(self):
        """
        Get all the commands from the package.

        :return: - generator with command objects.

        """
        return (command for command in self._commands)

    @property
    def commands(self):
        """Commands list"""
        return self._commands

    @property
    def name(self):
        """Pack name"""
        return self._name

    @property
    def count(self):
        """Commands count"""
        return len(self._commands)

    def __repr__(self):
        return f'<Pack {self._name}>'
