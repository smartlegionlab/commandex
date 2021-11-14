# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import json
from abc import ABC, abstractmethod
from pathlib import Path

from commandex.commandpack import Pack, Command


class ParserBase(ABC):
    """Abstract parser"""
    @abstractmethod
    def parse(self, file):
        """Parse file"""

    def __call__(self, file):
        return self.parse(file)


class CfgParser(ParserBase):

    def parse(self, file):
        packs = []
        try:
            pack = None
            with open(file, 'r') as f:
                lines = f.readlines()
        except (FileNotFoundError, PermissionError, OSError):
            return []
        else:
            for line in lines:
                line = line.rstrip('\n')
                if (len(line) > 0 and not line.startswith('#')
                        and line.startswith('[') and line.endswith(']')):
                    line = line.rstrip(']').lstrip('[')
                    pack = Pack(str(line))
                    packs.append(pack)
                else:
                    if pack in packs and line:
                        index = packs.index(pack)
                        packs[index].add(Command(str(line)))
        return packs


class JsonParser(ParserBase):

    def parse(self, file):
        packs = []
        try:
            with open(file, 'r') as f:
                json_data = json.load(f)
        except (
                json.decoder.JSONDecodeError,
                FileNotFoundError,
                PermissionError,
                OSError
        ):
            return []
        else:
            for pack_name, commands in json_data.items():
                pack = Pack(pack_name)
                packs.append(pack)
                index = packs.index(pack)
                command_gen = (Command(command) for command in commands if command)
                packs[index].add_commands(command_gen)
            return packs


class Parser(ParserBase):
    def __init__(self):
        self.cfg = CfgParser()
        self.json = JsonParser()

    def parse(self, file):
        suffix = Path(file).suffix
        parser = self._get_parser(suffix)
        return parser.parse(file)

    def _get_parser(self, suffix):
        if suffix == '.json':
            return self.json
        return self.cfg
