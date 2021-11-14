# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import pytest


class TestCommand:
    def test_name(self, command):
        assert command.name == 'echo "test"'

    def test__repr__(self, command):
        assert repr(command) == f'<Command {command.name}>'


class TestPack:
    def test_add(self, pack, command):
        pack.add(command)
        assert command in pack.commands

    def test_add_commands(self, pack, commands):
        pack.add_commands(commands)
        assert all([command in pack.commands for command in commands])

    def test_remove(self, pack, commands):
        pack.add_commands(commands)
        command = commands[0]
        assert command in pack.commands
        pack.remove(command)
        assert command not in pack.commands

    def test_get_commands(self, pack, commands):
        command = commands[0]
        pack.add_commands(commands)
        assert command in [c for c in pack.get_commands()]

    def test_commands(self, pack, commands):
        pack.add_commands(commands)
        assert isinstance(pack.commands, list)
        assert commands == pack.commands

    def test_name(self, pack):
        assert pack.name == 'Test'

    def test_count(self, pack, commands):
        pack.add_commands(commands)
        count = len(commands)
        assert pack.count == count

    def test_repr(self, pack):
        assert repr(pack) == f'<Pack {pack.name}>'

    def test_type_err(self, pack):
        with pytest.raises(TypeError):
            pack.add(8)
