# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from commandex.commandpack import Command, Pack
from commandex.executors import OsExecutor, SubExecutor, Executor
from commandex.maker import PackMaker
from commandex.parsers import CfgParser, JsonParser, Parser


class ExecutorsFactory:
    """Executors factory"""

    @classmethod
    def get_os_executor(cls):
        """Get OsExecutor"""
        return OsExecutor()

    @classmethod
    def get_sub_executor(cls):
        """Get SubExecutor"""
        return SubExecutor()

    @classmethod
    def get_executor(cls):
        """Get Executor"""
        return Executor()


class CommandPackFactory:
    @classmethod
    def create_command(cls, name):
        return Command(name)

    @classmethod
    def create_pack(cls, name):
        return Pack(name)


class MakerFactory:
    @classmethod
    def get_pack_maker(cls):
        return PackMaker()


class ParsersFactory:
    @classmethod
    def get_cfg_parser(cls):
        return CfgParser()

    @classmethod
    def get_json_parser(cls):
        return JsonParser()

    @classmethod
    def get_parser(cls):
        return Parser()


class CommandExFactory:
    """CommandEx factory"""
    executors = ExecutorsFactory()
    command_pack = CommandPackFactory()
    maker = MakerFactory()
    parsers = ParsersFactory()
