# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------


class TestPack:
    def test_add(self, pack, command):
        pack.add(command)
        assert command in pack.commands

    def test_remove(self, pack, command):
        pack.add(command)
        assert command in pack.commands
        pack.remove(command)
        assert command not in pack.commands

    def test_commands(self, pack, commands):
        for command in commands:
            pack.add(command)
        assert isinstance(pack.commands, list)
        assert commands == pack.commands

    def test_name(self, pack):
        assert pack.name == 'Test'

    def test_command_count(self, pack, commands):
        for command in commands:
            pack.add(command)
        count = len(commands)
        assert pack.command_count == count

    def test_repr(self, pack):
        assert repr(pack) == f'<Pack {pack.name}>'
